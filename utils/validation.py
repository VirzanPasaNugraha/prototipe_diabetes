"""
Validation Engine
"""

from __future__ import annotations

from config import DATA_DIR
import json


with open(DATA_DIR / "feature_order.json", encoding="utf-8") as f:
    REQUIRED_FEATURES = json.load(f)


BINARY_FEATURES = {
    "HighBP",
    "HighChol",
    "CholCheck",
    "Smoker",
    "Stroke",
    "HeartDiseaseorAttack",
    "PhysActivity",
    "Fruits",
    "Veggies",
    "HvyAlcoholConsump",
    "AnyHealthcare",
    "NoDocbcCost",
    "DiffWalk",
    "Sex"
}


class Validation:

    @staticmethod
    def validate(data: dict):

        missing = []

        for feature in REQUIRED_FEATURES:

            if feature not in data:
                missing.append(feature)

        if missing:
            raise ValueError(
                f"Missing feature(s): {', '.join(missing)}"
            )

        for key, value in data.items():

            if value is None:
                raise ValueError(f"{key} cannot be None.")

            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"{key} must be numeric."
                )

        for feature in BINARY_FEATURES:

            if data[feature] not in (0, 1):
                raise ValueError(
                    f"{feature} must be 0 or 1."
                )

        if data["BMI"] <= 0:
            raise ValueError("BMI must be > 0.")

        if not (1 <= data["GenHlth"] <= 5):
            raise ValueError(
                "GenHlth must be between 1-5."
            )

        return True