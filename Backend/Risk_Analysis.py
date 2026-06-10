def compute_risk_score(record):
    score = 0

    age_flag = record["age"] > 100
    if age_flag:
        score += 35

    high_value = record["amount"] >= 60000
    if high_value:
        score += 30

    # Machine learning anomaly indicator
    anomaly_detected = record["anomaly"] == -1
    if anomaly_detected:
        score += 50

    return score