import streamlit as st
import DBManager as dbm

st.write('이 페이지는 관리자용 페이지입니다.')

pw = st.text_input("비밀번호를 입력하세요.")

if pw == st.secrets['manager_pw']:
    df = dbm.get_result()
    st.dataframe(df, use_container_width=True)
# else:
#     st.write('비밀번호가 틀렸습니다.')
