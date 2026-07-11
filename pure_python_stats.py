"""
Research Task 01
Descriptive Statistics Using Pure Python

This script loads and analyzes the Facebook political ads dataset
using only Python's standard library.

No Pandas or NumPy are used in this file.
"""

import csv
import math
from collections import Counter
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("Data/facebook_political_ads_2024.csv")

MISSING_VALUES = {
    "",
    "na",
    "n/a",
    "null",
    "none",
    "nan",
    "missing",
}


def is_missing(value):
    """Return True when a value should be treated as missing."""

    if value is None:
        return True

    cleaned_value = str(value).strip().lower()
    return cleaned_value in MISSING_VALUES


def load_csv(file_path):
    """Load a CSV file using csv.DictReader."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found.\nExpected location: {file_path.resolve()}"
        )

    rows = []

    with file_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError("The CSV file does not contain column headers.")

        columns = reader.fieldnames

        for row in reader:
            rows.append(row)

    return rows, columns


def count_missing_values(rows, columns):
    """Count missing values for every column."""

    missing_counts = {column: 0 for column in columns}

    for row in rows:
        for column in columns:
            if is_missing(row.get(column)):
                missing_counts[column] += 1

    return missing_counts


def can_convert_to_number(value):
    """
    Return True when a value can be safely converted to a float.

    Examples accepted:
    10
    -2
    3.14
    $1,250.50
    """

    if is_missing(value):
        return False

    cleaned_value = str(value).strip()

    cleaned_value = cleaned_value.replace("$", "")
    cleaned_value = cleaned_value.replace(",", "")
    cleaned_value = cleaned_value.replace("%", "")

    try:
        float(cleaned_value)
        return True
    except ValueError:
        return False


def clean_numeric_value(value):
    """
    Convert a numeric-looking value into a float.

    Handles commas, dollar signs, and percentage signs.

    Returns None when the value is missing or cannot be converted.
    """

    if is_missing(value):
        return None

    cleaned_value = str(value).strip()

    cleaned_value = cleaned_value.replace("$", "")
    cleaned_value = cleaned_value.replace(",", "")
    cleaned_value = cleaned_value.replace("%", "")

    try:
        return float(cleaned_value)
    except ValueError:
        return None


def compute_numeric_stats(values):
    """
    Compute descriptive statistics for a numeric column.

    The standard deviation uses the sample formula with n - 1,
    matching Pandas Series.std() default behavior.

    Parameters
    ----------
    values : list
        Raw values from one numeric column.

    Returns
    -------
    dict
        Count, mean, minimum, maximum, standard deviation, and median.
    """

    numeric_values = []

    for value in values:
        numeric_value = clean_numeric_value(value)

        if numeric_value is not None:
            numeric_values.append(numeric_value)

    count = len(numeric_values)

    if count == 0:
        return {
            "count": 0,
            "mean": None,
            "minimum": None,
            "maximum": None,
            "standard_deviation": None,
            "median": None,
        }

    total = sum(numeric_values)
    mean = total / count
    minimum = min(numeric_values)
    maximum = max(numeric_values)

    sorted_values = sorted(numeric_values)

    middle_index = count // 2

    if count % 2 == 1:
        median = sorted_values[middle_index]
    else:
        lower_middle = sorted_values[middle_index - 1]
        upper_middle = sorted_values[middle_index]
        median = (lower_middle + upper_middle) / 2

    if count > 1:
        squared_differences = []

        for value in numeric_values:
            difference = value - mean
            squared_differences.append(difference ** 2)

        variance = sum(squared_differences) / (count - 1)
        standard_deviation = math.sqrt(variance)
    else:
        standard_deviation = None

    return {
        "count": count,
        "mean": mean,
        "minimum": minimum,
        "maximum": maximum,
        "standard_deviation": standard_deviation,
        "median": median,
    }


def compute_categorical_stats(values):
    """
    Compute descriptive statistics for a non-numeric column.

    Missing values are excluded from the calculations.

    Returns
    -------
    dict
        Non-null count, number of unique values, mode,
        mode frequency, and top five values.
    """

    cleaned_values = []

    for value in values:
        if not is_missing(value):
            cleaned_values.append(str(value).strip())

    count = len(cleaned_values)

    if count == 0:
        return {
            "count": 0,
            "unique_count": 0,
            "mode": None,
            "mode_frequency": 0,
            "top_five": [],
        }

    frequency_counts = Counter(cleaned_values)

    top_five = frequency_counts.most_common(5)

    mode, mode_frequency = top_five[0]

    return {
        "count": count,
        "unique_count": len(frequency_counts),
        "mode": mode,
        "mode_frequency": mode_frequency,
        "top_five": top_five,
    }


def analyze_numeric_columns(rows, columns, column_types):
    """
    Compute statistics for every column inferred as numeric.
    """

    numeric_results = {}

    for column in columns:
        if column_types[column] != "numeric":
            continue

        values = [row.get(column) for row in rows]

        numeric_results[column] = compute_numeric_stats(values)

    return numeric_results


def analyze_categorical_columns(rows, columns, column_types):
    """
    Compute statistics for categorical and date columns.

    Empty columns are also included so they can be reported safely.
    """

    categorical_results = {}

    for column in columns:
        if column_types[column] == "numeric":
            continue

        values = [row.get(column) for row in rows]

        categorical_results[column] = compute_categorical_stats(values)

    return categorical_results


def can_convert_to_date(value):
    """
    Return True when a value matches one of the supported date formats.
    """

    if is_missing(value):
        return False

    cleaned_value = str(value).strip()

    supported_formats = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%m/%d/%Y",
        "%m/%d/%Y %H:%M:%S",
    ]

    for date_format in supported_formats:
        try:
            datetime.strptime(cleaned_value, date_format)
            return True
        except ValueError:
            continue

    return False


def infer_column_type(values, threshold=0.95):
    """
    Infer whether a column is numeric, date, categorical, or empty.

    At least 95% of the non-missing values must match a type before
    the column is classified as that type.
    """

    non_missing_values = [
        value for value in values
        if not is_missing(value)
    ]

    if not non_missing_values:
        return "empty"

    numeric_count = sum(
        can_convert_to_number(value)
        for value in non_missing_values
    )

    numeric_ratio = numeric_count / len(non_missing_values)

    if numeric_ratio >= threshold:
        return "numeric"

    date_count = sum(
        can_convert_to_date(value)
        for value in non_missing_values
    )

    date_ratio = date_count / len(non_missing_values)

    if date_ratio >= threshold:
        return "date"

    return "categorical"


def infer_all_column_types(rows, columns):
    """Infer the type of every column in the dataset."""

    column_types = {}

    for column in columns:
        values = [row.get(column) for row in rows]
        column_types[column] = infer_column_type(values)

    return column_types


def print_missing_value_report(rows, columns, missing_counts):
    """Print missing-value counts and percentages."""

    total_rows = len(rows)

    print("\n" + "=" * 70)
    print("MISSING VALUE REPORT")
    print("=" * 70)

    print(
        f"{'Column':45}"
        f"{'Missing Count':>15}"
        f"{'Missing %':>10}"
    )

    print("-" * 70)

    for column in columns:
        missing_count = missing_counts[column]

        missing_percentage = (
            missing_count / total_rows * 100
            if total_rows > 0
            else 0.0
        )

        print(
            f"{column:45}"
            f"{missing_count:>15,}"
            f"{missing_percentage:>9.2f}%"
        )


def print_data_type_report(columns, column_types):
    """Print the inferred data type for every column."""

    print("\n" + "=" * 70)
    print("INFERRED DATA TYPES")
    print("=" * 70)

    print(f"{'Column':50}{'Inferred Type':>20}")
    print("-" * 70)

    for column in columns:
        print(f"{column:50}{column_types[column]:>20}")

def print_numeric_statistics_report(numeric_results):
    """Print descriptive statistics for all numeric columns."""

    print("\n" + "=" * 110)
    print("NUMERIC COLUMN STATISTICS")
    print("=" * 110)

    header = (
        f"{'Column':45}"
        f"{'Count':>12}"
        f"{'Mean':>10}"
        f"{'Min':>8}"
        f"{'Max':>8}"
        f"{'Std Dev':>12}"
        f"{'Median':>10}"
    )

    print(header)
    print("-" * 110)

    for column, stats in numeric_results.items():
        standard_deviation = stats["standard_deviation"]

        std_display = (
            f"{standard_deviation:.4f}"
            if standard_deviation is not None
            else "N/A"
        )

        print(
            f"{column:45}"
            f"{stats['count']:>12,}"
            f"{stats['mean']:>10.4f}"
            f"{stats['minimum']:>8.2f}"
            f"{stats['maximum']:>8.2f}"
            f"{std_display:>12}"
            f"{stats['median']:>10.2f}"
        )


def shorten_text(value, maximum_length=60):
    """
    Shorten long text values so reports remain readable.
    """

    if value is None:
        return "N/A"

    text = str(value)

    if len(text) <= maximum_length:
        return text

    return text[: maximum_length - 3] + "..."


def print_categorical_statistics_report(categorical_results):
    """
    Print descriptive statistics for all non-numeric columns.
    """

    print("\n" + "=" * 110)
    print("CATEGORICAL AND DATE COLUMN STATISTICS")
    print("=" * 110)

    for column, stats in categorical_results.items():
        print(f"\nCOLUMN: {column}")
        print("-" * 110)

        print(f"Non-null count: {stats['count']:,}")
        print(f"Unique values: {stats['unique_count']:,}")
        print(f"Mode: {shorten_text(stats['mode'])}")
        print(f"Mode frequency: {stats['mode_frequency']:,}")

        print("Top 5 values:")

        if not stats["top_five"]:
            print("  No non-missing values")
            continue

        for rank, (value, frequency) in enumerate(
            stats["top_five"],
            start=1
        ):
            percentage = (
                frequency / stats["count"] * 100
                if stats["count"] > 0
                else 0.0
            )

            print(
                f"  {rank}. {shorten_text(value)} "
                f"— {frequency:,} ({percentage:.2f}%)"
            )



def main():
    """Load the dataset and generate descriptive statistics."""

    rows, columns = load_csv(DATA_FILE)

    print("=" * 70)
    print("PURE PYTHON DATASET OVERVIEW")
    print("=" * 70)

    print(f"Dataset: {DATA_FILE.name}")
    print(f"Total rows: {len(rows):,}")
    print(f"Total columns: {len(columns):,}")

    missing_counts = count_missing_values(
        rows=rows,
        columns=columns
    )

    column_types = infer_all_column_types(
        rows=rows,
        columns=columns
    )

    numeric_results = analyze_numeric_columns(
        rows=rows,
        columns=columns,
        column_types=column_types
    )

    categorical_results = analyze_categorical_columns(
    rows=rows,
    columns=columns,
    column_types=column_types
    )

    print_missing_value_report(
        rows=rows,
        columns=columns,
        missing_counts=missing_counts
    )

    print_data_type_report(
        columns=columns,
        column_types=column_types
    )

    print_numeric_statistics_report(
        numeric_results=numeric_results
    )


    print_categorical_statistics_report(
    categorical_results=categorical_results
    )


if __name__ == "__main__":
    main()