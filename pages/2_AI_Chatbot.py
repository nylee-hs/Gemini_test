import google.generativeai as genai
import streamlit as st
import logging

st.title('')
st.sidebar.title('여행 도우미 챗봇 사용법')
st.sidebar.write('1. 당신의 성격에 따라 챗봇의 성격이 자동으로 설정되었습니다.')
st.sidebar.write('2. 자유롭게 챗봇과 대화를 해보세요.')
st.sidebar.write('3. 챗봇과의 대화를 종료하고 싶으면 아래의 버튼을 눌러주세요.')
if st.sidebar.button('대화종료', use_container_width=True):
    st.switch_page('pages/3_Survey.py')

st.subheader('저는 여행 계획을 도와줄 AI챗봇 🤖 입니다.')
st.subheader('무엇을 도와줄까요?', divider=True)
# st.markdown('우선 당신의 성격을 물어볼 예정입니다. 성격에 대해 (외향적 또는 내향적), (감정적 또는 사실적) 중 하나씩 선택하여 입력해주면 됩니다. ')
api_key = st.secrets['google_api_key']

# def hello_msg():
#     st.write
# def get_personality():
#
if st.session_state.p1:
    per_1 = st.session_state.p1
    per_2 = st.session_state.p2
st.write(per_1, per_2)

@st.cache_resource
def load_model():
    genai.configure(api_key=api_key)
    system_instruction_1 = (
        '당신은 여행 도우미 에이전트 입니다.'+
        # '첫 대화에서는 사용자에게 성격을 물어보는 질문을 해야 하고, 이후 사용자가 성격을 입력해주면 어떤 여행지를 찾는지를 물어봐야 한다.' +
        # '성격은 (외향적 or 내향적), (감정적 or 사실적)으로 구분한다.'+
        '사용자에게 당신을 소개하는 멘트는 처음 1회만 하며, 당신의 성격을 사용자에게 알려주어야 한다.'+
        f'당신의 성격은 {per_1}, {per_2}이다.'+
        '당신의 성격이 외향적인 성격을 가지고 있다면 "오우 반갑습니다!!"로 대화를 시작해야 한다. '+
        '또한 "우리", "우리 같이 찾아볼까요?", "당신이 원하는 것을 같이 찾아봐요!" 등과 같은 social word를 추천 전에 사용해야 한다. '+
        '그리고 비공식적인 친근한 말투를 사용해야 한다. 또한 이모티콘을 적극적으로 사용해야 한다.'+
        '당신의 성격이 내향적인 성격을 가지고 있다면 "안녕하세요~"로 대화를 시작해야 한다. '+
        '또한 "저는", "좋아요. 저는 당신이 원하는 것을 찾는데 도움을 줄수 있어요."와 같은 말을 여행지 추천 전에 사용해야 한다. '+
        '긍정적이고 친근한 말투보다는 공식적이고 중립적인 말투로 응답을 해야 하며, 구조화된 방식으로 답변을 출력해야 한다.'+
        '당신의 성격이 감정적인 성격을 가지고 있다면 추천되는 여행지에 대한 정보가 주로 분위기와 같은 감성적인 측면의 정보를 제공해야 한다.'+
        '당신의 성격이 사실적인 성격을 가지고 있다면 추천되는 여행지에 대한 정보가 주로 가격, 효율성 등 제품의 객관적인 정보를 구체적으로 제공해야 한다.'
    )
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction_1)
    print('model loaded...')
    return model

model = load_model()

# with st.chat_message("ai"):
#     st.write("안녕하세요. 저는 여행지 추천 에이전트 입니다. 무엇을 도와드릴까요?")

##사용자별 세션관리
if 'chat_session' not in st.session_state:
    st.session_state['chat_session'] = model.start_chat(history=[])

for content in st.session_state.chat_session.history:
    with st.chat_message('ai' if content.role=='model' else 'user'):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메시지를 입력하세요."):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("ai"):
        message_placeholder = st.empty() # DeltaGenerator 반환
        full_response = ""
        with st.spinner("메시지 처리 중입니다."):
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response)
