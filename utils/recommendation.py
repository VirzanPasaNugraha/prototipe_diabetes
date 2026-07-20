"""
Recommendation Engine
"""

from __future__ import annotations


class Recommendation:

    @staticmethod
    def get(level: str):

        recommendations = {

            "Very Low": [

                "Continue maintaining a healthy lifestyle.",

                "Perform routine health checkups."

            ],

            "Low": [

                "Maintain regular physical activity.",

                "Monitor your body weight."

            ],

            "Moderate": [

                "Improve dietary habits.",

                "Increase weekly physical activity.",

                "Monitor blood glucose regularly."

            ],

            "High": [

                "Consult a healthcare professional.",

                "Reduce sugar intake.",

                "Increase physical activity.",

                "Monitor blood pressure."

            ],

            "Very High": [

                "Seek medical evaluation immediately.",

                "Perform comprehensive blood tests.",

                "Adopt lifestyle modifications under medical supervision."

            ]

        }

        return recommendations.get(level, [])