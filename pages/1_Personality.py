import streamlit as st
import streamlit_survey as ss
import pandas as pd

# 사용자 성격 확인하는 함수(q_size = 첫번째 성격 설문 항목의 수)
def user_personlaity(user_json, q_size):
    df = pd.read_json(user_json)
    df = df.replace('매우 그렇지 않다', 1)
    df = df.replace('그렇지 않다', 2)
    df = df.replace('보통이다', 3)
    df = df.replace('그렇다', 4)
    df = df.replace('매우 그렇다', 5)

    # 성격 측정 설문 항목의 갯수에 따라 아래의 값이 변경되어야 함
    p1 = df.iloc[2, 0:q_size].mean()
    p2 = df.iloc[2, q_size:].mean()
    # st.write(p1, p2)
    if p1 >= 3:
        p1 = 'E'
    else:
        p1 = 'I'
    if p2 >= 3:
        p2 = 'T'
    else:
        p2 = 'F'

    # st.write(p1, p2)
    # st.dataframe(df, use_container_width=True)
    if 'p1' not in st.session_state:
        st.session_state.p1 = p1
        st.session_state.p2 = p2
    pages.current = 0
    st.switch_page('pages/2_AI_Chatbot.py')

survey_per = ss.StreamlitSurvey()

st.set_page_config(
    page_title='User Personality',
    page_icon='😊'
)

st.sidebar.header('사용자 성격 측정 페이지')
st.sidebar.write('''
    본 페이지는 사용자의 성격을 측정하는 페이지입니다. 성격은 크게 외향성의 정도와 감정적인 정도를 측정합니다.
    성격을 측정하는 이유는 사용자의 성격에 따라 AI챗봇의 성격을 변경하기 위해서입니다.
    
    ''')

pages = survey_per.pages(2, on_submit=lambda: user_personlaity(survey_per.to_json(), 3))
pages.submit_button = pages.default_btn_submit("설문완료")
pages.prev_button = pages.default_btn_previous("이전")
pages.next_button = pages.default_btn_next("다음")

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
}
    </style>
    """, unsafe_allow_html=True)

with pages:
    if pages.current == 0:
        st.markdown('### 외향성(extraversion)-내향성(intraversion) 측정 설문')
        st.divider()
        survey_per.radio('1\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q_p1')
        st.write('''
        
        
        
        ''')
        survey_per.radio('2\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q_p2')
        st.write('''



        ''')
        survey_per.radio('3\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q_p3')
        st.write('''



        ''')
    if pages.current == 1:
        st.markdown('### 사고(thinking)-감정(feeling) 측정 설문')
        st.divider()
        survey_per.radio('1\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q_p4')
        st.write('''



        ''')
        survey_per.radio('2\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q_p5')
        st.write('''



        ''')
        survey_per.radio('3\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q_p6')





