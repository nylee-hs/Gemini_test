import streamlit as st
import pandasql as psql
import DBManager as dbm
import pprint

st.progress(100, '현재 진행 단계: 4/4')
st.divider()
st.markdown(
    '''
    ## 설문에 참여해 주셔서 감사합니다!  
    여러분의 소중한 의견은 저희 연구에 큰 도움이 됩니다.   
    추가 질문이나 의견이 있으시면 언제든지 아래의 연락처로 연락해 주세요.  
     
    이남연 교수(nylee@hs.ac.kr)  
    김준환 교수()
    
    감사합니다!   
    '''
)

st.balloons()

result = ''
per_1 = ''
per_2 = ''
if 'r1' in st.session_state:
    survey = st.session_state.r1
    survey = survey.replace('매우 그렇지 않다', 1)
    survey = survey.replace('그렇지 않다', 2)
    survey = survey.replace('보통이다', 3)
    survey = survey.replace('그렇다', 4)
    survey = survey.replace('매우 그렇다', 5)
    result = survey
    # st.write(result)
if 'p1' in st.session_state:
    per_1 = st.session_state.p1
    per_2 = st.session_state.p2
    # st.write(per_1, per_2)


def get_response(survey, per_1, per_2):
    values = survey.loc['value']
    values_list = values.tolist()
    # print('check!!', values_list)
    temp = values_list[49]
    temp = ', '.join(temp)
    # print('check!!!', temp)
    values_list[49] = temp
    values_list.append(per_1)
    values_list.append(per_2)
    # st.write(values_list)
    st.session_state['completed'] = False
    return values_list


dbm.create_table()
if 'completed' not in st.session_state:
    st.session_state['completed'] = False
    # pprint.pprint(st.session_state.r1.to_json())
    dbm.insert_response(get_response(result, per_1, per_2))
else:
    st.write('이미 설문을 완료하였습니다!')