from data_fetcher import get_financial_data
from analyzer import calculate_extra_metrics, apply_full_rules, summarize

def analyze_stock(ticker):
    data = get_financial_data(ticker)
    extra = calculate_extra_metrics(data)
    results = apply_full_rules(data, extra)
    summary = summarize(results)
    return {"ticker": ticker, "score": summary["passed"], "total": summary["total"], "pass": summary["pass_threshold"]}

def analyze_multiple(tickers):
    results = []
    for t in tickers:
        try:
            results.append(analyze_stock(t.strip()))
        except:
            pass
    return sorted(results, key=lambda x: x["score"], reverse=True)
