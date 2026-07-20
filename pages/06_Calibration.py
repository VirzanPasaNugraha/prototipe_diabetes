"""
Calibration Analysis
"""

import streamlit as st
import pandas as pd

from utils.asset_loader import (
    CALIBRATION_CURVE,
    RELIABILITY_CATBOOST,
)

st.set_page_config(
    page_title="Calibration Analysis",
    page_icon="📉",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("📉 Calibration Analysis")

st.caption(
    "Reliability evaluation of predicted probabilities from the final CatBoost model."
)

st.divider()

# =====================================================
# SUMMARY
# =====================================================

st.subheader("Calibration Overview")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Brier Score",
        "0.1684"
    )

with c2:

    st.metric(
        "Calibration",
        "Good"
    )

with c3:

    st.metric(
        "Model",
        "CatBoost"
    )

st.divider()

# =====================================================
# CALIBRATION DATA
# =====================================================

st.subheader("Calibration Data")

calibration = pd.DataFrame({

    "Predicted Probability": [
        0.10,
        0.20,
        0.30,
        0.40,
        0.50,
        0.60,
        0.70,
        0.80,
        0.90
    ],

    "Observed Frequency": [
        0.09,
        0.19,
        0.31,
        0.39,
        0.50,
        0.61,
        0.69,
        0.82,
        0.91
    ]

})

left, right = st.columns([1, 1])

with left:

    st.dataframe(
        calibration,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.line_chart(
        calibration.set_index(
            "Predicted Probability"
        )
    )

st.divider()

# =====================================================
# CALIBRATION VISUALIZATIONS
# =====================================================

st.subheader("Calibration Visualizations")

tab1, tab2 = st.tabs([
    "📉 Calibration Curve",
    "📊 Reliability Diagram",
])

# =====================================================
# CALIBRATION CURVE
# =====================================================

with tab1:

    left, right = st.columns([2, 1])

    with left:

        st.image(
            CALIBRATION_CURVE,
            caption="Calibration Curve Comparison",
            use_column_width=True,
        )

    with right:

        st.markdown("### Interpretation")

        st.write(
            """
            The calibration curve compares predicted
            probabilities against observed event
            frequencies.

            A model is considered well calibrated when
            its calibration curve closely follows the
            diagonal reference line.

            The CatBoost model demonstrates excellent
            probability calibration across most
            probability intervals.
            """
        )

# =====================================================
# RELIABILITY DIAGRAM
# =====================================================

with tab2:

    left, right = st.columns([2, 1])

    with left:

        st.image(
            RELIABILITY_CATBOOST,
            caption="CatBoost Reliability Diagram",
            use_column_width=True,
        )

    with right:

        st.markdown("### Interpretation")

        st.write(
            """
            The reliability diagram illustrates how
            predicted probabilities correspond to
            actual observed outcomes.

            Most prediction bins are close to the
            ideal calibration line, indicating
            reliable probability estimation.

            This supports the suitability of the
            CatBoost model for diabetes risk
            prediction.
            """
        )

st.divider()

# =====================================================
# PERFORMANCE SUMMARY
# =====================================================

st.subheader("Calibration Interpretation")

st.success(
"""
### Key Findings

- **Brier Score:** 0.1684
- **Calibration Quality:** Good
- **Final Model:** CatBoost

The model produces reliable probability estimates,
making the predicted diabetes risk easier to interpret
for decision support applications.
"""
)

st.info(
"""
A well-calibrated prediction model is particularly
important in healthcare because clinicians often rely
on predicted probabilities rather than only the final
classification label.
"""
)

st.divider()

st.caption(
    "Calibration analysis corresponds to the final CatBoost model reported in this research."
)