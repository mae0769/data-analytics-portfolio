"""Synthetic resource-prioritisation demonstration.

The pressure score is an illustrative, equally weighted heuristic for
portfolio demonstration purposes. It is not a validated operational KPI.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parents[1] / "synthetic_allocation_demo.csv"


PRESSURE_COMPONENTS = [
    "demand_supply_gap_ratio",
    "stockout_rate",
    "service_gap",
]


def main():
    df = pd.read_csv(DATA_PATH)

    # Equal weighting is deliberately transparent for the synthetic demo.
    df["demand_supply_gap_ratio"] = (
        df["demand_supply_gap"] / df["actual_demand"]
    )
    df["service_gap"] = 1 - df["fill_rate"]
    df["pressure_score"] = df[PRESSURE_COMPONENTS].mean(axis=1)

    ranked = df.sort_values("pressure_score", ascending=False).copy()
    ranked["priority_tier"] = pd.qcut(
        ranked["pressure_score"],
        q=3,
        labels=["Lower", "Medium", "Higher"],
        duplicates="drop",
    )

    print("Synthetic resource-prioritisation analysis")
    print(
        ranked[
            [
                "product_group",
                "demand_supply_gap_ratio",
                "stockout_rate",
                "fill_rate",
                "pressure_score",
                "priority_tier",
            ]
        ].to_string(index=False)
    )
    print(
        "\nInterpretation: the score is an equally weighted heuristic for review prioritisation. "
        "It is not a validated KPI or a production-allocation optimisation model."
    )


if __name__ == "__main__":
    main()
