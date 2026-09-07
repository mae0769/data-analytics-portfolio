"""Synthetic resource-prioritisation demonstration."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parents[1] / "synthetic_allocation_demo.csv"


def main():
    df = pd.read_csv(DATA_PATH)
    ranked = df.sort_values("pressure_score", ascending=False).copy()
    ranked["priority_tier"] = pd.qcut(
        ranked["pressure_score"], q=3, labels=["Lower", "Medium", "Higher"], duplicates="drop"
    )
    print("Synthetic resource-prioritisation analysis")
    print(ranked[["product_group", "demand_supply_gap", "stockout_rate", "fill_rate", "pressure_score", "priority_tier"]].to_string(index=False))
    print("\nInterpretation: the ranking is a decision-support signal for review; it is not a production-allocation optimisation model.")


if __name__ == "__main__":
    main()
