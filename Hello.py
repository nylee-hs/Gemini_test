import streamlit as st

# st.set_page_config(
#     page_title='Hello',
#     page_icon='👋'
# )
st.sidebar.header('안녕하세요')
st.write('# Welcome to Travel Recommendation with AI 👋')
st.sidebar.write('''
본 페이지는 연구목적으로 진행되는 페이지입니다.\n
궁금하신 점이 있으면 이남연교수(nylee@hs.ac.kr)에게 연락을 주시기 바랍니다.''')

st.markdown(
    '''
    본 실험은 사용자의 성격에 맞춰 여행과 관련한 추천 정보를 제공하는 AI 챗봇에 대한 사용자의 반응을 연구하는 목적의 실험입니다.\n
    👈 왼쪽의 사이드 바에 보시는 것과 같이 총 4단계로 진행됩니다. 
    #### 우선 당신의 성격을 간단한 설문을 통해 알아볼 예정입니다. 
    - 성격은 외향적(또는 내향적), 감정적(또는 사실적)의 두 가지의 성격을 측정합니다.\n
    #### 이후 AI챗봇이 특정한 성격을 부여받고 당신과 이야기를 진행할 예정입니다.
    - 여행과 관련한 자유로운 이야기를 진행하시면 됩니다.
    - 충분히 대화를 진행하였다면 "대화종료" 버튼을 누르시면 됩니다.\n
    #### 대화 종료 후 AI챗봇과의 대화에 대한 간단한 설문을 진행합니다.
    
    '''
)
#
if st.button('시작'):
    st.switch_page('pages/1_Personality.py')