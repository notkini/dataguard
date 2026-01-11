# DataGuard

DataGuard is a lightweight Python package for dataset quality validation with both API and CLI support.  
It focuses on catching **silent data issues** that often pass basic checks.

---

## Features

- Missing value detection
- Duplicate row detection
- Optional target column analysis
- Silent signal loss detection (variance and entropy collapse)
- Automatic column role inference (identifier, numeric, categorical, text)
- JSON report export
- Command line interface

---

## Installation

```bash
pip install dataguard-lite

For local development:

pip install -e .

Usage (Python API)

from dataguard import validate_csv

report = validate_csv(
    "data.csv",
    target="label",
    signal=True,
    roles=True
)

report.summary()
report.to_json("report.json")

Usage (CLI)

Basic validation:

dataguard data.csv

With target column:

dataguard data.csv --target label

Detect silent signal loss:

dataguard data.csv --signal

Infer column roles:

dataguard data.csv --roles

Why DataGuard?

Most data quality tools focus on schema and missing values.
DataGuard goes further by detecting information collapse and column intent, helping catch failures that silently break downstream analysis and models.
