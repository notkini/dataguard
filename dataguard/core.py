import pandas as pd
from .checks import basic_checks
from .report import ValidationReport


def validate_csv(path: str) -> ValidationReport:
    """
    Validate a CSV file and return a validation report.
    """
    df = pd.read_csv(path)

    results = basic_checks(df)

    return ValidationReport(results)
