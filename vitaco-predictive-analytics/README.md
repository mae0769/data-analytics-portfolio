# Predictive Analytics & Business Intelligence

**Vitaco-inspired academic case study · Independent synthetic demonstration**

## Publication and data-safety boundary

This portfolio case study is a curated adaptation of postgraduate academic work. It is **not a reproduction of the original assessment submission** and is not an official report, operational assessment, or publication of Vitaco Health Group.

The academic analysis examined three proposed decision requirements associated with the Vitaco case using public proxy datasets. The datasets used were **not Vitaco proprietary or internal datasets**, so the findings do not assess Vitaco's actual operational performance, systems, forecasts, inventory, production capability, or business decisions.

The accompanying demonstration code uses **independently generated synthetic data**. It is not Vitaco data and is not copied, sampled, transformed, extracted, or derived from the academic source datasets.

**Conservative publication rule:** no raw dataset, extracted dataset, cleaned dataset, generated dataset copy, row-level prediction output, or other redistribution of source data is included in this repository. Dataset redistribution is not assumed from public availability alone.

### Dataset provenance and publication boundary

The original academic case study used datasets identified on Kaggle. The Machine Downtime Analysis dataset is listed under the **Apache 2.0** licence. The Demand & Supply Planning dataset is listed as **"Other (specified in description)"**; because permission to redistribute that dataset could not be verified from the available licence information, **no copy of that dataset is included in this portfolio**. Public availability is not treated as permission to redistribute data.

---

## 1. Business problem

The case examined how Business Intelligence can turn production, demand and supply signals into earlier and more defensible management review.

Three connected decision requirements were analysed:

1. **Production-risk visibility** — identify machine-condition patterns associated with failure risk.
2. **Demand anticipation** — test whether predictive modelling can provide a model-based challenge signal for demand planning.
3. **Resource allocation** — identify product groups that warrant earlier review when demand, supply and service-risk indicators diverge.

The techniques were selected to match the decision requirement rather than for technical novelty.

| Decision requirement | Technique | Decision output |
|---|---|---|
| Production-risk visibility | Decision Tree classification | Failure-risk patterns for technical review |
| Demand anticipation | Random Forest regression + forecast comparison | Model-based challenge/correction signal |
| Resource allocation | Allocation-pressure analysis | Tiered priority for management review |

---

## 2. Production-risk visibility

A Decision Tree was developed in RapidMiner using public machine-condition and downtime indicators to classify records into machine-failure and no-machine-failure categories.

The analysed test output achieved **92.52% overall accuracy**. More importantly for a failure-detection use case, it correctly identified 328 failure cases but missed 51 actual failures, giving approximately **86.5% recall for the failure class**.

That distinction changes the interpretation of the result: the model is more appropriately positioned as an **early-warning review layer**, not an automated maintenance trigger.

The strongest tree splits involved variables including cutting force, coolant temperature, torque, hydraulic pressure, spindle speed and coolant pressure. These are predictive/classification associations; they do not establish that any individual variable causes machine failure.

### Analytical capability demonstrated

- Binary classification
- Confusion-matrix interpretation
- Recall versus overall accuracy
- Model interpretability
- Translating model error into an operational control boundary

---

## 3. Demand anticipation and predictive modelling

Python was used to prepare the planning data, exclude variables identified as potentially target-derived, apply a chronological train/test split, train a Random Forest regression model, and evaluate the resulting predictions. Power BI was used to present forecast alignment, model error and feature-importance results.

On the **two-month test period** used in the academic analysis, the Random Forest produced:

| Metric | Random Forest |
|---|---:|
| MAPE | 9.817% |
| MAE | 35.539 |
| RMSE | 64.247 |
| R² | 0.972 |

For comparison, the existing forecast had a MAPE of 22.638%, while the average monthly demand estimate had a MAPE of 20.141%.

These results are intentionally interpreted narrowly. The test period covered only July and August 2025, so the analysis does **not** establish that the model would generalise across longer planning horizons.

