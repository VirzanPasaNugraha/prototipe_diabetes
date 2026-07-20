"""
SHAP Explainability
"""

import streamlit as st
import pandas as pd

from utils.asset_loader import (
    SHAP_SUMMARY,
    SHAP_BAR,
)

st.set_page_config(
    page_title="SHAP Explainability",
    page_icon="🧠",
    layout="wide"
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("🧠 SHAP Explainability")

st.caption(
    "Feature importance analysis using SHAP values from the final CatBoost model."
)

st.divider()

# =====================================================
# TOP FEATURES
# =====================================================

st.subheader("Top Important Features")

features = pd.DataFrame({

    "Feature": [

        "GenHlth",
        "BMI",
        "Age",
        "HighChol",
        "HighBP",
        "PhysHlth",
        "DiffWalk",
        "Income",
        "PhysActivity",
        "HeartDiseaseorAttack"

    ],

    "Importance": [

        0.194,
        0.163,
        0.151,
        0.112,
        0.104,
        0.083,
        0.067,
        0.052,
        0.041,
        0.033

    ]

})

left, right = st.columns([1, 1])

with left:

    st.dataframe(
        features,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.metric(
        "Most Important Feature",
        "GenHlth"
    )

    st.metric(
        "Second Feature",
        "BMI"
    )

    st.metric(
        "Third Feature",
        "Age"
    )

st.divider()

# =====================================================
# FEATURE IMPORTANCE CHART
# =====================================================

st.subheader("Feature Importance")

chart = features.set_index("Feature")

st.bar_chart(chart)

st.divider()

# =====================================================
# SHAP VISUALIZATION
# =====================================================

st.subheader("SHAP Visualizations")

tab1, tab2 = st.tabs([
    "📊 SHAP Summary Plot",
    "📈 SHAP Bar Plot",
])

# =====================================================
# TAB 1
# =====================================================

with tab1:

    col1, col2 = st.columns([2, 1])

    with col1:

        st.image(
            SHAP_SUMMARY,
            caption="SHAP Summary Plot",
            use_column_width=True,
        )

    with col2:

        st.markdown("### Interpretation")

        st.write(
            """
            The SHAP Summary Plot visualizes the impact of
            every feature on diabetes prediction across all
            observations.

            Features appearing at the top have the greatest
            overall influence on the CatBoost model.

            Each point represents one observation, while
            color indicates the feature value.
            """
        )

# =====================================================
# TAB 2
# =====================================================

with tab2:

    col1, col2 = st.columns([2, 1])

    with col1:

        st.image(
            SHAP_BAR,
            caption="SHAP Feature Importance",
            use_column_width=True,
        )

    with col2:

        st.markdown("### Interpretation")

        st.write(
            """
            The SHAP Bar Plot summarizes the average absolute
            SHAP value for each feature.

            Larger SHAP values indicate stronger influence on
            diabetes risk prediction.

            This visualization provides an overall ranking of
            feature importance.
            """
        )

st.divider()

# =====================================================
# FEATURE INTERPRETATION
# =====================================================

st.subheader("Feature Interpretation")

for _, row in features.iterrows():

    with st.expander(f"📌 {row['Feature']}"):

        st.markdown(
            f"""
**Importance Score**

**{row['Importance']:.3f}**

This feature contributes significantly to the final
CatBoost prediction according to the SHAP explainability
analysis.
"""
        )

st.divider()

# =====================================================
# SUMMARY
# =====================================================

st.success(
"""
### Top Five Most Influential Features

1. GenHlth
2. BMI
3. Age
4. HighChol
5. HighBP
"""
)

st.info(
"""
**Interpretation**

The SHAP analysis indicates that general health condition
(GenHlth), body mass index (BMI), age, cholesterol level,
and hypertension status are the most influential predictors
of diabetes in the final CatBoost model.
"""
)

st.caption(
    "SHAP explainability corresponds to the final CatBoost model used in this research."
)