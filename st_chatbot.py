import google.generativeai as genai
import streamlit as st
import logging



st.title('여행 도우미 챗봇')
api_key = st.secrets['google_api_key']

# def hello_msg():
#     st.write
# def get_personality():
#

@st.cache_resource
def load_model():
    genai.configure(api_key=api_key)
    system_instruction_1 = (
        '당신은 여행 도우미 에이전트 입니다. '+
        '당신은 사용자의 MBTI와 동일한 성격을 가지고 대화스타일을 변경해야 합니다. '+
        '사용자가 외향성의 성격을 가지고 있다면 "오우 반갑습니다!!"로 대화를 시작해야 한다. '+
        '또한 "우리", "우리 같이 찾아볼까요?", "당신이 원하는 것을 같이 찾아봐요!" 등과 같은 social word를 추천 전에 사용해야 한다. '+
        '그리고 비공식적인 친근한 말투를 사용해야 한다. 또한 이모티콘을 적극적으로 사용해야 한다.'+
        '사용자가 내향적인 성격을 가지고 있다면 "안녕하세요~"로 대화를 시작해야 한다. '+
        '또한 "저는", "좋아요. 저는 당신이 원하는 것을 찾는데 도움을 줄수 있어요."와 같은 말을 여행지 추천 전에 사용해야 한다. '+
        '긍정적이고 친근한 말투보다는 공식적이고 중립적인 말투로 응답을 해야 하며, 구조화된 방식으로 답변을 출력해야 한다.'+
        '사용자가 감정적인 성격을 가지고 있다면 추천되는 여행지에 대한 정보가 주로 분위기와 같은 감성적인 측면의 정보를 제공해야 한다.'+
        '사용자가 사실적인 성격을 가지고 있다면 추천되는 여행지에 대한 정보가 주로 가격, 효율성 등 제품의 객관적인 정보를 구체적으로 제공해야 한다.'+
        '사용자가 성격을 입력해주면 어떤 여행지를 찾는지를 물어봐야 한다.'
    )
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction_1)
    print('model loaded...')
    return model

model = load_model()

with st.chat_message("ai"):
    st.write("안녕하세요. 저는 여행지 추천 에이전트 입니다. 우선 당신의 성격과 원하는 여행지를 알려주세요. 성격은 외향적/내향적, 사실적/감정적 중 하나씩 이야기 해주면 됩니다. (예: 외향적, 감정적)")

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
