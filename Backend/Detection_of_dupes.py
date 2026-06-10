def detect_duplicate_records(dataframe):
    """
    Identifies repeated beneficiary entries based on identity attributes.
    """

    key_columns = ["name", "age", "location"]

    duplicate_mask = dataframe.duplicated(subset=key_columns, keep=False)

    duplicates_df = dataframe.loc[duplicate_mask].copy()

    return duplicates_df