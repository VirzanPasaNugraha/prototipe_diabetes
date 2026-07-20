"""
Sidebar Component
"""

import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            ## 🩺

            # Diabetes AI

            ---
            """
        )


        st.markdown(
            """
            Navigate through:

            🏠 Dashboard

            🩺 Prediction

            📊 Performance

            🧠 Explainability

            ⚖ Fairness

            📈 Calibration

            """
        )


        st.divider()


        st.caption(
            "Version 1.0.0 | CatBoost Model"
        )