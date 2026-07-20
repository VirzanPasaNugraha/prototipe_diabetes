"""
Preprocessing Engine
"""

from __future__ import annotations

import json
import pandas as pd

from config import DATA_DIR


with open(DATA_DIR / "feature_order.json", encoding="utf-8") as f:
    FEATURE_ORDER = json.load(f)


class Preprocessing:

    @staticmethod
    def prepare(data: dict):

        ordered = {}

        for feature in FEATURE_ORDER:

            ordered[feature] = float(data[feature])

        return pd.DataFrame([ordered])