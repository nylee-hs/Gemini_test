import streamlit as st
import streamlit_survey as ss
import pandas as pd
from attr.validators import disabled


# 사용자 성격 확인하는 함수(q_size = 첫번째 성격 설문 항목의 수)
def user_personlaity(user_json, q_size):
    df = pd.read_json(user_json)
    df = df.replace('매우 그렇지 않다', 1)
    df = df.replace('그렇지 않다', 2)
    df = df.replace('보통이다', 3)
    df = df.replace('그렇다', 4)
    df = df.replace('매우 그렇다', 5)
    # st.write(df)

    p1_a = df.filter(like = 'MQ1a_').iloc[2].sum()
    p1_b = df.filter(like = 'MQ1b_').iloc[2].sum()
    p2_a = df.filter(like = 'MQ2a_').iloc[2].sum()
    p2_b = df.filter(like='MQ2b_').iloc[2].sum()
    # st.write(p1_a, p1_b, p2_a, p2_b)

    if p1_b >= p1_a:
        p1 = 'E'
    else:
        p1 = 'I'
    if p2_b >= p2_a:
        p2 = 'F'
    else:
        p2 = 'T'

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
    font-size: 16px;
    font-weight: bold;
}
    </style>
    """, unsafe_allow_html=True)

options={
    '매우 그렇지 않다': 1,
    '그렇지 않다': 2,
    '보통이다': 3,
    '그렇다': 4,
    '매우 그렇다': 5
}

items = pd.read_csv('static/MQ_items.csv')
with pages:
    if pages.current == 0:
        st.markdown('### 내향성(intraversion)-외향성(extraversion) 측정 설문')
        st.markdown('- 각 질문의 A, B 두 문항을 읽으시고 두 문항의 합이 5점이 되는 범위 안에서 "매우 그렇다(5점)", "매우 그렇지 않다(0점)"으로 하여 각 문항의 빈칸에 점수를 표시하여 주시기 바랍니다.')
        st.markdown('- A항목의 값을 "매우 그렇다(5점)"으로 선택하였다면 B항목의 값은 자동으로 "매우 그렇지 않다(0점)으로 설정됩니다.')
        st.divider()
        counter = 1
        points=[]
        for a_item, a_index, b_item, b_index in zip(items['MQ1a'], items['MQ1a_in'], items['MQ1b'], items['MQ1b_in']):
            col1, col2 = st.columns(2)
            with col1:
                globals()['mq1a_%d'%counter] = survey_per.radio(f'{counter}-A\. {a_item}', options=options, horizontal=True, id=f'MQ1a_{counter}')
            with col2:
                globals()['mq1b_point%d'%counter] = 5 - options[globals()['mq1a_%d'%counter]]
                survey_per.radio(f'{counter}-B\. {b_item}', options=options, horizontal=True, index=globals()['mq1b_point%d'%counter], id=f'MQ1b_{counter}', disabled=True)
            counter += 1
            st.divider()

            # mq1a = survey_per.radio('1-a\. 다른 사람들과 상의하지 않고서 결정한다.', options=options,
            #          horizontal=True, id='MQ1a')
            # mq2a = survey_per.radio('2-a\. 혼자서 조용히 생각할 수 있는 시간이 좋다.', options=options,
            #                         horizontal=True, id='MQ2a')
            #     print(options[mq1a_1])
        # with col2:
        #     mq1b_index = 5 - options[mq1a]
        #     mq1b = survey_per.radio('1-b\. 다른 사람들의 생각을 안 연후에 결정한다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
        #              horizontal=True, id='MQ1b', index=mq1b_index)
        #     mq2b_index = 5 - options[mq1a]

    if pages.current == 1:
        st.markdown('### 사고(thinking)-감정(feeling) 측정 설문')
        st.markdown('- 각 질문의 A, B 두 문항을 읽으시고 두 문항의 합이 5점이 되는 범위 안에서 "가장 동의한다(5점)", "전혀 동의하지 않는다(0점)"으로 하여 각 문항의 빈칸에 점수를 표시하여 주시기 바랍니다.')
        st.markdown('- A항목의 값을 "매우 그렇다(5점)"으로 선택하였다면 B항목의 값은 자동으로 "매우 그렇지 않다(0점)으로 설정됩니다.')
        st.divider()
        counter = 1
        points = []
        for a_item, a_index, b_item, b_index in zip(items['MQ2a'], items['MQ2a_in'], items['MQ2b'], items['MQ2b_in']):
            col1, col2 = st.columns(2)
            with col1:
                globals()['mq2a_%d' % counter] = survey_per.radio(f'{counter}-A\. {a_item}', options=options,
                                                                  horizontal=True, id=f'MQ2a_{counter}')
            with col2:
                globals()['mq2b_point%d' % counter] = 5 - options[globals()['mq2a_%d' % counter]]
                survey_per.radio(f'{counter}-B\. {b_item}', options=options, horizontal=True,
                                 index=globals()['mq2b_point%d' % counter], id=f'MQ2b_{counter}', disabled=True)
            counter += 1
            st.divider()





