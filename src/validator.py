REQUIRED_COLUMNS = [
    "Employee ID",
    "Employee Name",
    "Department",
    "Sales"
]

def validate_dataframe(df):
    """
    Validates whether all required columns exist.
    """

    missing_columns = []

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return True
