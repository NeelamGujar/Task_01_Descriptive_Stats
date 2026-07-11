# Task 01: Descriptive Statistics with Pure Python and Pandas

## Project Overview

This project analyzes a real-world Facebook political advertising dataset related to the 2024 United States presidential election.

The analysis was completed using two independent approaches:

1. Pure Python using only the standard library
2. Pandas using DataFrame-based analysis

The purpose of this project is to compare manual statistical calculations with library-based analysis and verify that both approaches produce consistent results.

## Dataset Overview

The dataset contains:

- 246,745 rows
- 40 columns
- Facebook political advertisements related to the 2024 U.S. presidential election

The dataset includes information about:

- Political pages and advertisers
- Ad creation and delivery dates
- Spending ranges
- Impression ranges
- Estimated audience sizes
- Publisher platforms
- Candidate mentions
- Message types
- Political topics
- Incivility and election-integrity indicators

## Repository Structure

```text
Task_01_Descriptive_Stats/
│
├── Data/
│   └── facebook_political_ads_2024.csv
│
├── Output/
│   ├── pure_python_output.txt
│   ├── pandas_output.txt
│   └── comparison_output.txt
│
├── pure_python_stats.py
├── pandas_stats.py
├── comparison_check.py
├── FINDINGS.md
├── COMPARISON.md
├── requirements.txt
├── .gitignore
└── README.md
```

The dataset file is stored locally but is not included in the public GitHub repository.

## Analysis Performed

### Pure Python Analysis

The `pure_python_stats.py` script uses only Python's standard library.

It calculates:

- Total row count
- Total column count
- Missing values by column
- Inferred data types
- Numeric count
- Mean
- Minimum
- Maximum
- Sample standard deviation
- Median
- Categorical non-null count
- Unique-value count
- Mode
- Mode frequency
- Top five values by frequency

### Pandas Analysis

The `pandas_stats.py` script performs the equivalent analysis using Pandas.

It includes:

- Dataset shape
- Data types
- `DataFrame.info()`
- Missing-value counts and percentages
- `DataFrame.describe()` for numeric and non-numeric columns
- Numeric descriptive statistics
- Unique-value counts
- Modes
- Frequency distributions

### Comparison Check

The `comparison_check.py` script compares the numeric results produced by Pure Python and Pandas.

The comparison verifies:

- Count
- Mean
- Minimum
- Maximum
- Sample standard deviation
- Median

All numeric results matched within a small floating-point tolerance.

## Setup Instructions

### 1. Clone the repository

```bash
git clone                                                   YOUR_REPOSITORY_URL
cd Task_01_Descriptive_Stats
```

### 2. Create a virtual environment

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Dataset Setup

The dataset is not included in this repository.

Download the 2024 Facebook Political Ads dataset from the Google Drive link provided in the official research-task instructions.

Place the downloaded CSV file in:

```text
Data/facebook_political_ads_2024.csv
```

## Running the Analysis

### Run the Pure Python analysis

```bash
python pure_python_stats.py
```

### Run the Pandas analysis

```bash
python pandas_stats.py
```

### Run the comparison check

```bash
python comparison_check.py
```

## Saving the Outputs

```bash
python pure_python_stats.py > Output/pure_python_output.txt
python pandas_stats.py > Output/pandas_output.txt
python comparison_check.py > Output/comparison_output.txt
```

## Key Findings

The dataset showed that political advertising activity was concentrated among a relatively small number of major campaign pages and political organizations.

Key observations included:

- Kamala Harris was the page with the highest number of ads.
- Donald J. Trump and Joe Biden were also among the most active pages.
- Ad activity increased significantly during the final days of October 2024.
- November 5, 2024, was the most common ad-delivery stop date.
- The most common spending range was $0–$99.
- Facebook and Instagram together were used for most ads.
- Advocacy and call-to-action messaging were the most common message types.
- The economy, health, and social or cultural issues were among the most common topics.

See [FINDINGS.md](FINDINGS.md) for the complete written analysis.

## Pure Python vs. Pandas

The Pure Python version required manual implementation of:

- Missing-value detection
- Type inference
- Numeric conversion
- Mean
- Median
- Standard deviation
- Frequency counting
- Output formatting

The Pandas version was shorter and more concise, but it handled several decisions automatically.

See [COMPARISON.md](COMPARISON.md) for the full comparison.

## Data Quality Considerations

The analysis identified several important data-quality issues:

- Missing values in selected columns
- Spend, impression, and audience values stored as ranges
- Inconsistent uppercase and lowercase hash values
- Candidate names stored in inconsistent formats
- List-like values stored as strings
- Unique identifiers that are not analytically meaningful categories

## Requirements

- Python 3.12 or compatible version
- Pandas

## Author

Neelam Gujar