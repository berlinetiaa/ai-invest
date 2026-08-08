def calculate_extra_metrics(data):
    results = {}
    if data["revenue"] and data["gross_profit"]:
        results["gross_margin"] = data["gross_profit"][0] / data["revenue"][0]
    if data["ocf"] and data["capex"]:
        results["fcf"] = data["ocf"][0] + data["capex"][0]
    if data["ocf"] and data["net_income"] and data["net_income"][0] != 0:
        results["quality"] = data["ocf"][0] / data["net_income"][0]
    if data["current_assets"] and data["current_liabilities"]:
        results["current_ratio_calc"] = data["current_assets"][0] / data["current_liabilities"][0]
    if data["revenue"] and data["total_assets"]:
        results["asset_turnover"] = data["revenue"][0] / data["total_assets"][0]
    return results

def apply_full_rules(data, extra):
    return {
        "P2": extra.get("gross_margin", 0) > 0.4,
        "A8": extra.get("fcf", 0) > 0,
        "A10": extra.get("quality", 0) > 0.8,
        "C11": data["de_ratio"] and data["de_ratio"] < 0.5,
        "C12": (data["current_ratio"] and data["current_ratio"] > 1) or extra.get("current_ratio_calc", 0) > 1,
        "E14": data["roe"] and data["roe"] > 0.15,
        "E15": extra.get("asset_turnover", 0) > 0.5
    }

def summarize(results):
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    return {"passed": passed, "total": total, "pass_threshold": passed >= 4}
