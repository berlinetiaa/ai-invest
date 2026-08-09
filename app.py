import streamlit as st
import pandas as pd
from main import analyze_multiple
from llm import analyze_with_llm, build_prompt

st.title("🚀 AI 投資分析系統 PRO")

tickers = st.text_input("輸入股票代號", "NVDA,AMD,AVGO").split(",")

if st.button("開始分析"):
    results = analyze_multiple(tickers)
    df = pd.DataFrame(results)

    st.subheader("📊 排名")
    st.dataframe(df)

    st.subheader("📈 分數圖")
    st.bar_chart(df.set_index("ticker")["score"])

    st.subheader("🤖 AI分析")
    for r in results[:3]:
        prompt = build_prompt(r["ticker"], r["detail"], r["score"])
        report = analyze_with_llm(prompt)
        st.markdown(f"## {r['ticker']}")
        st.write(report)
