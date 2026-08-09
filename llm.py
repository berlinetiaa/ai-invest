import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_llm(prompt):
    try:
        r = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role":"user","content":prompt}],
        )
        return r.choices[0].message.content
    except:
        return "⚠️ AI分析未啟用（請設定API KEY）"

def build_prompt(ticker, detail, score):
    return f'''
你是巴菲特等級分析師
公司：{ticker}
通過：{score}/16
指標：{detail}
請輸出：優勢、風險、投資建議
'''
