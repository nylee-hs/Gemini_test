import sqlite3
import streamlit as st
import pandas as pd
import datetime

# SQLite 데이터베이스 연결 함수
def create_connection():
    conn = sqlite3.connect(st.secrets['db_name'])
    return conn

# 테이블 생성 함수 (앱 실행 시 테이블이 없으면 생성)
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                q1 INTEGER NOT NULL,
                q2 INTEGER NOT NULL,
                q3 INTEGER NOT NULL,
                q4 INTEGER NOT NULL,
                q5 INTEGER NOT NULL,
                q6 INTEGER NOT NULL,
                dtime DATETIME NOT NULL
            )
        ''')
    conn.commit()
    conn.close()

# 데이터 삽입 함수
def insert_response(q_list):
    conn = create_connection()
    cursor = conn.cursor()
    q_label = ''
    print('>>>>>', q_list)
    for i in range(len(q_list)):
        if i == len(q_list)-1:
            q_label += f'q{i+1}, dtime'
        else:
            q_label += f'q{i + 1}, '

    st.write(q_label)
    q_list.append(datetime.datetime.now())
    q_values = ', '.join(['?' for x in q_list])
    sql_str = f'INSERT INTO results ({q_label}) VALUES ({q_values})'
    st.write(sql_str)
    st.write(tuple(q_list))
    cursor.execute(sql_str, tuple(q_list))
    conn.commit()
    conn.close()

# 데이터 조회 함수
def get_result():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM results", conn)
    conn.close()
    return df
