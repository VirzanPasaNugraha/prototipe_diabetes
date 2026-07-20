"""
Application Header
"""

import streamlit as st


def render_header():

    st.markdown(
        """
        <div style="
            padding:20px 0;
        ">

        <h1 style="
            font-size:42px;
            color:#0F172A;
        ">
        🩺 Diabetes Risk Prediction System
        </h1>


        <p style="
            font-size:20px;
            color:#475569;
        ">
        Explainable AI Platform for Diabetes Risk Assessment
        </p>


        </div>
        """,
        unsafe_allow_html=True
    )