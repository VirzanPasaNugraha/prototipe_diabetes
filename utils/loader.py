"""
Model Loader Utility

Responsible for:
- Loading model
- Loading metadata
- Loading version information
"""

from __future__ import annotations

import json
import pickle
from pathlib import Path
from typing import Any

from config import (
    MODEL_PATH,
    METADATA_PATH,
    VERSION_PATH,
)


class Loader:

    @staticmethod
    def load_model() -> Any:
        """
        Load trained machine learning model.
        """

        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model not found:\n{MODEL_PATH}"
            )

        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)

        return model

    @staticmethod
    def load_metadata() -> dict:

        if not METADATA_PATH.exists():
            raise FileNotFoundError(
                f"Metadata not found:\n{METADATA_PATH}"
            )

        with open(
            METADATA_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def load_version() -> dict:

        if not VERSION_PATH.exists():
            raise FileNotFoundError(
                f"Version file not found:\n{VERSION_PATH}"
            )

        with open(
            VERSION_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)