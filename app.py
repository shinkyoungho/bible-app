import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 디자인 설정
st.set_page_config(page_title="Gemini 매일 묵상 주해", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&display=swap');
    .main { background-color: #fcfcfc; font-family: 'Nanum Myeongjo', serif; }
    .bible-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-left: 5px solid #6c5ce7; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .interpretation { line-height: 2.1; font-size: 1.15em; color: #2d3436; white-space: pre-wrap; }
    .context-box { background-color: #f1f2f6; padding: 20px; border-radius: 10px; font-style: italic; color: #2f3542; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. 구글 시트 연결 (사용자님의 시트 ID 적용됨)
def load_data():
    sheet_id = "1nNSdd8vQXdaZ2OubF_WinhFqpBQjY9KlBOdZGPeWAzE"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
    try:
        df = pd.read_csv(url)
        return df.iloc[-1] # 가장 마지막 행 데이터
    except:
        return None

data = load_data()

# 3. 화면 출력
st.title("📖 오늘의 심층 주해 묵상")
st.write(f"**묵상 일시:** {datetime.now().strftime('%Y년 %m월 %d일')}")

if data is not None:
    st.header(f"주제: {data['제목']}")
    st.markdown("### 🏛️ 고대 근동 배경 (Context)")
    st.markdown(f"<div class='context-box'>{data['배경']}</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🕊️ 각 절 심층 주해")
    st.markdown(f"<div class='interpretation'>{data['주해']}</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📢 오늘의 적용")
    st.success(data['적용'])
else:
    st.info("구글 시트에 '제목, 배경, 주해, 적용' 항목으로 첫 줄을 만드시고 데이터를 입력해주세요!")
