"""
Risk Level Utility
"""

from __future__ import annotations


class RiskLevel:

    @staticmethod
    def from_probability(probability: float):

        if probability < 0.20:

            return (
                "Very Low",
                "#22C55E"
            )

        if probability < 0.40:

            return (
                "Low",
                "#84CC16"
            )

        if probability < 0.60:

            return (
                "Moderate",
                "#FACC15"
            )

        if probability < 0.80:

            return (
                "High",
                "#F59E0B"
            )

        return (
            "Very High",
            "#EF4444"
        )