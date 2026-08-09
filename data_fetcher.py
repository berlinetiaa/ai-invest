import yfinance as yf
def get_financial_data(ticker_symbol):
    t = yf.Ticker(ticker_symbol)
    income = t.financials
    balance = t.balance_sheet
    cashflow = t.cashflow
    info = t.info

    def safe_get(df, key):
        try:
            return df.loc[key].head(5).tolist()
        except:
            return []

    def safe_info(key):
        return info.get(key, None)

    return {
        "revenue": safe_get(income, "Total Revenue"),
        "gross_profit": safe_get(income, "Gross Profit"),
        "net_income": safe_get(income, "Net Income"),
        "operating_income": safe_get(income, "Operating Income"),
        "ocf": safe_get(cashflow, "Total Cash From Operating Activities"),
        "capex": safe_get(cashflow, "Capital Expenditures"),
        "total_assets": safe_get(balance, "Total Assets"),
        "current_assets": safe_get(balance, "Total Current Assets"),
        "current_liabilities": safe_get(balance, "Total Current Liabilities"),
        "de_ratio": safe_info("debtToEquity"),
        "current_ratio": safe_info("currentRatio"),
        "roe": safe_info("returnOnEquity"),
    }
