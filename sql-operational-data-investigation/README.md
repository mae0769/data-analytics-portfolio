# Operational Data Investigation & Performance Analysis

*SQL-based business analysis · Independent synthetic demonstration*

## Business question

A fictional distribution business wants to understand where order-fulfilment delays are concentrated and which operational areas warrant further investigation.

The analysis asks:

1. Where are fulfilment delays concentrated?
2. Which warehouses and product categories have the greatest operational exposure?
3. Has fulfilment performance changed over time?
4. Which areas should management investigate first?

## Analytical approach

The project uses a small relational data model and analytical SQL to move from raw operational records to management-focused findings.

**Business question → data quality → SQL investigation → comparative evidence → decision focus**

The project deliberately distinguishes association from causation. A high delay rate identifies an area for investigation; it does not establish that the area causes the delay.

## Data model

```text
customers
    |
    +---- orders ---- order_items ---- products
              |
              +---- fulfilments ---- warehouses
```

All records are independently generated synthetic data. They are not copied, sampled, transformed, extracted, or derived from a real company's data or from a university dataset.

## SQL capabilities demonstrated

- filtering and aggregation
- joins across relational tables
- `CASE` logic
- common table expressions (CTEs)
- date-based analysis
- data-quality validation
- window functions such as `LAG()` and `AVG() OVER()`
- ranking and comparative analysis

## Data-quality controls

Before interpreting results, the project checks for issues such as:

- duplicate order identifiers
- orders without fulfilments
- missing warehouse assignments
- fulfilment dates before order dates
- shipments after promised dates
- invalid quantities

The objective is to demonstrate that analytical querying begins with establishing whether the underlying records are fit for the question being asked.

## Decision boundary

The output is an **investigation-prioritisation analysis**, not an operational optimisation model. It does not determine staffing levels, warehouse capacity, inventory policy, or root cause automatically.

Findings from synthetic data are illustrative only and must not be interpreted as evidence about a real organisation.

## Repository structure

- `schema/schema.sql` — SQLite-compatible table definitions
- `demo/generate_synthetic_data.py` — reproducible synthetic data generator
- `sql/01_data_quality_checks.sql` — validation queries
- `sql/02_operational_performance.sql` — baseline performance measures
- `sql/03_delay_analysis.sql` — warehouse and category investigation
- `sql/04_monthly_trends.sql` — time-series analysis using window functions
- `sql/05_management_summary.sql` — consolidated investigation view
- `analysis/findings.md` — interpretation framework and decision implications

## Reproducibility

The demonstration uses synthetic data generated with a fixed random seed. Generated CSV/database files are intentionally not committed to the repository; they can be recreated locally.

## Publication boundary

This project is an independently written portfolio demonstration. It does not reproduce a university assessment, confidential business material, third-party dataset, or proprietary operational data.