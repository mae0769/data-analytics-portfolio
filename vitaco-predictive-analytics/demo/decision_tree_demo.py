# Synthetic Decision Tree demonstration
# This script is independently written and uses only the synthetic dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score

DATA_PATH = "synthetic_machine_condition_demo.csv"

FEATURES = [
    "cutting_force",
    "coolant_temperature",
    "torque",
    "hydraulic_pressure",
    "spindle_speed",
    "coolant_pressure",
]


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURES]
    y = df["machine_failure"]

    # Stratified split is used only for this synthetic demonstration.
    # It is not a reconstruction of the academic modelling procedure.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions, zero_division=0)
    matrix = confusion_matrix(y_test, predictions)

    print(f"Accuracy: {accuracy:.3f}")
    print(f"Failure recall: {recall:.3f}")
    print("Confusion matrix:")
    print(matrix)

    # Accuracy summarises all classifications.
    # Failure recall focuses on how many actual failures were detected.
    # Neither metric alone establishes business readiness or causality.


if __name__ == "__main__":
    main()
