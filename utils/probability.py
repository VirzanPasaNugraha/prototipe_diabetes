"""
Probability Utility
"""

from __future__ import annotations


class Probability:

    @staticmethod
    def positive_probability(probabilities):

        """
        Return probability of positive class.
        """

        return float(probabilities[1])

    @staticmethod
    def negative_probability(probabilities):

        """
        Return probability of negative class.
        """

        return float(probabilities[0])

    @staticmethod
    def percentage(value: float) -> float:

        return round(value * 100, 2)