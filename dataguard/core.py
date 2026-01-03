import pandas as pd
from .checks import basic_checks
from .report import ValidationReport


def validate_csv(path: str, target: str | None = None) -> ValidationReport:
    df = pd.read_csv(path)
    results = basic_checks(df, target=target)
    return ValidationReport(results)
