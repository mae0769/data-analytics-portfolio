# Reproducible synthetic analytical workflow

This project is an **independent synthetic reconstruction of the analytical workflow** used in the portfolio case study. The business-question structure and analytical reasoning are analogous; the datasets, records and numerical results are independently generated.

## Pipeline

**Business requirements → synthetic data generation → data preparation → modelling/analysis → evaluation → limitations → decision-support interpretation**

### 1. Production-risk visibility

Synthetic machine-condition records are used to demonstrate Decision Tree classification. The evaluation includes accuracy, failure recall and a confusion matrix. Recall is important because a missed failure may matter more operationally than an overall accuracy figure.

### 2. Demand anticipation

Synthetic SKU/month planning records are used to demonstrate Random Forest regression. The model is evaluated against an existing synthetic forecast using MAE, RMSE, R² and MAPE. Because the existing forecast is itself an input, the model is interpreted as a **model-based challenge/correction signal**, not an independent forecast.

The synthetic generator creates temporal observations, but the demonstration is not evidence of production forecasting readiness. Predictor timing and availability would need to be validated in a real operating environment.

### 3. Resource prioritisation

Synthetic product-group data is used to calculate demand–supply gaps and a transparent pressure score combining shortage and service-risk indicators. The demonstration uses equal weighting across the components; those weights are **illustrative rather than empirically calibrated or business-validated**. Groups are ranked into relative priority tiers using quantile bands. These tiers are demonstration thresholds, not validated operational thresholds. This is decision-support prioritisation, not an optimisation model and does not determine actual production allocation.

## Why synthetic data?

The portfolio needs to demonstrate analytical competence without publishing third-party datasets, cleaned copies, row-level outputs or assessment material. The datasets are therefore generated independently from explicit assumptions.

The numerical results are **not engineered to match the academic results**. They are produced by running the models against the synthetic data. This preserves a meaningful distinction between demonstrating the analytical method and reproducing the original submission.

## Validity boundary

The synthetic results demonstrate implementation and reasoning only. They do not establish performance for Vitaco or any real organisation, and they do not establish causal relationships.
