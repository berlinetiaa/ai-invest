from data_fetcher import get_financial_data
from analyzer import calculate_extra_metrics, calculate_16_metrics

def analyze_stock(ticker):
    data = get_financial_data(ticker)
    extra = calculate_extra_metrics(data)
    metrics = calculate_16_metrics(data, extra)
    score = sum(metrics.values())
    return {"ticker": ticker, "score": score, "detail": metrics}

def analyze_multiple(tickers):
    results = []
    for t in tickers:
        try:
            results.append(analyze_stock(t.strip()))
        except:
            pass
    return sorted(results, key=lambda x: x["score"], reverse=True)
