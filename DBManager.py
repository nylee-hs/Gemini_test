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

    ## 테이블의 구조 p1~px: 성격측정 항목 / r1~rx: 사후 설문항목
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                p1 INTEGER NOT NULL, p2 INTEGER NOT NULL, p3 INTEGER NOT NULL, p4 INTEGER NOT NULL,
                p5 INTEGER NOT NULL, p6 INTEGER NOT NULL,
                r1 INTEGER NOT NULL, r2 INTEGER NOT NULL, r3 INTEGER NOT NULL, r4 INTEGER NOT NULL,
                r5 INTEGER NOT NULL, r6 INTEGER NOT NULL,
                per_1 TEXT NOT NULL, per_2 TEXT NOT NULL,
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
    d_label = 'p1, p2, p3, p4, p5, p6, r1, r2, r3, r4, r5, r6, per_1, per_2, dtime'

    n_time = datetime.datetime.now()
    now_time = n_time.strftime('%Y-%m-%d %H:%M:%S')
    q_list.append(now_time)
    # q_values = ', '.join(['?' for x in q_list])
    sql_str = f'INSERT INTO results ({d_label}) VALUES {tuple(q_list)}'
    # st.write(sql_str)
    # st.write(tuple(q_list))
    cursor.execute(sql_str)
    conn.commit()
    conn.close()

# 데이터 조회 함수
def get_result():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM results", conn)
    conn.close()
    return df
