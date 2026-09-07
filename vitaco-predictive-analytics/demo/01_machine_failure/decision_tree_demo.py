# Synthetic Decision Tree demonstration
# This script is independently written and uses only the synthetic dataset.

from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

DATA_PATH = Path(__file__).parents[1] / "synthetic_machine_condition_demo.csv"
FEATURES = [
    "process_load",
    "thermal_load",
    "drive_torque",
    "fluid_pressure",
    "rotation_rate",
    "flow_pressure",
]


def main():
    df = pd.read_csv(DATA_PATH)
    X, y = df[FEATURES], df["failure_flag"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(f"Failure recall: {recall_score(y_test, predictions, zero_division=0):.3f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))
    print("Interpretation: recall focuses on actual failures detected; metrics do not establish causality or business readiness.")


if __name__ == "__main__":
    main()
