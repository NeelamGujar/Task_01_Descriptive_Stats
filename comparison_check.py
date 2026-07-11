"""
Research Task 01
Comparison of Pure Python and Pandas Numeric Statistics

This script verifies that both analytical approaches produce
equivalent numeric results.
"""

import math
from pathlib import Path

import pandas as pd

from pure_python_stats import (
    analyze_numeric_columns,
    infer_all_column_types,
    load_csv,
)


DATA_FILE = Path("Data/facebook_political_ads_2024.csv")

METRICS = [
    "count",
    "mean",
    "minimum",
    "maximum",
    "standard_deviation",
    "median",
]


def get_pandas_numeric_stats(df):
    """Compute numeric statistics using Pandas."""

    results = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        series = df[column]

        results[column] = {
            "count": int(series.count()),
            "mean": float(series.mean()),
            "minimum": float(series.min()),
            "maximum": float(series.max()),
            "standard_deviation": float(series.std(ddof=1)),
            "median": float(series.median()),
        }

    return results


def values_match(value_one, value_two, tolerance=1e-9):
    """Compare numeric values with a small floating-point tolerance."""

    if value_one is None and value_two is None:
        return True

    if value_one is None or value_two is None:
        return False

    return math.isclose(
        float(value_one),
        float(value_two),
        rel_tol=tolerance,
        abs_tol=tolerance,
    )


def compare_results(pure_python_results, pandas_results):
    """Compare statistics from both implementations."""

    all_match = True

    print("=" * 120)
    print("PURE PYTHON VS. PANDAS NUMERIC COMPARISON")
    print("=" * 120)

    print(
        f"{'Column':45}"
        f"{'Metric':>22}"
        f"{'Pure Python':>18}"
        f"{'Pandas':>18}"
        f"{'Match':>10}"
    )

    print("-" * 120)

    shared_columns = sorted(
        set(pure_python_results) & set(pandas_results)
    )

    for column in shared_columns:
        for metric in METRICS:
            pure_value = pure_python_results[column][metric]
            pandas_value = pandas_results[column][metric]

            match = values_match(pure_value, pandas_value)

            if not match:
                all_match = False

            pure_display = (
                f"{pure_value:.10f}"
                if isinstance(pure_value, float)
                else str(pure_value)
            )

            pandas_display = (
                f"{pandas_value:.10f}"
                if isinstance(pandas_value, float)
                else str(pandas_value)
            )

            print(
                f"{column:45}"
                f"{metric:>22}"
                f"{pure_display:>18}"
                f"{pandas_display:>18}"
                f"{'YES' if match else 'NO':>10}"
            )

    pure_only = set(pure_python_results) - set(pandas_results)
    pandas_only = set(pandas_results) - set(pure_python_results)

    if pure_only:
        all_match = False
        print("\nColumns detected only by Pure Python:")
        for column in sorted(pure_only):
            print(f"- {column}")

    if pandas_only:
        all_match = False
        print("\nColumns detected only by Pandas:")
        for column in sorted(pandas_only):
            print(f"- {column}")

    print("\n" + "=" * 120)

    if all_match:
        print("RESULT: All numeric statistics match.")
    else:
        print("RESULT: Some differences were detected. Review the rows marked NO.")

    print("=" * 120)


def main():
    """Run the numerical comparison."""

    rows, columns = load_csv(DATA_FILE)

    column_types = infer_all_column_types(
        rows=rows,
        columns=columns,
    )

    pure_python_results = analyze_numeric_columns(
        rows=rows,
        columns=columns,
        column_types=column_types,
    )

    df = pd.read_csv(DATA_FILE)

    pandas_results = get_pandas_numeric_stats(df)

    compare_results(
        pure_python_results=pure_python_results,
        pandas_results=pandas_results,
    )


if __name__ == "__main__":
    main()