"""
Global Configuration
Diabetes Risk Prediction System
"""

from pathlib import Path

# ==========================================================
# PROJECT PATH
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parent

ASSETS_DIR = ROOT_DIR / "assets"
DATA_DIR = ROOT_DIR / "data"
MODELS_DIR = ROOT_DIR / "models"
DOCS_DIR = ROOT_DIR / "docs"
OUTPUTS_DIR = ROOT_DIR / "outputs"
CACHE_DIR = ROOT_DIR / "cache"
LOGS_DIR = ROOT_DIR / "logs"

# ==========================================================
# MODEL
# ==========================================================

MODEL_FILENAME = "best_model_pipeline.pkl"

MODEL_PATH = MODELS_DIR / MODEL_FILENAME

METADATA_PATH = MODELS_DIR / "metadata.json"

VERSION_PATH = MODELS_DIR / "version.json"

# ==========================================================
# APP
# ==========================================================

APP_NAME = "Diabetes Risk Prediction System"

APP_VERSION = "1.0.0"

AUTHOR = "Virzan Pasa Nugraha"

# ==========================================================
# OUTPUT
# ==========================================================

REPORT_DIR = OUTPUTS_DIR / "reports"

PREDICTION_DIR = OUTPUTS_DIR / "predictions"

FIGURE_DIR = OUTPUTS_DIR / "figures"

EXPORT_DIR = OUTPUTS_DIR / "exports"

# ==========================================================
# RANDOM
# ==========================================================

RANDOM_STATE = 42