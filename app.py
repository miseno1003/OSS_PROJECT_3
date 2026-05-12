import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="OSS_PROJECT_3",
    page_icon="🐯",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("## 사용자 정보")

user_id = st.text_input("아이디")
password = st.text_input("비밀번호", type="password")

if st.button("완료"):
    print(f"---------------------------------------------------", flush=True)
    print(f"[{datetime.now()}] 입력이 완료됨", flush=True)
    print(f"[{datetime.now()}] 입력된 아이디: {user_id}", flush=True)
    print(
        f"[{datetime.now()}] 입력된 비밀번호: {password}",
        flush=True,
    )

    st.success("입력이 완료되었습니다.")
    st.balloons()
