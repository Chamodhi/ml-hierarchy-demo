def classify_risk(score):
    if score >= 90:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"