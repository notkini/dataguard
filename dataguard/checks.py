import pandas as pd


def basic_checks(df: pd.DataFrame) -> dict:
    """
    Run basic data quality checks.
    """
    missing_values = df.isnull().sum().to_dict()
    duplicate_rows = int(df.duplicated().sum())
    total_rows = int(len(df))
    total_columns = int(len(df.columns))

    return {
        "rows": total_rows,
        "columns": total_columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows
    }
