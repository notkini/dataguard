import json


class ValidationReport:
    def __init__(self, results: dict):
        self.results = results

    def summary(self):
        print("DataGuard Validation Summary")
        print("-" * 30)
        for key, value in self.results.items():
            print(f"{key}: {value}")

    def to_dict(self) -> dict:
        return self.results

    def to_json(self, path: str):
        with open(path, "w") as f:
            json.dump(self.results, f, indent=2)
