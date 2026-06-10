import streamlit as st

from Source_files.Cleaning import load_dataset, preprocess_data
from Source_files.Detection_of_dupes import detect_duplicate_records
from Source_files.Suspesious_Records import detect_outlier_behaviour

st.title("Fraud Detection Dashboard")

data = load_dataset()
data = preprocess_data(data)

duplicates = detect_duplicate_records(data)
processed_data = detect_outlier_behaviour(data)


st.subheader("Processed Dataset")
st.dataframe(processed_data)

st.subheader("Summary")

total_records = len(processed_data)

anomaly_count = (
    processed_data["anomaly_flag"] == -1
).sum()

col1, col2 = st.columns(2)

col1.metric(
    "Total Records",
    total_records
)

col2.metric(
    "Anomaly Cases",
    anomaly_count
)

st.subheader("Duplicate Records")
st.dataframe(duplicates)

st.subheader("Suspicious Records")

suspicious_records = processed_data[
    processed_data["anomaly_flag"] == -1
]

st.dataframe(suspicious_records)

st.subheader("Behavioral Analysis")

analysis_df = (
    processed_data
    .groupby("name")["anomaly_flag"]
    .apply(lambda x: (x == -1).sum())
    .reset_index()
)

analysis_df.columns = [
    "Name",
    "Anomaly_Count"
]

st.bar_chart(
    analysis_df.set_index("Name")
)

st.subheader("Top Suspicious Entities")

top_risky = (
    analysis_df
    .sort_values(
        by="Anomaly_Count",
        ascending=False
    )
    .head(5)
)

st.dataframe(top_risky)