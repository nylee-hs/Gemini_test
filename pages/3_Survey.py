from time import strftime

import streamlit as st
import streamlit_survey as ss
import pandas as pd

def get_result(r_json):
    df = pd.read_json(r_json)
    if 'r1' not in st.session_state:
        st.session_state.r1 = df
    st.switch_page('pages/4_Completed.py')

survey = ss.StreamlitSurvey()

st.set_page_config(
    page_title='User Survey',
    page_icon='😊'
)

st.sidebar.header('사용 후 설문')
st.sidebar.write('''
    AI쳇봇을 이용한 후 챗봇에 대해 느낀 당신의 생각을 알려주시기 바랍니다.
    

    ''')
new_pages = survey.pages(2, on_submit=lambda: get_result(survey.to_json()))
new_pages.submit_button = new_pages.default_btn_submit("설문완료")
new_pages.prev_button = new_pages.default_btn_previous("이전")
new_pages.next_button = new_pages.default_btn_next("다음")

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
}
    </style>
    """, unsafe_allow_html=True)

with new_pages:
    if new_pages.current == 0:
        st.markdown('### 사용 만족도 측정 설문')
        st.divider()
        survey.radio('1\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q1')
        st.write('''



        ''')
        survey.radio('2\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q2')
        st.write('''



        ''')
        survey.radio('3\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q3')
        st.write('''



        ''')
    if new_pages.current == 1:
        st.markdown('### 인지된 수용성 측정 설문')
        st.divider()
        survey.radio('1\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q4')
        st.write('''



        ''')
        survey.radio('2\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q5')
        st.write('''



        ''')
        survey.radio('3\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
                     horizontal=True, id='q6')