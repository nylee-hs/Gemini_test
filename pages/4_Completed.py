import streamlit as st
import pandasql as psql
import DBManager as dbm

result = ''
if 'r1' in st.session_state:
    survey = st.session_state.r1
    survey = survey.replace('매우 그렇지 않다', 1)
    survey = survey.replace('그렇지 않다', 2)
    survey = survey.replace('보통이다', 3)
    survey = survey.replace('그렇다', 4)
    survey = survey.replace('매우 그렇다', 5)
    result = survey
    # st.write(result)

def get_response(survey):
    values = survey.loc['value']
    st.write(values.tolist())
    return values.tolist()


dbm.create_table()
dbm.insert_response(get_response(result))