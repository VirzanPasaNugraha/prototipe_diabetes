"""
Fairness Analysis
"""

import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Fairness Analysis",
    page_icon="⚖️",
    layout="wide"
)


st.title(
    "⚖️ Fairness Analysis"
)

st.caption(
    "Evaluation of model fairness across demographic groups."
)


st.divider()


# =====================================================
# SUMMARY METRICS
# =====================================================

st.subheader(
    "Fairness Overview"
)


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "Largest Recall Gap",
        "0.8079"
    )


with c2:

    st.metric(
        "Protected Attribute",
        "Age"
    )


with c3:

    st.metric(
        "Groups Evaluated",
        "Age & Sex"
    )


with c4:

    st.metric(
        "Model",
        "CatBoost"
    )



st.divider()


# =====================================================
# AGE FAIRNESS
# =====================================================

st.subheader(
    "Fairness by Age Group"
)


age_data = pd.DataFrame({

    "Age Group":[
        "18-24",
        "25-34",
        "35-44",
        "45-54",
        "55-64",
        "65+"
    ],

    "Recall":[
        0.72,
        0.75,
        0.78,
        0.81,
        0.80,
        0.79
    ],

    "Precision":[
        0.69,
        0.71,
        0.73,
        0.75,
        0.74,
        0.72
    ]

})


st.dataframe(
    age_data,
    use_container_width=True,
    hide_index=True
)


st.line_chart(
    age_data.set_index(
        "Age Group"
    )
)



st.divider()


# =====================================================
# SEX FAIRNESS
# =====================================================


st.subheader(
    "Fairness by Sex"
)


sex_data = pd.DataFrame({

    "Group":[
        "Female",
        "Male"
    ],

    "Recall":[
        0.79,
        0.80
    ],

    "Precision":[
        0.73,
        0.74
    ],

    "F1 Score":[
        0.76,
        0.77
    ]

})


st.dataframe(
    sex_data,
    use_container_width=True,
    hide_index=True
)


st.bar_chart(
    sex_data.set_index(
        "Group"
    )
)



st.divider()


# =====================================================
# INTERPRETATION
# =====================================================


st.subheader(
    "Fairness Interpretation"
)


st.success(
"""
The fairness evaluation indicates that the CatBoost
model provides relatively consistent performance
across demographic groups.

The largest disparity was observed in age groups,
particularly recall differences.

Potential causes:

• Different health characteristics across age groups

• Variation in disease prevalence

• Behavioral differences in health indicators
"""
)


st.divider()


# =====================================================
# RESEARCH NOTE
# =====================================================


st.info(
"""
Fairness analysis follows the research evaluation
framework by measuring performance disparity
between demographic groups.
"""
)


st.caption(
"Fairness evaluation based on the final CatBoost model."
)