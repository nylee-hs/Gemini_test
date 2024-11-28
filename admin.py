import streamlit as st
import DBManager as dbm

df = dbm.get_result()
st.write(df)
