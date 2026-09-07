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

## Decision boundary

The analysis does **not** claim to identify causal drivers, prescribe staffing, optimise warehouse capacity, or make automatic operational decisions. It creates a structured evidence base for the next investigation step.

Because the data is synthetic, every observed pattern is illustrative rather than evidence about a real organisation.
