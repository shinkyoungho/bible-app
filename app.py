import streamlit as st
import requests
from datetime import datetime

# 1. 페이지 기본 설정
st.set_page_config(page_title="Gemini 매일 묵상 주해", layout="centered")

# 2. 디자인 꾸미기 (모바일에서 앱처럼 보이게 함)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&display=swap');
    .main { background-color: #f9f9f9; font-family: 'Nanum Myeongjo', serif; }
    .bible-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 20px; }
    .interpretation { line-height: 2.0; font-size: 1.15em; color: #2c3e50; white-space: pre-wrap; }
    .verse-header { color: #8e44ad; font-weight: bold; font-size: 1.2em; margin-bottom: 10px; border-left: 4px solid #8e44ad; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 불러오기 (이 부분은 제가 나중에 데이터 소스를 연결해 드릴게요)
def load_data():
    # 현재는 샘플 데이터를 보여주지만, 나중에 제가 매일 업데이트하는 서버 주소로 바꿀 겁니다.
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "title": "여호와는 나의 목자 (시편 23편)",
        "context": "고대 근동의 목축 문화와 다윗의 배경을 통한 서론...",
        "content": "여기에 Gemini가 작성한 15~20장 분량의 풍성한 각 절 주해가 들어갑니다."
    }

data = load_data()

# 4. 앱 화면 출력
st.title("🕊️ 오늘의 심층 주해")
st.write(f"**날짜:** {data['date']}")
st.markdown("---")

st.header(f"주제: {data['title']}")
st.subheader("🏛️ 고대 근동 배경 (Context)")
st.info(data['context'])

st.markdown("---")
st.markdown("### 📖 오늘의 상세 주해")
st.markdown(f"<div class='interpretation'>{data['content']}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("매일 아침 Gemini가 당신을 위한 설교적 주해를 준비합니다.")
