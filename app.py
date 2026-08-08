import streamlit as st
from main import analyze_multiple

st.title("AI 投資分析系統")

tickers_input = st.text_input("輸入股票代號", "NVDA,AMD,AVGO")

if st.button("開始分析"):
    tickers = tickers_input.split(",")
    results = analyze_multiple(tickers)

    for r in results:
        st.write(f"{r['ticker']} - {r['score']}/{r['total']}")
