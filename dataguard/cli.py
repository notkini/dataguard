import argparse
from .core import validate_csv


def main():
    parser = argparse.ArgumentParser(description="DataGuard dataset validator")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--target", help="Target column name", default=None)
    parser.add_argument("--json", help="Save report as JSON file", default=None)

    args = parser.parse_args()

    report = validate_csv(args.csv, target=args.target)
    report.summary()

    if args.json:
        report.to_json(args.json)
        print(f"Report saved to {args.json}")
