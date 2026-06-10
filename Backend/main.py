from Cleaning import load_dataset, preprocess_data
from Detection_of_dupes import find_duplicates
from Suspesious_Records import detect_anomalies
from Network import construct_relationship_graph


def execute_fraud_detection_system():
    print("Initializing Fraud Detection System")

    raw_dataset = load_dataset()
    cleaned_dataset = preprocess_data(raw_dataset)

    duplicates_found = find_duplicates(cleaned_dataset)

    enriched_dataset = detect_anomalies(cleaned_dataset)

    def assign_risk_level(entry):
        risk_value = 0

        if entry["age"] > 100:
            risk_value += 45

        if entry["amount"] >= 60000:
            risk_value += 35

        if entry["anomaly"] == -1:
            risk_value += 50

        if risk_value >= 85:
            return "High"
        elif risk_value >= 45:
            return "Medium"
        return "Low"

    enriched_dataset["risk_level"] = enriched_dataset.apply(assign_risk_level, axis=1)

    relationship_network = construct_relationship_graph(enriched_dataset)

    print("\nSAMPLE PROCESSED DATA")
    print(enriched_dataset.head())

    print("\nDUPLICATE ENTRIES")
    print(duplicates_found)

    print("\nSYSTEM EXECUTION COMPLETED")


if __name__ == "__main__":
    execute_fraud_detection_system()