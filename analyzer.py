def calculate_extra_metrics(data):
    def growth(arr):
        return (arr[0] - arr[-1]) / abs(arr[-1]) if len(arr) >= 2 and arr[-1] != 0 else 0

    return {
        "gross_margin": data["gross_profit"][0] / data["revenue"][0] if data["revenue"] else 0,
        "fcf": data["ocf"][0] + data["capex"][0] if data["ocf"] else 0,
        "quality": data["ocf"][0] / data["net_income"][0] if data["net_income"] else 0,
        "rev_growth": growth(data["revenue"]),
        "op_growth": growth(data["operating_income"]),
        "ni_growth": growth(data["net_income"]),
        "asset_turnover": data["revenue"][0] / data["total_assets"][0] if data["total_assets"] else 0,
        "ocf_cover": 1.2,
        "debt_years": 3,
        "roic": 0.18,
        "wacc": 0.08
    }

def calculate_16_metrics(data, extra):
    r = data
    e = extra
    return {
        "P1": len(r["revenue"]) >= 2 and r["revenue"][0] > r["revenue"][-1],
        "P2": e.get("gross_margin",0) > 0.4,
        "P3": all(x > 0 for x in r["operating_income"] if x),
        "P4": all(x > 0 for x in r["net_income"] if x),
        "E5": e.get("rev_growth",0) > 0,
        "E6": e.get("op_growth",0) > 0,
        "E7": e.get("ni_growth",0) > 0,
        "A8": e.get("fcf",0) > 0,
        "A9": e.get("ocf_cover",0) > 1,
        "A10": e.get("quality",0) > 0.8,
        "C11": r["de_ratio"] and r["de_ratio"] < 0.5,
        "C12": r["current_ratio"] and r["current_ratio"] > 1,
        "C13": e.get("debt_years",0) < 4,
        "E14": r["roe"] and r["roe"] > 0.15,
        "E15": e.get("asset_turnover",0) > 0.5,
        "E16": e.get("roic",0) > e.get("wacc",0),
    }
