"""
Threshold Utility
"""

from __future__ import annotations


class Threshold:

    DEFAULT = 0.50

    @classmethod
    def classify(cls, probability: float) -> int:
        """
        Convert probability to prediction class.
        """

        return 1 if probability >= cls.DEFAULT else 0