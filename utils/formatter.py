"""
Result Formatter
"""

from __future__ import annotations

from datetime import datetime

from services.model_service import ModelService


class ResultFormatter:

    @staticmethod
    def build(result: dict) -> dict:

        metadata = ModelService().get_metadata()

        version = ModelService().get_version()

        return {

            "application": "Diabetes Risk Prediction System",

            "prediction": (
                "Positive"
                if result["prediction"] == 1
                else "Negative"
            ),

            "prediction_code": result["prediction"],

            "probability": f"{result['positive_percentage']:.2f}%",

            "positive_probability": result["positive_probability"],

            "negative_probability": result["negative_probability"],

            "positive_percentage": result["positive_percentage"],

            "negative_percentage": result["negative_percentage"],

            "risk_level": result["risk_level"],

            "risk_color": result["risk_color"],

            "recommendations": result["recommendations"],

            "model": metadata["model_name"],

            "framework": metadata["framework"],

            "dataset": metadata["dataset"],

            "version": version["version"],

            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }