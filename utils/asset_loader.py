"""
Research Figure Asset Loader
"""

from pathlib import Path

# =====================================================
# ROOT DIRECTORY
# =====================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

FIGURE_DIR = ROOT_DIR / "outputs" / "figures"

# =====================================================
# HELPER
# =====================================================

def get_figure(filename: str) -> str:
    """
    Return absolute figure path as string.
    """
    return str(FIGURE_DIR / filename)

# =====================================================
# MODEL PERFORMANCE
# =====================================================

ROC_CURVE = get_figure(
    "roc_curve_comparison.png"
)

PR_CURVE = get_figure(
    "pr_curve_comparison.png"
)

CONFUSION_MATRIX = get_figure(
    "confusion_matrix_best_model.png"
)

# =====================================================
# CALIBRATION
# =====================================================

CALIBRATION_CURVE = get_figure(
    "calibration_curve_comparison.png"
)

RELIABILITY_CATBOOST = get_figure(
    "reliability_diagram_catboost.png"
)

RELIABILITY_LOGISTIC = get_figure(
    "reliability_diagram_logistic_regression.png"
)

RELIABILITY_RANDOM_FOREST = get_figure(
    "reliability_diagram_random_forest.png"
)

RELIABILITY_XGBOOST = get_figure(
    "reliability_diagram_xgboost.png"
)

# =====================================================
# SHAP
# =====================================================

SHAP_SUMMARY = get_figure(
    "shap_summary_plot.png"
)

SHAP_BAR = get_figure(
    "shap_bar_plot.png"
)

FEATURE_IMPORTANCE = get_figure(
    "permutation_importance.png"
)

# =====================================================
# THRESHOLD
# =====================================================

THRESHOLD = get_figure(
    "threshold_optimization_plot.png"
)

# =====================================================
# DATASET ANALYSIS
# =====================================================

CLASS_DISTRIBUTION = get_figure(
    "class_distribution.png"
)

AGE_DISTRIBUTION = get_figure(
    "age_distribution.png"
)

BMI_DISTRIBUTION = get_figure(
    "bmi_distribution.png"
)

CORRELATION_HEATMAP = get_figure(
    "correlation_heatmap.png"
)

HIGHBP_VS_DIABETES = get_figure(
    "highbp_vs_diabetes.png"
)

HIGHCHOL_VS_DIABETES = get_figure(
    "highchol_vs_diabetes.png"
)

VIF_ANALYSIS = get_figure(
    "vif_analysis.png"
)

# =====================================================
# ADDITIONAL ANALYSIS
# =====================================================

ABLATION_STUDY = get_figure(
    "ablation_study_plot.png"
)

MISCLASSIFICATION_SUMMARY = get_figure(
    "misclassification_summary_plot.png"
)

# =====================================================
# OPTIONAL
# =====================================================

ALL_FIGURES = {
    "roc_curve": ROC_CURVE,
    "pr_curve": PR_CURVE,
    "confusion_matrix": CONFUSION_MATRIX,
    "calibration_curve": CALIBRATION_CURVE,
    "reliability_catboost": RELIABILITY_CATBOOST,
    "reliability_logistic": RELIABILITY_LOGISTIC,
    "reliability_random_forest": RELIABILITY_RANDOM_FOREST,
    "reliability_xgboost": RELIABILITY_XGBOOST,
    "shap_summary": SHAP_SUMMARY,
    "shap_bar": SHAP_BAR,
    "feature_importance": FEATURE_IMPORTANCE,
    "threshold": THRESHOLD,
    "class_distribution": CLASS_DISTRIBUTION,
    "age_distribution": AGE_DISTRIBUTION,
    "bmi_distribution": BMI_DISTRIBUTION,
    "correlation_heatmap": CORRELATION_HEATMAP,
    "highbp_vs_diabetes": HIGHBP_VS_DIABETES,
    "highchol_vs_diabetes": HIGHCHOL_VS_DIABETES,
    "vif_analysis": VIF_ANALYSIS,
    "ablation_study": ABLATION_STUDY,
    "misclassification_summary": MISCLASSIFICATION_SUMMARY,
}