import pandas as pd

def clean_data(df):
    """
    Cleans the input dataframe by:
    - Removing duplicate rows
    - Filling missing Sales values
    - Standardizing column names
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Fill missing Sales values with 0
    if "Sales" in df.columns:
        df["Sales"] = df["Sales"].fillna(0)

    # Remove leading/trailing spaces from text columns
    for col in ["Employee Name", "Department"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    return df
