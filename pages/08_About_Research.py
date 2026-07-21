"""
About Research
"""

import streamlit as st
import pandas as pd

from utils.asset_loader import (
    CORRELATION_HEATMAP,
    BMI_DISTRIBUTION,
    VIF_ANALYSIS,
    ABLATION_STUDY,
    MISCLASSIFICATION_SUMMARY,
)

st.set_page_config(
    page_title="About Research",
    page_icon="📖",
    layout="wide"
)

st.title("📖 About Research")

st.caption(
    "Research background and methodology."
)

st.divider()

# ======================================================
# TITLE
# ======================================================

st.subheader("Research Title")

st.info(
"""
Comprehensive Diabetes Risk Prediction Using BRFSS Data:
Performance, Explainability, Fairness, and Calibration
"""
)

st.divider()

# ======================================================
# OVERVIEW
# ======================================================

st.subheader("Research Overview")

st.write(
"""
This application implements the final machine learning model
developed from the diabetes risk prediction research.

The objective is to provide reliable diabetes risk prediction
while ensuring model interpretability, fairness,
and probability calibration.
"""
)

st.divider()

# ======================================================
# DATASET
# ======================================================

st.subheader("Dataset")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Dataset",
        "BRFSS 2015"
    )

with c2:
    st.metric(
        "Samples",
        "69,057"
    )

with c3:
    st.metric(
        "Features",
        "21"
    )

with c4:
    st.metric(
        "Target",
        "Diabetes"
    )

st.divider()

# ======================================================
# PIPELINE
# ======================================================

st.subheader("Machine Learning Pipeline")

pipeline = pd.DataFrame({

    "Step":[
        "Data Cleaning",
        "Feature Engineering",
        "Nested Cross Validation",
        "Hyperparameter Optimization",
        "Model Evaluation",
        "Explainability",
        "Fairness Analysis",
        "Calibration",
        "Threshold Analysis"
    ],

    "Technique":[
        "Cleaning & Validation",
        "BRFSS Health Indicators",
        "10x5 CV",
        "GridSearchCV",
        "Multiple Metrics",
        "SHAP",
        "Group Evaluation",
        "Reliability Analysis",
        "Threshold Optimization"
    ]

})

st.dataframe(
    pipeline,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ======================================================
# MODELS
# ======================================================

st.subheader("Evaluated Models")

models = pd.DataFrame({

    "Model":[
        "Logistic Regression",
        "Random Forest",
        "XGBoost",
        "CatBoost"
    ],

    "Status":[
        "Evaluated",
        "Evaluated",
        "Evaluated",
        "Selected"
    ]

})

st.dataframe(
    models,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ======================================================
# FINAL RESULT
# ======================================================

st.subheader("Final Performance")

performance = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Balanced Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC",
        "PR-AUC",
        "MCC",
        "Brier Score"
    ],

    "Value":[
        0.7495,
        0.7486,
        0.7320,
        0.8000,
        0.7645,
        0.8267,
        0.8073,
        0.5003,
        0.1684
    ]

})

st.dataframe(
    performance,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ======================================================
# DATASET & MODEL DIAGNOSTICS (previously missing)
# ======================================================

st.subheader("Dataset & Model Diagnostics")

st.write(
    """
    Additional exploratory and diagnostic analyses conducted
    during the research, complementing the performance,
    SHAP, fairness, and calibration results shown on the
    other pages.
    """
)

diag_tab1, diag_tab2, diag_tab3, diag_tab4 = st.tabs(
    [
        "🔥 Correlation Heatmap",
        "📏 BMI Distribution",
        "🧮 VIF Analysis",
        "✂️ Ablation & Misclassification",
    ]
)

# ---------------------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------------------

with diag_tab1:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            CORRELATION_HEATMAP,
            caption="Correlation Heatmap of All Variables",
            use_column_width=True
        )

    with col2:
        st.subheader("Interpretation")
        st.write(
            """
            Diabetes status is positively correlated with
            HighBP, HighChol, BMI, GenHlth, DiffWalk, and Age.

            Education and Income show relatively weak
            negative correlations with diabetes status.

            All correlations are moderate, indicating no
            severe multicollinearity among predictor
            variables.
            """
        )

