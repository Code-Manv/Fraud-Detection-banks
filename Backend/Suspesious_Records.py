from sklearn.ensemble import IsolationForest

def detect_outlier_behaviour(df):
    target_features = df.loc[:, ["age", "amount"]]

    model = IsolationForest(
        n_estimators=100,
        contamination=0.2,
        random_state=42
    )

    prediction = model.fit_predict(target_features)

    updated_df = df.copy()
    updated_df["anomaly_flag"] = prediction

    return updated_df