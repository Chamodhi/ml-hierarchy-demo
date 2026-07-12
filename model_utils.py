def classify_risk(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"
