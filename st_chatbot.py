import google.generativeai as genai
import streamlit as st


st.title('이조수 챗봇')
api_key = st.secrets['google_api_key']

# @st.cache_resouce
def load_model():
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    # print('model loaded...')
    return model

model = load_model()

if 'chat_session' not in st.session_state:
    st.session_state['chat_session'] = model.start_chat(history=[])

for content in st.session_state.chat_session.history:
    with st.chat_message('ai' if content.role=='model' else 'user'):
        st.markdown(content.parts[0].text)

with st.chat_message("ai"):
    st.write("안녕하세요. 저는 이조수 입니다. 무엇이든 물어보세요~")

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
