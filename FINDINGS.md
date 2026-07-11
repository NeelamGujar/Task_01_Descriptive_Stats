# Findings: 2024 Facebook Political Advertising Dataset

## Dataset Overview

This analysis examined 246,745 Facebook political advertising records with 40 columns. Each row represents an individual ad associated with the 2024 United States presidential election. The dataset includes information about the page running the ad, ad timing, estimated audience size, impressions, spending ranges, publisher platforms, candidate mentions, message types, political topics, and indicators such as incivility and election-integrity content.

The dataset was generally complete. Only three columns contained missing values:

- `ad_delivery_stop_time`: 2,159 missing values, approximately 0.87%
- `bylines`: 1,009 missing values, approximately 0.41%
- `estimated_audience_size`: 579 missing values, approximately 0.23%

All other columns had complete values.

## Concentration of Advertising Activity

Advertising activity was concentrated among a relatively small number of major political pages.

The page with the highest number of ads was Kamala Harris, with 55,503 records, representing 22.49% of the dataset. Donald J. Trump followed with 23,988 ads, or 9.72%, while Joe Biden accounted for 14,822 ads, or 6.01%.

The top five pages were:

1. Kamala Harris — 55,503 ads
2. Donald J. Trump — 23,988 ads
3. Joe Biden — 14,822 ads
4. The Daily Scroll — 10,461 ads
5. Kamala HQ — 7,564 ads

This indicates that ad volume was not evenly distributed. A few major campaign and political pages were responsible for a substantial portion of the activity.

The byline results showed a similar pattern. The most frequent sponsor was `HARRIS FOR PRESIDENT`, followed by `HARRIS VICTORY FUND`, `BIDEN VICTORY FUND`, and `DONALD J. TRUMP FOR PRESIDENT 2024, INC.`

These results suggest that official campaign organizations and large fundraising committees played a dominant role in the dataset.

## Timing of Political Advertising

The most common ad creation dates were concentrated near the end of October 2024.

The highest-volume creation dates were:

- October 27, 2024 — 8,619 ads
- October 28, 2024 — 7,356 ads
- October 26, 2024 — 6,414 ads
- October 23, 2024 — 5,021 ads
- October 25, 2024 — 4,769 ads

The most common ad delivery start date was October 28, 2024, with 10,089 ads beginning on that date.

The most common stop date was November 5, 2024, with 14,222 ads ending on Election Day.

This timing pattern indicates a strong increase in political advertising activity during the final days of the election campaign. The concentration of creation, start, and stop dates in late October and early November is consistent with campaigns intensifying digital outreach immediately before voting.

## Spending and Audience Patterns

The `spend`, `impressions`, and `estimated_audience_size` columns were stored as ranges rather than exact numeric values.

The most common spending range was:

- `$0–$99`: 135,950 ads, or 55.10%

Other common ranges included:

- `$100–$199`: 24,593 ads
- `$200–$299`: 13,797 ads
- `$300–$399`: 9,095 ads
- `$1,000–$1,499`: 8,911 ads

This shows that most ads were relatively low-cost individual purchases. However, the dataset does not directly reveal total spending by organization because spend is stored as a range instead of a single value.

For impressions, the most common range was:

- `0–999 impressions`: 80,822 ads, or 32.76%

For estimated audience size, the largest category was:

- More than 1,000,001 people: 100,146 ads, or 40.68%

This combination suggests that many ads had broad potential targeting ranges, even when their observed impression counts or spending levels were relatively low.

## Candidate Mentions

The `illuminating_mentions` column contained recognized candidate names stored as list-like strings.

The most common value was an empty list:

- No recognized candidate mention: 73,205 ads, or 29.67%

The most common individual candidate mentions were:

- Donald Trump — 53,182 ads, or 21.55%
- Kamala Harris — 31,019 ads, or 12.57%
- President Trump — 14,580 ads, or 5.91%
- Joe Biden — 14,059 ads, or 5.70%

Because `Donald Trump` and `President Trump` appear as separate values, the raw frequency results understate the combined number of Trump-related mentions. This is an important normalization issue for future analysis.

## Publisher Platforms

The dominant delivery combination was Facebook and Instagram together.

The most common publisher-platform values were:

- Facebook and Instagram — 214,434 ads, or 86.91%
- Facebook only — 23,259 ads, or 9.43%
- Instagram only — 8,395 ads, or 3.40%

This indicates that most political advertisers used Meta’s platforms together rather than relying on a single channel.

## Message Types and Political Topics

The binary indicator columns show the proportion of ads associated with each message type or topic.

The most common message characteristics were:

- Call-to-action content — 57.28%
- Advocacy content — 54.86%
- Issue-focused content — 38.16%
- Attack messaging — 27.19%
- Image-focused messaging — 22.27%
- Incivility — 18.75%

Among call-to-action subtypes:

- Fundraising — 22.85%
- Voting — 14.38%
- Engagement — 12.49%

The most common political topics were:

- Economy — 12.21%
- Health — 10.92%
- Social and cultural issues — 10.58%
- Women’s issues — 8.09%
- Safety — 3.37%
- Immigration — 3.36%

The economy was the most frequently identified topic. Health and social or cultural issues were also prominent.

The least frequent topics included:

- Technology and privacy — 0.12%
- Military — 0.22%
- LGBTQ issues — 0.32%
- Foreign policy — 0.53%

These results suggest that campaign messaging focused more heavily on economic and domestic social issues than on technology, military policy, or foreign affairs.

## Data Quality Observations

Several data-quality issues were identified.

First, `spend`, `impressions`, and `estimated_audience_size` were stored as structured range strings rather than exact numeric values. This limits direct statistical calculations unless the ranges are transformed into lower bounds, upper bounds, or estimated midpoints.

Second, `illuminating_scored_message` contained some hashes in both uppercase and lowercase forms. These values may represent the same underlying message but were counted separately because the raw text was not normalized.

Third, candidate mentions were not fully standardized. For example, `Donald Trump` and `President Trump` appeared as separate categories.

Fourth, `ad_id` was unique for all 246,745 rows. Although technically categorical, it functions as a record identifier rather than a meaningful analytical category.

Finally, some columns contained list-like strings, such as publisher platforms and candidate mentions. Future analysis would benefit from parsing these strings into actual lists before aggregation.

## Key Takeaways

The dataset shows that Facebook political advertising activity was highly concentrated among major campaign pages and official political organizations. Activity increased sharply in late October and many ads ended on Election Day.

Most individual ads fell into the lowest spending range, while many targeted very large potential audiences. Facebook and Instagram were overwhelmingly used together.

In terms of content, advocacy and call-to-action messaging were the most common formats. The economy, health, and social or cultural issues were the most prominent topics.

The analysis also revealed important data-cleaning challenges, particularly range-based numeric fields, inconsistent candidate naming, mixed text casing, and list-like strings. These issues would need to be addressed before performing more advanced spending, audience, or cross-candidate comparisons.