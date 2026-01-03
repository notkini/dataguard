class ValidationReport:
    def __init__(self, results: dict):
        self.results = results

    def summary(self):
        print("DataGuard Validation Summary")
        print("-" * 30)
        print(f"Rows: {self.results['rows']}")
        print(f"Columns: {self.results['columns']}")
        print(f"Duplicate rows: {self.results['duplicate_rows']}")
        print("Missing values per column:")
        for col, count in self.results["missing_values"].items():
            print(f"  {col}: {count}")

    def to_dict(self) -> dict:
        return self.results
