"""
About Research
"""

import streamlit as st
import pandas as pd

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
# KEY FINDINGS
# ======================================================

st.subheader("Key Findings")

st.success(
"""
• CatBoost achieved the best overall performance.

• SHAP identified General Health, BMI, Age,
High Cholesterol, and High Blood Pressure as the
most influential features.

• Fairness evaluation showed relatively balanced
performance across demographic groups.

• Calibration analysis demonstrated reliable
probability estimates.

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