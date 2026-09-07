"""Synthetic demand-forecast challenge demonstration.

The existing forecast is treated as an input to a model-based challenge signal,
not as an independent benchmark-free forecast.
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_PATH = Path(__file__).parents[1] / "synthetic_demand_planning_demo.csv"
FEATURES = [
    "historical_demand",
    "existing_forecast",
    "safety_stock",
    "reorder_point",
    "planned_receipts",
    "on_hand",
    "lead_time_days",
]
TARGET = "actual_demand"


def mape(actual, predicted):
    actual = pd.Series(actual)
    predicted = pd.Series(predicted)
    mask = actual != 0
    return (abs((actual[mask] - predicted[mask]) / actual[mask]).mean() * 100)


def evaluate(actual, predicted):
    return {
        "MAE": mean_absolute_error(actual, predicted),
        "RMSE": mean_squared_error(actual, predicted) ** 0.5,
        "R2": r2_score(actual, predicted),
        "MAPE": mape(actual, predicted),
    }


def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["month"]).sort_values("month")
    cutoff = df["month"].sort_values().unique()[-3]
    train = df[df["month"] < cutoff]
    test = df[df["month"] >= cutoff]

    model = RandomForestRegressor(n_estimators=300, max_depth=8, random_state=42)
    model.fit(train[FEATURES], train[TARGET])
    predictions = model.predict(test[FEATURES])

    model_metrics = evaluate(test[TARGET], predictions)
    baseline_metrics = evaluate(test[TARGET], test["existing_forecast"])

    print("Synthetic demand-forecast challenge")
    print(f"Test period starts: {pd.Timestamp(cutoff).date()}")
    print("Random Forest:", {k: round(v, 3) for k, v in model_metrics.items()})
    print("Existing forecast:", {k: round(v, 3) for k, v in baseline_metrics.items()})
    print("Top features:")
    print(pd.Series(model.feature_importances_, index=FEATURES).sort_values(ascending=False).head(5).round(3))


if __name__ == "__main__":
    main()
