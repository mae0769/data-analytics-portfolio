# Analytical findings framework

This project is designed to demonstrate how SQL outputs are translated into business investigation priorities.

## Interpretation principles

### 1. Separate incidence from exposure

A warehouse can have a high delay rate but relatively few delayed orders. Another warehouse can have a lower rate but a much larger number of delayed orders. Both measures should therefore be considered before deciding where management attention is warranted.

### 2. Treat concentration as an investigation signal

If delays cluster around a warehouse or product category, that pattern is evidence for further investigation. It is not proof of root cause.

Potential follow-up questions include processing time, inventory availability, order mix, capacity constraints and scheduling conditions.

### 3. Use trends to identify change, not explain it automatically

Month-over-month changes and rolling averages can identify deterioration or improvement. They do not establish why performance changed without additional evidence.

## Expected decision output

The final SQL summary is intended to answer:

> **Where should an analyst or manager investigate first, and what evidence supports that priority?**

The answer should reference both absolute delayed volume and delay rate, while considering average delay duration and recent trend.

## Results from the synthetic run

The figures below come from running the SQL files against the synthetic database (3,000 orders, seed 42). They are illustrative only.

### Data quality

Checks 1–4 and 6 returned no issues: no duplicate order IDs, no orders without a fulfilment record, no missing warehouse assignments, no fulfilment activity before the order date and no invalid quantities. Check 5 returned 956 shipments sent after the promised date. That is not a data error; it is the delay the rest of the analysis investigates.

### Overall performance

| Fulfilled orders | Delayed orders | Delay rate | Avg fulfilment days |
|---:|---:|---:|---:|
| 3,000 | 956 | 31.87% | 3.90 |

### Warehouse comparison

| Warehouse | Fulfilled | Delayed | Delay rate | Avg days late (when delayed) | Volume rank | Rate rank |
|---|---:|---:|---:|---:|---:|---:|
| Warehouse D | 602 | 368 | 61.13% | 2.85 | 1 | 1 |
| Warehouse A | 634 | 166 | 26.18% | 1.84 | 2 | 2 |
| Warehouse C | 582 | 150 | 25.77% | 1.83 | 3 | 3 |
| Warehouse E | 584 | 142 | 24.32% | 2.05 | 4 | 4 |
| Warehouse B | 598 | 130 | 21.74% | 1.68 | 5 | 5 |

Warehouse D stands out on every measure: more than double the delay rate of any other warehouse, the most delayed orders and the longest delays when late.

### Product categories

| Category | Order-item records | Delayed records | Delay rate |
|---|---:|---:|---:|
| Consumables | 1,620 | 511 | 31.54% |
| Components | 1,418 | 455 | 32.09% |
| Packaging | 1,371 | 423 | 30.85% |
| Maintenance | 979 | 305 | 31.15% |
| Equipment | 570 | 190 | 33.33% |

Category delay rates sit within a narrow band (30.85–33.33%). Equipment has the highest rate but the lowest volume; Consumables has the most delayed records at an average rate. This is the incidence-versus-exposure distinction in practice, and neither measure suggests a category-level problem.

### Monthly trend

Monthly delay rates ranged from 26.47% (November) to 37.94% (December), with December showing the largest month-over-month rise (+11.47 percentage points). The three-month rolling average stayed between 29.92% and 33.10%, so there is no sustained trend; December is worth monitoring rather than acting on alone.

### Investigation priority

**Warehouse D should be investigated first.** It ranks first on both delayed volume and delay rate, so the priority does not depend on which measure is used. Product category does not explain the pattern.

### Validating the analysis against a known answer

The synthetic data generator deliberately builds longer processing times and a higher chance of late shipments into Warehouse D, and builds no category effect. The queries recovered both: a clear Warehouse D signal and no category signal. This confirms the analysis finds a real pattern when one exists and does not invent one when it does not.

## Decision boundary

The analysis does **not** claim to identify causal drivers, prescribe staffing, optimise warehouse capacity, or make automatic operational decisions. It creates a structured evidence base for the next investigation step.

Because the data is synthetic, every observed pattern is illustrative rather than evidence about a real organisation.
