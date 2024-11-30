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
                MQ1a_1 INTEGER NOT NULL, MQ1b_1 INTEGER NOT NULL, MQ1a_2 INTEGER NOT NULL, MQ1b_2 INTEGER NOT NULL,
                MQ1a_3 INTEGER NOT NULL, MQ1b_3 INTEGER NOT NULL, MQ1a_4 INTEGER NOT NULL, MQ1b_4 INTEGER NOT NULL,
                MQ1a_5 INTEGER NOT NULL, MQ1b_5 INTEGER NOT NULL, MQ1a_6 INTEGER NOT NULL, MQ1b_6 INTEGER NOT NULL,
                MQ1a_7 INTEGER NOT NULL, MQ1b_7 INTEGER NOT NULL, MQ1a_8 INTEGER NOT NULL, MQ1b_8 INTEGER NOT NULL,
                MQ2a_1 INTEGER NOT NULL, MQ2b_1 INTEGER NOT NULL, MQ2a_2 INTEGER NOT NULL, MQ2b_2 INTEGER NOT NULL,
                MQ2a_3 INTEGER NOT NULL, MQ2b_3 INTEGER NOT NULL, MQ2a_4 INTEGER NOT NULL, MQ2b_4 INTEGER NOT NULL,
                MQ2a_5 INTEGER NOT NULL, MQ2b_5 INTEGER NOT NULL, MQ2a_6 INTEGER NOT NULL, MQ2b_6 INTEGER NOT NULL,
                MQ2a_7 INTEGER NOT NULL, MQ2b_7 INTEGER NOT NULL, MQ2a_8 INTEGER NOT NULL, MQ2b_8 INTEGER NOT NULL,
                AQ1_1 INTEGER NOT NULL, AQ1_2 INTEGER NOT NULL, AQ1_3 INTEGER NOT NULL, AQ1_4 INTEGER NOT NULL,
                AQ2_1 INTEGER NOT NULL, AQ2_2 INTEGER NOT NULL, AQ2_3 INTEGER NOT NULL,
                RQ1_1 INTEGER NOT NULL, RQ1_2 INTEGER NOT NULL, RQ1_3 INTEGER NOT NULL,
                ESQ1_1 INTEGER NOT NULL, ESQ1_2 INTEGER NOT NULL, ESQ1_3 INTEGER NOT NULL,
                PUQ1_1 INTEGER NOT NULL, PUQ1_2 INTEGER NOT NULL, PUQ1_3 INTEGER NOT NULL, PUQ1_4 INTEGER NOT NULL,
                DQ1 TEXT NOT NULL, DQ2 TEXT NOT NULL, DQ3 TEXT NOT NULL, DQ4 TEXT NOT NULL,
                DQ5 TEXT NOT NULL, DQ6 TEXT NOT NULL, DQ7 TEXT NOT NULL,
                PER_1 TEXT NOT NULL, PER_2 TEXT NOT NULL,
                DTIME DATETIME NOT NULL
            )
        ''')
    conn.commit()
    conn.close()

# 데이터 삽입 함수
def insert_response(q_list):
    conn = create_connection()
    cursor = conn.cursor()
    q_label = ''
    # print(tuple(q_list))
    # d_label = 'p1, p2, p3, p4, p5, p6, r1, r2, r3, r4, r5, r6, per_1, per_2, dtime'
    d_label = "MQ1a_1, MQ1b_1, MQ1a_2, MQ1b_2, MQ1a_3, MQ1b_3, MQ1a_4, MQ1b_4, MQ1a_5, MQ1b_5, MQ1a_6, MQ1b_6, MQ1a_7, MQ1b_7, MQ1a_8, MQ1b_8, MQ2a_1, MQ2b_1, MQ2a_2, MQ2b_2, MQ2a_3, MQ2b_3, MQ2a_4, MQ2b_4, MQ2a_5, MQ2b_5, MQ2a_6, MQ2b_6, MQ2a_7, MQ2b_7, MQ2a_8, MQ2b_8, AQ1_1, AQ1_2, AQ1_3, AQ1_4, AQ2_1, AQ2_2, AQ2_3, RQ1_1, RQ1_2, RQ1_3, ESQ1_1, ESQ1_2, ESQ1_3, PUQ1_1, PUQ1_2, PUQ1_3, PUQ1_4, DQ1, DQ2, DQ3, DQ4, DQ5, DQ6, DQ7, PER_1, PER_2, DTIME"
    n_time = datetime.datetime.now()
    now_time = n_time.strftime('%Y-%m-%d %H:%M:%S')
    q_list.append(now_time)
    # print(q_list)
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
