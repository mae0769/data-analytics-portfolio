"""Generate an independently created synthetic machine-condition dataset."""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
N_ROWS = 1200
OUTPUT = Path(__file__).with_name("synthetic_machine_condition_demo.csv")


def main():
    rng = np.random.default_rng(SEED)
    dates = pd.date_range("2025-01-01", periods=N_ROWS, freq="D")

    process_load = rng.normal(50, 10, N_ROWS).clip(20, 85)
    thermal_load = (45 + 0.55 * process_load + rng.normal(0, 5, N_ROWS)).clip(35, 100)
    drive_torque = (18 + 0.55 * process_load + rng.normal(0, 4, N_ROWS)).clip(10, 75)
    fluid_pressure = (55 + 0.65 * process_load + rng.normal(0, 6, N_ROWS)).clip(35, 115)
    rotation_rate = (2200 + 22 * process_load + rng.normal(0, 180, N_ROWS)).clip(1500, 4500)
    flow_pressure = (30 + 0.35 * process_load + rng.normal(0, 3, N_ROWS)).clip(15, 65)

    stress = (
        0.035 * (process_load - 50)
        + 0.045 * (thermal_load - 70)
        + 0.04 * (drive_torque - 45)
        + 0.025 * (fluid_pressure - 85)
        + 0.015 * (rotation_rate - 3300) / 10
        + 0.03 * (flow_pressure - 48)
    )
    probability = 1 / (1 + np.exp(-stress))
    failure_flag = (rng.random(N_ROWS) < probability).astype(int)

    df = pd.DataFrame(
        {
            "date": dates,
            "asset_group": rng.choice(["Group_A", "Group_B", "Group_C"], N_ROWS),
            "process_load": process_load.round(2),
            "thermal_load": thermal_load.round(2),
            "drive_torque": drive_torque.round(2),
            "fluid_pressure": fluid_pressure.round(2),
            "rotation_rate": rotation_rate.round(0).astype(int),
            "flow_pressure": flow_pressure.round(2),
            "failure_flag": failure_flag,
        }
    )

    df.to_csv(OUTPUT, index=False)
    print(f"Generated {len(df):,} synthetic records: {OUTPUT}")


if __name__ == "__main__":
    main()
