# Synthetic Decision Tree demonstration

This directory contains a **fully synthetic** demonstration of the analytical workflow described in the portfolio case study.

The synthetic dataset is generated independently for this portfolio. It is not copied, sampled, transformed, extracted, or otherwise derived from the academic source datasets.

It is **not Vitaco data** and must not be interpreted as representing Vitaco operations, equipment, failure rates, or performance.

## Contents

- `generate_synthetic_data.py` — independently generates the synthetic dataset.
- `decision_tree_demo.py` — trains and evaluates a Decision Tree using the generated synthetic data.
- `WORKFLOW.md` — documents the reproducible analytical workflow.
- `requirements.txt` — Python dependencies for the demonstration.

The generated CSV is intentionally not committed; it can be recreated deterministically from the generator using seed 42.

## Reproducibility

From this directory, run:

```bash
pip install -r requirements.txt
python generate_synthetic_data.py
python decision_tree_demo.py
```

The model produces its **own** accuracy, failure recall and confusion matrix from the synthetic data. Those results are separate from the academic case study results reported in the parent portfolio page.

## Publication boundary

No original source rows, values, extracts, cleaned copies, or row-level academic outputs are used in this demonstration. The synthetic data exists specifically to demonstrate the analytical method without redistributing third-party or assessment data.
