"""
Home Page
Research Dashboard
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🩺 Diabetes Risk Prediction System")

st.caption(
    "Machine Learning-Based Diabetes Risk Prediction Using BRFSS 2015 Dataset"
)

st.divider()

# =====================================================
# RESEARCH OVERVIEW
# =====================================================

st.subheader("Research Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Dataset",
        "BRFSS 2015"
    )

with col2:

    st.metric(
        "Samples",
        "69,057"
    )

with col3:

    st.metric(
        "Features",
        "21"
    )

with col4:

    st.metric(
        "Algorithm",
        "CatBoost"
    )

st.divider()

# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.subheader("Model Performance")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Accuracy",
        "74.95%"
    )

with c2:

    st.metric(
        "ROC-AUC",
        "82.67%"
    )

with c3:

    st.metric(
        "PR-AUC",
        "80.73%"
    )

with c4:

    st.metric(
        "MCC",
        "0.5003"
    )

st.divider()

# =====================================================
# MODEL INFORMATION
# =====================================================

left, right = st.columns([1,1])

with left:

    st.subheader("Model Information")

    info = pd.DataFrame({

        "Item":[
            "Algorithm",
            "Framework",
            "Dataset",
            "Validation",
            "Hyperparameter Search",
            "Selected Model"
        ],

        "Value":[
            "CatBoostClassifier",
            "CatBoost",
            "BRFSS 2015",
            "Nested Cross Validation",
            "GridSearchCV",
            "Best Pipeline"
        ]

    })

    st.dataframe(
        info,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("Research Components")

    st.success("Prediction Module")

    st.success("Model Performance Evaluation")

    st.success("SHAP Explainability")

    st.success("Fairness Analysis")

    st.success("Calibration Analysis")

    st.success("Threshold Analysis")

st.divider()

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

st.subheader("Top Important Features")

st.caption(
    "Mean |SHAP value| — feature contribution to the final CatBoost model predictions."
)

importance = pd.DataFrame({

    "Feature":[
        "GenHlth",
        "BMI",
        "Age",
        "HighChol",
        "HighBP"
    ],

    "Mean |SHAP Value|":[
        0.5586,
        0.4721,
        0.4011,
        0.3380,
        0.3226
    ]

})

st.bar_chart(
    importance.set_index("Feature")
)

st.caption(
    "See the SHAP Explainability page for the full summary and bar plots."
)

st.divider()

# =====================================================
# RESEARCH SUMMARY
# =====================================================

st.subheader("Research Summary")

st.info(
"""
This application implements the final CatBoost machine learning
model developed for diabetes risk prediction using the
Behavioral Risk Factor Surveillance System (BRFSS) 2015 dataset.

The research evaluates predictive performance using
nested cross-validation and multiple evaluation metrics,
followed by explainability (SHAP), fairness analysis,
calibration assessment, and threshold optimization
to provide a comprehensive evaluation of the proposed model.
"""
)

st.divider()

# =====================================================
# NAVIGATION
# =====================================================

st.subheader("Application Modules")

module1, module2 = st.columns(2)

with module1:

    st.markdown("""
- 🩺 Prediction
- 📊 Model Performance
- 🧠 SHAP Explainability
- ⚖️ Fairness Analysis
""")

with module2:

    st.markdown("""
- 📉 Calibration
- 🎯 Threshold Analysis
- 📖 About Research
- 👨‍💻 About Developer
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
"""
Diabetes Risk Prediction System

CatBoost Machine Learning Model

BRFSS 2015 Dataset

Version 1.0.0
"""
)