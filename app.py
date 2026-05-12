import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="OSS_PROJECT_3",
    page_icon="🐯",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("## 사용자 정보")
name = st.text_input("이름", "김민서")
age = st.number_input("나이", min_value=0, max_value=120, value=24)
option = st.selectbox(
    "좋아하는 프로그래밍 언어", ["c", "C++", "Python", "Java", "JavaScript"]
)
st.write(f"선택: {option}")

if st.button("완료"):
    st.balloons()
