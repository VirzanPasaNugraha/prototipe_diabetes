"""
Prediction Engine
"""

from __future__ import annotations

from services.model_service import ModelService

from utils.validation import Validation
from utils.preprocessing import Preprocessing
from utils.probability import Probability
from utils.risk_level import RiskLevel
from utils.recommendation import Recommendation
from utils.formatter import ResultFormatter


class Predictor:

    def __init__(self):

        self.model = ModelService().get_model()

    def predict_result(self, data: dict):

        # Validate input
        Validation.validate(data)

        # Preprocess input
        df = Preprocessing.prepare(data)

        # Prediction
        prediction = int(
            self.model.predict(df)[0]
        )

        # Probability
        probability = self.model.predict_proba(df)[0]

        positive = Probability.positive_probability(
            probability
        )

        negative = Probability.negative_probability(
            probability
        )

        # Risk Level
        level, color = RiskLevel.from_probability(
            positive
        )

        # Recommendation
        recommendations = Recommendation.get(
            level
        )

        # Raw Result
        raw_result = {

            "prediction": prediction,

            "positive_probability": positive,

            "negative_probability": negative,

            "positive_percentage": Probability.percentage(
                positive
            ),

            "negative_percentage": Probability.percentage(
                negative
            ),

            "risk_level": level,

            "risk_color": color,

            "recommendations": recommendations

        }

        return ResultFormatter.build(raw_result)