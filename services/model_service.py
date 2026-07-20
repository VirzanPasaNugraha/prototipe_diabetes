"""
Model Service

Central access point for:
- ML Model
- Metadata
- Version
"""

from __future__ import annotations

from utils.loader import Loader


class ModelService:

    def __init__(self):

        self._model = None
        self._metadata = None
        self._version = None

    def get_model(self):

        if self._model is None:
            self._model = Loader.load_model()

        return self._model

    def get_metadata(self):

        if self._metadata is None:
            self._metadata = Loader.load_metadata()

        return self._metadata

    def get_version(self):

        if self._version is None:
            self._version = Loader.load_version()

        return self._version

    def reload(self):

        self._model = Loader.load_model()

        self._metadata = Loader.load_metadata()

        self._version = Loader.load_version()

    def is_ready(self) -> bool:

        try:

            self.get_model()

            self.get_metadata()

            self.get_version()

            return True

        except Exception:

            return False