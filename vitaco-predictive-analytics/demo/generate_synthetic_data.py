"""Generate independent synthetic datasets for the portfolio demonstrations."""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
OUTPUT_DIR = Path(__file__).parent


def generate_machine_data(rng, n_rows=1200):
    dates = pd.date_range("2025-01-01", periods=n_rows, freq="D")
    process_load = rng.normal(50, 10, n_rows).clip(20, 85)
    thermal_load = (45 + 0.55 * process_load + rng.normal(0, 5, n_rows)).clip(35, 100)
    drive_torque = (18 + 0.55 * process_load + rng.normal(0, 4, n_rows)).clip(10, 75)
    fluid_pressure = (55 + 0.65 * process_load + rng.normal(0, 6, n_rows)).clip(35, 115)
    rotation_rate = (2200 + 22 * process_load + rng.normal(0, 180, n_rows)).clip(1500, 4500)
    flow_pressure = (30 + 0.35 * process_load + rng.normal(0, 3, n_rows)).clip(15, 65)

    stress = (
        0.035 * (process_load - 50)
        + 0.045 * (thermal_load - 70)
        + 0.04 * (drive_torque - 45)
        + 0.025 * (fluid_pressure - 85)
        + 0.015 * (rotation_rate - 3300) / 10
        + 0.03 * (flow_pressure - 48)
    )
    probability = 1 / (1 + np.exp(-stress))
    failure_flag = (rng.random(n_rows) < probability).astype(int)

    return pd.DataFrame({
        "date": dates,
        "asset_group": rng.choice(["Group_A", "Group_B", "Group_C"], n_rows),
        "process_load": process_load.round(2),
        "thermal_load": thermal_load.round(2),
        "drive_torque": drive_torque.round(2),
        "fluid_pressure": fluid_pressure.round(2),
        "rotation_rate": rotation_rate.round(0).astype(int),
        "flow_pressure": flow_pressure.round(2),
        "failure_flag": failure_flag,
    })


def generate_demand_data(rng, n_skus=24, months=18):
    rows = []
    dates = pd.date_range("2025-01-01", periods=months, freq="MS")
    for sku_idx in range(n_skus):
        sku = f"SKU_{sku_idx + 1:02d}"
        base = rng.uniform(300, 1200)
        trend = rng.uniform(-0.01, 0.025)
        seasonal_phase = rng.uniform(0, 2 * np.pi)
        previous = base
        for month_idx, date in enumerate(dates):
            seasonal = 1 + 0.12 * np.sin(2 * np.pi * month_idx / 12 + seasonal_phase)
            demand = max(50, previous * (1 + trend) * seasonal + rng.normal(0, base * 0.08))
            existing_forecast = max(50, demand * (1 + rng.normal(0, 0.14)) + rng.normal(0, base * 0.05))
            safety_stock = max(40, base * rng.uniform(0.12, 0.22))
            reorder_point = safety_stock + base * rng.uniform(0.25, 0.45)
            planned_receipts = max(0, demand * rng.uniform(0.72, 1.05))
            on_hand = max(0, rng.normal(base * 0.35, base * 0.12))
            lead_time = rng.integers(5, 31)
            rows.append({
                "month": date,
                "sku_id": sku,
                "historical_demand": round(previous, 2),
                "existing_forecast": round(existing_forecast, 2),
                "safety_stock": round(safety_stock, 2),
                "reorder_point": round(reorder_point, 2),
                "planned_receipts": round(planned_receipts, 2),
                "on_hand": round(on_hand, 2),
                "lead_time_days": int(lead_time),
                "actual_demand": round(demand, 2),
            })
            previous = demand
    return pd.DataFrame(rows)


def generate_allocation_data(rng, n_groups=10):
    groups = [f"Group_{chr(65 + i)}" for i in range(n_groups)]
    demand = rng.uniform(45000, 140000, n_groups)
    planned_receipts = demand * rng.uniform(0.55, 0.95, n_groups)
    production_plan = demand * rng.uniform(1.4, 4.2, n_groups)
    stockout_rate = rng.uniform(0.05, 0.30, n_groups)
    fill_rate = np.clip(1 - stockout_rate * rng.uniform(0.15, 0.65, n_groups), 0.82, 0.999)

    df = pd.DataFrame({
        "product_group": groups,
        "actual_demand": demand,
        "planned_receipts": planned_receipts,
        "production_plan": production_plan,
        "stockout_rate": stockout_rate,
        "fill_rate": fill_rate,
    })
    df["demand_supply_gap"] = df["actual_demand"] - df["planned_receipts"]
    df["pressure_score"] = (
        df["demand_supply_gap"] / df["actual_demand"]
        + df["stockout_rate"]
        + (1 - df["fill_rate"])
    )
    return df.round(4)


def main():
    rng = np.random.default_rng(SEED)
    machine = generate_machine_data(rng)
    demand = generate_demand_data(rng)
    allocation = generate_allocation_data(rng)

    machine.to_csv(OUTPUT_DIR / "synthetic_machine_condition_demo.csv", index=False)
    demand.to_csv(OUTPUT_DIR / "synthetic_demand_planning_demo.csv", index=False)
    allocation.to_csv(OUTPUT_DIR / "synthetic_allocation_demo.csv", index=False)

    print(f"Generated {len(machine):,} machine records")
    print(f"Generated {len(demand):,} demand-planning records")
    print(f"Generated {len(allocation):,} allocation records")


if __name__ == "__main__":
    main()
