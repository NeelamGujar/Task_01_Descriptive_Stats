# Comparison of Pure Python and Pandas Approaches

## Overview

This project analyzed the same Facebook political advertising dataset using two independent approaches:

1. Pure Python using only the standard library
2. Pandas using DataFrame-based methods

The goal was to verify that both approaches produced the same descriptive statistics while also comparing the amount of work, transparency, and flexibility involved in each method.

## Agreement Between Results

The numeric statistics produced by the Pure Python and Pandas scripts matched for all numeric columns.

The following measures were compared:

- Count
- Mean
- Minimum
- Maximum
- Standard deviation
- Median

The comparison script confirmed that all calculated values matched within a small floating-point tolerance.

Both approaches also reported the same dataset dimensions:

- 246,745 rows
- 40 columns

The missing-value counts also matched:

- `ad_delivery_stop_time`: 2,159 missing values
- `bylines`: 1,009 missing values
- `estimated_audience_size`: 579 missing values

All other columns contained no missing values.

## Pure Python Approach

The Pure Python implementation required more manual work.

I had to explicitly:

- Load the CSV using `csv.DictReader`
- Define which values should be considered missing
- Detect numeric, categorical, and date columns
- Convert numeric-looking values into floats
- Calculate the mean manually
- Sort values to calculate the median
- Calculate sample standard deviation using the `n - 1` formula
- Count categorical frequencies using `collections.Counter`
- Handle empty columns and invalid values
- Format the output manually

This approach made the logic behind each statistic very clear. It also required careful decisions about edge cases, including mixed data types, missing values, invalid numeric strings, and columns containing structured text.

The main disadvantage was that the code was longer and more time-consuming to write and test.

## Pandas Approach

The Pandas implementation was shorter and easier to develop.

Pandas automatically handled many operations, including:

- Reading the CSV
- Inferring data types
- Counting missing values
- Computing means, medians, minimums, maximums, and standard deviations
- Counting unique values
- Calculating frequency distributions
- Generating summary statistics with `DataFrame.describe()`

The Pandas implementation required fewer lines of code and was easier to read for common analytical tasks.

However, Pandas made some decisions silently. For example, it automatically inferred column types and excluded missing values from many calculations. Without first implementing the Pure Python version, it would have been easier to overlook these behaviors.

## Differences in Type Inference

The dataset contains several columns that appear numeric in meaning but are stored as structured strings.

Examples include:

- `spend`
- `impressions`
- `estimated_audience_size`

A typical value looks like:

```text
{'lower_bound': '200', 'upper_bound': '299'}
```

Because these fields are stored as range-based strings rather than single numeric values, they were treated as categorical columns in the raw descriptive analysis. Converting them into numeric values would require an additional assumption, such as using the lower bound, upper bound, or midpoint. To keep the comparison faithful to the original dataset, no such transformation was applied in Task 01.

## Verification Method

To verify consistency, I created a separate comparison script that calculated the same numeric metrics using both implementations and compared the results using a small floating-point tolerance.

The comparison confirmed that all numeric statistics matched across the Pure Python and Pandas approaches.


## Data Quality Observations

The analysis identified several data-quality considerations:

- Some fields contained missing values, especially `ad_delivery_stop_time`, `bylines`, and `estimated_audience_size`.
- `spend`, `impressions`, and `estimated_audience_size` were stored as range-based structured strings rather than direct numeric values.
- `illuminating_scored_message` included hashes with inconsistent uppercase and lowercase formatting.
- `ad_id` was unique for every row, so its mode frequency was one and was not analytically meaningful.
- Some categorical columns contained list-like strings, such as candidate mentions and publisher platforms.