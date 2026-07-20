"""
Threshold Analysis
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Threshold Analysis",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Threshold Analysis")

st.caption(
    "Evaluate prediction performance under different probability thresholds."
)

st.divider()

# =====================================================
# THRESHOLD
# =====================================================

st.subheader("Threshold Selection")

threshold = st.slider(
    "Decision Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.50,
    step=0.05
)

st.divider()

# =====================================================
# METRICS
# =====================================================

if threshold <= 0.40:

    metrics = {

        "Accuracy":"0.7194",

        "Recall":"0.8792",

        "Precision":"0.6945",

        "F1":"0.7760",

        "Specificity":"0.6035",

        "MCC":"0.4876",

        "False Positive":"2688",

        "False Negative":"848"

    }

else:

    metrics = {

        "Accuracy":"0.7485",

        "Recall":"0.8000",

        "Precision":"0.7320",

        "F1":"0.7645",

        "Specificity":"0.6954",

        "MCC":"0.4983",

        "False Positive":"2069",

        "False Negative":"1405"

    }

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Accuracy", metrics["Accuracy"])

with c2:
    st.metric("Recall", metrics["Recall"])

with c3:
    st.metric("Precision", metrics["Precision"])

with c4:
    st.metric("F1 Score", metrics["F1"])

c5,c6,c7,c8 = st.columns(4)

with c5:
    st.metric("Specificity", metrics["Specificity"])

with c6:
    st.metric("MCC", metrics["MCC"])

with c7:
    st.metric("False Positive", metrics["False Positive"])

with c8:
    st.metric("False Negative", metrics["False Negative"])

st.divider()

# =====================================================
# COMPARISON
# =====================================================

st.subheader("Threshold Comparison")

comparison = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Recall",
        "Precision",
        "F1",
        "Specificity",
        "MCC"
    ],

    "Threshold 0.40":[
        0.7194,
        0.8792,
        0.6945,
        0.7760,
        0.6035,
        0.4876
    ],

    "Threshold 0.50":[
        0.7485,
        0.8000,
        0.7320,
        0.7645,
        0.6954,
        0.4983
    ]

})

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.bar_chart(
    comparison.set_index("Metric")
)

st.divider()

# =====================================================
# INTERPRETATION
# =====================================================

st.subheader("Interpretation")

if threshold <= 0.40:

    st.warning(
"""
Threshold 0.40 prioritizes **higher recall**.

Advantages

• Detects more diabetes cases

• Reduces False Negatives

Disadvantages

• Increases False Positives

Suitable for screening applications.
"""
    )

else:

    st.success(
"""
Threshold 0.50 provides a balanced trade-off.

Advantages

• Better overall accuracy

• Better specificity

• Higher MCC

Suitable for general prediction systems.
"""
    )

st.divider()

st.subheader("Recommendation")

st.info(
"""
Research Recommendation

• Threshold **0.50** → balanced prediction.

• Threshold **0.40** → screening scenarios where missing positive cases is more critical.
"""
)

st.caption(
"Threshold analysis based on the final CatBoost model."
)