# ---------------------------------------------------
# BMI DISTRIBUTION
# ---------------------------------------------------

with diag_tab2:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            BMI_DISTRIBUTION,
            caption="BMI Distribution by Diabetes Status",
            use_column_width=True
        )

    with col2:
        st.subheader("Interpretation")
        st.write(
            """
            Individuals with diabetes tend to have higher
            BMI values compared to those without diabetes.

            The diabetes group is concentrated around BMI
            values above 25, indicating that higher BMI is
            associated with increased diabetes risk.
            """
        )

# ---------------------------------------------------
# VIF ANALYSIS
# ---------------------------------------------------

with diag_tab3:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            VIF_ANALYSIS,
            caption="Variance Inflation Factor (VIF) Results",
            use_column_width=True
        )

    with col2:
        st.subheader("Interpretation")
        st.write(
            """
            All numerical variables have VIF values below 2.0,
            indicating no serious multicollinearity issues.

            Highest VIF: GenHlth (1.6813), PhysHlth (1.5474)

            Lowest VIF: BMI (1.0802), Age (1.0711)

            Numerical features provide complementary
            information without excessive overlap.
            """
        )

# ---------------------------------------------------
# ABLATION + MISCLASSIFICATION
# ---------------------------------------------------

with diag_tab4:

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            ABLATION_STUDY,
            caption="Feature Impact Based on Ablation Study",
            use_column_width=True
        )

        st.write(
            """
            Removing **BMI** causes the largest ROC-AUC
            drop (0.0153), while removing **GenHlth** causes
            the largest Recall drop (0.0159).

            BMI drives overall discrimination; GenHlth drives
            sensitivity to positive diabetes cases.
            """
        )

    with col2:
        st.image(
            MISCLASSIFICATION_SUMMARY,
            caption="Misclassification Distribution",
            use_column_width=True
        )

        st.write(
            """
            False Positives (2,069) outnumber False Negatives
            (1,405), showing the model tends to over-predict
            diabetes risk.

            580 high-confidence errors and 1,307 borderline
            predictions highlight remaining room for
            improvement.
            """
        )

st.divider()

# ======================================================
# KEY FINDINGS
# ======================================================

st.subheader("Key Findings")

st.success(
"""
• CatBoost achieved the best overall performance.

• SHAP identified General Health, BMI, Age,
High Cholesterol, and High Blood Pressure as the
most influential features.

• Fairness evaluation showed disparities across age and
education groups, with older individuals detected more
reliably than younger ones.

• Calibration analysis demonstrated reliable
probability estimates (lowest Brier Score among all models).

• Ablation study confirms BMI and GenHlth as the most
critical features for discrimination and sensitivity.

• Threshold optimization provides flexibility
between balanced prediction and screening scenarios.
"""
)

st.divider()

# ======================================================
# TECHNOLOGIES
# ======================================================

st.subheader("Technologies")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.write("""
🐍 Python

🤖 CatBoost

📊 Scikit-Learn

📈 Pandas
""")

with tech2:

    st.write("""
🧠 SHAP

📉 Calibration

⚖ Fairness

📋 Nested CV
""")

with tech3:

    st.write("""
🎨 Streamlit

📁 BRFSS

🔬 Machine Learning

📚 Research
""")

st.divider()

# ======================================================
# REFERENCE
# ======================================================

st.subheader("Reference")

st.info(
"""
BRFSS 2015

Behavioral Risk Factor Surveillance System

Centers for Disease Control and Prevention (CDC)

Machine Learning:
CatBoost

Explainability:
SHAP
"""
)

st.caption(
"Research implementation dashboard."
)