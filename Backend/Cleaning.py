import pandas as pd
from pathlib import Path


def load_dataset():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir.parent / "data" / "scheme_data.csv"
    
    data = pd.read_csv(file_path)
    return data



def preprocess_data(dataframe):
    df = dataframe.copy()

    # Remove exact duplicate rows
    df = df.drop_duplicates(keep="first")

    # Handle missing values
    df = df.dropna(how="any")

    # Reset index after cleaning
    df.reset_index(drop=True, inplace=True)

    return df