A critical modelling detail is that **the existing forecast was itself included as a model input** and was one of the strongest predictors. Therefore, the Random Forest should not be described as a fully independent replacement forecast. It is better characterised as a **model-based challenge/correction signal against the existing planning forecast**.

The three strongest predictors — `Forecast_units`, `Avg_Monthly_Demand_est`, and `Base_Monthly_Demand` — accounted for approximately 81% of model feature importance. This indicates predictive contribution within the analysed model; it does not establish causal influence.

The analysis also excluded variables identified as potentially target-derived and used a chronological split. Before any operational deployment, however, the timing and provenance of every predictor would still need to be verified to confirm that the information would genuinely be available at prediction time.

### Analytical capability demonstrated

- Python-based data preparation
- Regression modelling with Random Forest
- Chronological train/test design
- MAE, RMSE, MAPE and R² interpretation
- Feature-importance analysis
- Leakage-risk awareness
- Distinguishing predictive usefulness from causal explanation
- Evaluating a model against an existing planning baseline

---

## 4. Resource allocation and prioritisation

The third analysis shifted from prediction to prioritisation. Demand, planned receipts, production plan, stockout rate, fill rate and demand-supply gap were combined into an allocation-pressure view.

The purpose was to **rank where management review should begin**, rather than to perform full optimisation.

In the analysed proxy data, Packaging generated the strongest combined shortage-pressure signal, followed by Solvents and Additives. These are analytical rankings from the proxy dataset, **not recommendations for Vitaco's actual production allocation**.

The portfolio demonstration implements the pressure score as an **illustrative, equally weighted heuristic**. The weights are not empirically calibrated or business-validated, and the resulting quantile tiers are relative demonstration bands rather than validated operational thresholds.

Full optimisation would require additional decision variables and constraints such as:

- labour capacity;
- machine availability;
- margin or contribution economics;
- changeover time;
- scheduling rules; and
- operational service constraints.

### Analytical capability demonstrated

- Multi-indicator prioritisation
- Demand/supply gap analysis
- Service-risk interpretation
- Translating competing signals into review priorities
- Recognising the boundary between prioritisation and optimisation

---

## 5. What this project demonstrates

This project demonstrates a decision-oriented analytics workflow rather than a collection of isolated models:

**Business requirement → data role → analytical technique → model evaluation → limitation assessment → decision boundary**

The three methods serve different analytical jobs:

- **Decision Tree:** interpretable failure-risk classification for technical review.
- **Random Forest:** model-based challenge/correction signal against an existing demand forecast.
- **Allocation-pressure analysis:** structured prioritisation where supply and service indicators diverge.

The important competency is not simply achieving a metric. It is determining **what the metric supports, what it does not support, and what decision should remain with a human reviewer**.

---

## 6. Limitations

- The datasets are public proxy data and do not represent Vitaco's internal operational records.
- The demand model was evaluated on only two test months.
- External demand drivers such as promotions, retailer sell-through, competitor activity and broader market effects were not represented.
- The downtime analysis identifies associations with failure outcomes but does not establish causality.
- Predictor timing and provenance would require operational verification before deployment.
- Allocation-pressure analysis supports prioritisation rather than constrained optimisation.
- The pressure score is an illustrative heuristic rather than a validated business metric.
- Operational deployment would require governed internal data, validation, monitoring, business rules and appropriate decision controls.

---

## 7. Tools

- **Python** — data preparation, Random Forest regression and model evaluation
- **RapidMiner** — Decision Tree classification
- **Power BI** — analytical presentation and decision-support visualisation
- **Excel / data preparation workflows** — supporting inspection and preparation

---

## 8. Data and attribution

The underlying datasets are intentionally **not included** in this repository.

The analysis used public proxy datasets solely for the academic exercise. Dataset availability on a public platform is not treated as permission to redistribute the data.

This page is a **curated portfolio adaptation of postgraduate academic work**. It is not the original university submission, does not reproduce the original appendices or working files, and does not include lecturer feedback, assessment marks, assessment rubrics, raw data, cleaned data, or row-level outputs.
