# DataGuard

DataGuard is a lightweight Python package for basic dataset quality checks.

## Installation (local)

```bash
pip install -e .

Usage

from dataguard import validate_csv

report = validate_csv("data.csv")
report.summary()

License
 
MIT


---

## Why this was missing

README files do not auto generate sections.

You already wrote:
- Title
- Description
- Installation

Usage is always written explicitly by the developer.

You did nothing wrong.

---

## Quick sanity test to confirm usage works

After adding the section, run this in Python:

```python
from dataguard import validate_csv
report = validate_csv("yourfile.csv")
report.summary()
