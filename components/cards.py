"""
Reusable Cards
Native Streamlit Components
"""

import streamlit as st


def metric_card(icon, title, value, description):
    """
    Metric Card
    """

    with st.container(border=True):

        col1, col2 = st.columns([1, 4])

        with col1:
            st.markdown(
                f"""
                <div style="
                    font-size:34px;
                    text-align:center;
                    margin-top:8px;
                ">
                    {icon}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:

            st.caption(title)

            st.markdown(
                f"""
                <div style="
                    font-size:28px;
                    font-weight:700;
                    color:#2563EB;
                ">
                    {value}
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.caption(description)


def info_card(title, content, icon="ℹ️"):
    """
    Information Card
    """

    with st.container(border=True):

        st.subheader(f"{icon} {title}")

        st.write(content)


def prediction_card(risk, probability):
    """
    Prediction Result Card
    """

    with st.container(border=True):

        color = "🟢"

        if probability >= 0.5:
            color = "🔴"

        st.subheader(f"{color} {risk}")

        st.metric(
            "Probability",
            f"{probability:.1%}"
        )

        st.progress(float(probability))


def feature_card(feature, value):
    """
    Feature Importance Card
    """

    with st.container(border=True):

        st.caption("Feature")

        st.markdown(
            f"### {feature}"
        )

        st.metric(
            "Value",
            value
        )


def developer_card(name, role):
    """
    Developer Card
    """

    with st.container(border=True):

        st.markdown("# 👨‍💻")

        st.subheader(name)

        st.caption(role)