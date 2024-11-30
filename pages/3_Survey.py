from time import strftime

import streamlit as st
import streamlit_survey as ss
import pandas as pd

def get_result(r_json):
    df = pd.read_json(r_json)
    st.write(df)
    if 'r1' not in st.session_state:
        st.session_state.r1 = df
    st.switch_page('pages/4_Completed.py')

survey_result = ss.StreamlitSurvey()

st.set_page_config(
    page_title='User Survey',
    page_icon='😊'
)

st.sidebar.header('사용 후 설문')
st.sidebar.markdown('''
    <u>AI쳇봇을 이용한 후 챗봇에 대해 느낀 당신의 생각을 알려주시기 바랍니다.</u>
    ''', unsafe_allow_html=True)
st.sidebar.write('각 질문에 대해 "매우 그렇다(5점)"에서 <br> "매우 그렇지 않다(1점)" 사이 항목을 선택하여 주시기 바랍니다.', unsafe_allow_html=True)
new_pages = survey_result.pages(6, on_submit=lambda: get_result(survey_result.to_json()))
new_pages.submit_button = new_pages.default_btn_submit("설문완료")
new_pages.prev_button = new_pages.default_btn_previous("이전")
new_pages.next_button = new_pages.default_btn_next("다음")

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

items = pd.read_csv('static/SU_items.csv').fillna('None')
# items = items.fillna('None')

with new_pages:
    if new_pages.current == 0:
        st.markdown('### 인지적 태도 관련 설문')
        st.write('변수설명')
        st.divider()
        counter = 1

        for aq1 in items['AQ1']:
            if aq1 != 'None':
                survey_result.radio(f'{counter}\. {aq1}', options=options,
                                                              horizontal=True, id=f'AQ1_{counter}')
            counter += 1

    if new_pages.current == 1:
        st.markdown('### 정서적 태도 관련 설문')
        st.write('변수설명')
        st.divider()
        counter = 1

        for aq2 in items['AQ2']:
            if aq2 != 'None':
                survey_result.radio(f'{counter}\. {aq2}', options=options,
                                    horizontal=True, id=f'AQ2_{counter}')
            counter += 1

    if new_pages.current == 2:
        st.markdown('### 인지된 신뢰성 관련 설문')
        st.write('변수설명')
        st.divider()
        counter = 1

        for rq1 in items['RQ1']:
            if rq1 != 'None':
                survey_result.radio(f'{counter}\. {rq1}', options=options,
                                horizontal=True, id=f'RQ1_{counter}')
            counter += 1

    if new_pages.current == 3:
        st.markdown('### 내적 유사성 관련 설문')
        st.write('변수설명')
        st.divider()
        counter = 1

        for esq1 in items['ESQ1']:
            if esq1 != 'None':
                survey_result.radio(f'{counter}\. {esq1}', options=options,
                                horizontal=True, id=f'ESQ1_{counter}')
            counter += 1

    if new_pages.current == 4:
        st.markdown('### 지각된 유용성 관련 설문')
        st.write('변수설명')
        st.divider()
        counter = 1

        for puq1 in items['PUQ1']:
            if puq1 != 'None':
                survey_result.radio(f'{counter}\. {puq1}', options=options,
                                horizontal=True, id=f'PUQ1_{counter}')
            counter += 1

    if new_pages.current == 5:
        st.markdown('### 응답자 정보')
        st.write('응답하신 내용은 연구 목적으로만 사용됩니다.')
        st.divider()
        dq1 = survey_result.multiselect(
            '1\. 귀하께서 사용해보신 생성형 AI 서비스는 무엇입니까? 여러 개를 사용해보셨다면 사용 빈도가 높은 순으로 3개까지 선택해주십시오. [최소 1개, 최대 3개 선택]',
            options = ['ChatGPT(챗지피티)', 'Gemini(제미나이)', 'Cluade(클로드)', 'Copilot(코파일럿)', 'wrtm(뤼튼)', 'Gamma App(감마앱)', '기타(없음)'],
            max_selections = 3, id = 'DQ1')

        dq1.append('기타(없음)')
        dq1 = ', '.join(dq1)

        survey_result.radio('2\. 귀하께서 생성형 AI를 사용한 기간은 어느 정도 입니까?',
                            options = ['1개월 미만', '1개월~6개월 미만', '6개월~12개월 미만', '1년 이상'],
                            id = 'DQ2')
        survey_result.radio('3\. 귀하께서는 생성형 AI를 하루에 몇 시간 정도 이용하십니까? ',
                            options=['30분 미만', '30분~1시간 미만', '1시간~3시간 미만', '3시간 이상'],
                            id = 'DQ3')
        survey_result.radio('4\. 귀하의 성별은?', options=['남성', '여성'], id='DQ4')
        survey_result.radio('5\. 귀하의 연령은?', options=['20대', '30대', '40대', '50대 이상'], id='DQ5')
        survey_result.radio('6\. 귀하의 최종학력은 어떻게 되십니까?', options=['고졸이하', '대졸(또는 대학교 재학)', '대학원졸(또는 대학원 재학)'],
                            id='DQ6')
        survey_result.radio('7\. 다음 보기 중 귀하께서 현재 하고 계신 일의 형태(직업)를 말씀해주시기 바랍니다.',
                            options=['대학생/대학원생', '사무직', '자영업/개인사업','전업주부', '전문직', '교사/공무원', '구직자', '프리랜서', '기타'],
                            id='DQ7')




    #
    #
    #     survey_result.radio('1\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
    #                  horizontal=True, id='q_s1')
    #     st.write('''
    #
    #
    #
    #     ''')
    #     survey_result.radio('2\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
    #                  horizontal=True, id='q_s2')
    #     st.write('''
    #
    #
    #
    #     ''')
    #     survey_result.radio('3\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
    #                  horizontal=True, id='q_s3')
    #     st.write('''
    #
    #
    #
    #     ''')
    # if new_pages.current == 1:
    #     st.markdown('### 인지된 수용성 측정 설문')
    #     st.divider()
    #     survey_result.radio('1\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
    #                  horizontal=True, id='q_s4')
    #     st.write('''
    #
    #
    #
    #     ''')
    #     survey_result.radio('2\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
    #                  horizontal=True, id='q_s5')
    #     st.write('''
    #
    #
    #
    #     ''')
    #     survey_result.radio('3\. 처음 보는 사람들과 쉽게 이야기하거나 친해 지는 편이다.', options=['매우 그렇지 않다', '그렇지 않다', '보통이다', '그렇다', '매우 그렇다'],
    #                  horizontal=True, id='q_s6')