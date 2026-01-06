import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 기본 설정 및 디자인
st.set_page_config(page_title="Gemini 매일 묵상 주해", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&display=swap');
    .main { background-color: #fcfcfc; font-family: 'Nanum Myeongjo', serif; }
    .bible-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-left: 5px solid #6c5ce7; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .interpretation { line-height: 2.1; font-size: 1.15em; color: #2d3436; white-space: pre-wrap; }
    .context-box { background-color: #f1f2f6; padding: 20px; border-radius: 10px; font-style: italic; color: #2f3542; margin-bottom: 20px; }
    .verse-title { color: #6c5ce7; font-weight: bold; font-size: 1.3em; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. 구글 시트 데이터 불러오기 함수
def load_data():
    # 사용자님이 주신 시트 ID
    sheet_id = "1nNSdd8vQXdaZ2OubF_WinhFqpBQjY9KlBOdZGPeWAzE"
    sheet_name = "Sheet1"  # 시트 하단 이름이 'Sheet1'이 아닐 경우 수정 필요
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    try:
        df = pd.read_csv(url)
        # 가장 최근(마지막 행) 데이터를 가져옴
        latest_data = df.iloc[-1]
        return latest_data
    except Exception as e:
        return None

# 3. 데이터 로드 및 화면 출력
data = load_data()

st.title("📖 오늘의 심층 주해 묵상")
today = datetime.now().strftime("%Y년 %m월 %d일")
st.write(f"**묵상 일시:** {today}")
st.markdown("---")

if data is not None:
    # 시트 열 이름을 '제목', '배경', '주해', '적용'으로 가정합니다.
    st.header(f"주제: {data['제목']}")
    
    st.markdown("### 🏛️ 고대 근동 배경 및 맥락 (Context)")
    st.markdown(f"<div class='context-box'>{data['배경']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🕊️ 각 절 심층 주해")
    st.markdown(f"<div class='interpretation'>{data['주해']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📢 오늘의 적용 및 질문")
    st.success(data['적용'])
else:
    st.warning("오늘의 묵상 데이터를 불러오는 중입니다. 잠시만 기다려 주시거나 구글 시트에 데이터가 있는지 확인해 주세요!")

st.markdown("---")
st.caption("Gemini가 제공하는 10점 만점의 10점 주해 시스템입니다.")
