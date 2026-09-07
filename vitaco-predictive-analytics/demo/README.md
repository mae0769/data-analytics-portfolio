# Independent synthetic analytics demonstrations

This directory contains an **independently generated synthetic reconstruction of the analytical workflow** described in the portfolio case study. It demonstrates the methods and decision logic without publishing third-party or assessment data.

The synthetic datasets are generated from scratch for this portfolio. They are not copied, sampled, transformed, extracted, or otherwise derived from the academic source datasets. They are **not Vitaco data** and must not be interpreted as representing Vitaco operations or performance.

## Demonstrations

- `01_machine_failure/decision_tree_demo.py` — classification of synthetic machine-condition records using a Decision Tree.
- `02_demand_forecasting/random_forest.py` — Random Forest demand modelling and comparison with an existing synthetic forecast.
- `03_resource_prioritisation/allocation_analysis.py` — analytical ranking of synthetic allocation pressure.
- `generate_synthetic_data.py` — independently generates all three datasets.
- `WORKFLOW.md` — explains the end-to-end analytical reasoning.
- `requirements.txt` — Python dependencies.

Generated CSV files are intentionally **not committed**. They are recreated locally by the generator using seed 42.

## Reproducibility

From this directory:

```bash
pip install -r requirements.txt
python generate_synthetic_data.py
python 01_machine_failure/decision_tree_demo.py
python 02_demand_forecasting/random_forest.py
python 03_resource_prioritisation/allocation_analysis.py
```

Each demonstration produces its own results from the synthetic data. Numerical results are not copied from the academic case study and are not expected to match it.

## What this demonstrates

The purpose is not to reproduce an academic result. It is to demonstrate the ability to move from **business requirement → data structure → analytical technique → evaluation → interpretation → decision-support implication**.

The demonstrations deliberately preserve the analytical problem structure while using different data-generating assumptions and independently obtained results.

## Publication boundary

No original source rows, values, extracts, cleaned copies, or row-level academic outputs are used. The synthetic data exists specifically to demonstrate analytical competence without redistributing third-party or assessment data.
