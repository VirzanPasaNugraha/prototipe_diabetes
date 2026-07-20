"""
Main Application
"""

import streamlit as st


from styles.theme import apply_theme

from components.sidebar import render_sidebar
from components.header import render_header
from components.footer import render_footer
from components.cards import metric_card



st.set_page_config(

    page_title="Diabetes Risk Prediction System",

    page_icon="🩺",

    layout="wide"

)



apply_theme()


render_sidebar()


render_header()



st.divider()



st.subheader(
    "Research Overview"
)



col1,col2,col3,col4 = st.columns(4)



with col1:

    metric_card(
        "🧠",
        "Model",
        "CatBoost",
        "Best ML Classifier"
    )


with col2:

    metric_card(
        "📈",
        "ROC-AUC",
        "0.8267",
        "Validation Performance"
    )


with col3:

    metric_card(
        "📂",
        "Dataset",
        "BRFSS",
        "2015 Health Indicators"
    )


with col4:

    metric_card(
        "🔢",
        "Features",
        "21",
        "Predictor Variables"
    )



st.divider()



left,right = st.columns(2)



with left:

    st.subheader(
        "Research Focus"
    )


    st.write(
        """
        This system implements an explainable
        machine learning framework for diabetes
        risk prediction.

        Evaluated aspects:

        - Performance
        - Explainability
        - Fairness
        - Calibration
        """
    )



with right:

    st.subheader(
        "Technology Stack"
    )


    st.write(
        """
        🐍 Python

        🤖 CatBoost

        📊 Scikit-Learn

        🧠 SHAP

        🎨 Streamlit

        📁 BRFSS Dataset
        """
    )



st.success(
    """
    Navigate to Prediction page
    to analyze diabetes risk.
    """
)


render_footer()