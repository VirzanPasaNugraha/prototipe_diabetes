"""
Model Performance
"""

import streamlit as st

from utils.asset_loader import (
    ROC_CURVE,
    PR_CURVE,
    CONFUSION_MATRIX,
    CALIBRATION_CURVE,
)


st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)


# ===================================================
# HEADER
# ===================================================

st.title("📈 Model Performance")

st.caption(
    "Performance evaluation of the final CatBoost model."
)

st.divider()



# ===================================================
# PERFORMANCE METRICS
# ===================================================

st.subheader("Overall Performance")


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "Accuracy",
        "0.7495"
    )


with c2:

    st.metric(
        "ROC-AUC",
        "0.8267"
    )


with c3:

    st.metric(
        "PR-AUC",
        "0.8073"
    )


with c4:

    st.metric(
        "MCC",
        "0.5003"
    )



c5, c6, c7, c8 = st.columns(4)


with c5:

    st.metric(
        "Precision",
        "0.7320"
    )


with c6:

    st.metric(
        "Recall",
        "0.8000"
    )


with c7:

    st.metric(
        "F1 Score",
        "0.7645"
    )


with c8:

    st.metric(
        "Brier Score",
        "0.1684"
    )



st.divider()



# ===================================================
# MODEL INFORMATION
# ===================================================

left, right = st.columns(2)



with left:

    with st.container(border=True):

        st.subheader("🤖 Model")

        st.write(
            """
            - Algorithm : CatBoostClassifier

            - Dataset : BRFSS 2015

            - Features : 21

            - Cross Validation : Nested Cross Validation

            - Hyperparameter Tuning : GridSearchCV
            """
        )



with right:

    with st.container(border=True):

        st.subheader("⚙️ Training Summary")

        st.write(
            """
            - Iterations : 200

            - Learning Rate : 0.05

            - Depth : 6

            - L2 Leaf Regularization : 3

            - Random State : 42
            """
        )



st.divider()



# ===================================================
# PERFORMANCE SUMMARY
# ===================================================

st.subheader("Performance Summary")


with st.container(border=True):

    st.success(
        """
        The CatBoost model achieved the best overall performance
        among evaluated machine learning models.

        Key strengths:

        • High ROC-AUC (0.8267)

        • High Recall (0.8000)

        • Good probability calibration

        • Balanced classification performance

        • Reliable diabetes risk prediction
        """
    )



st.divider()



# ===================================================
# PERFORMANCE VISUALIZATION
# ===================================================

st.subheader(
    "Performance Visualizations"
)



tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📈 ROC Curve",
        "📊 PR Curve",
        "🧩 Confusion Matrix",
        "🎯 Calibration Curve"
    ]
)



# ===================================================
# ROC CURVE
# ===================================================

with tab1:


    col1, col2 = st.columns(
        [2,1]
    )


    with col1:

       st.image(
    ROC_CURVE,
    caption="ROC Curve Comparison",
    use_column_width=True
)


    with col2:

        st.subheader(
            "Interpretation"
        )

        st.write(
            """
            ROC Curve evaluates the discrimination
            ability of the model.

            CatBoost achieved:

            **ROC-AUC = 0.8267**

            indicating strong capability
            to distinguish diabetes and
            non-diabetes classes.
            """
        )



# ===================================================
# PR CURVE
# ===================================================

with tab2:


    col1, col2 = st.columns(
        [2,1]
    )


    with col1:

        st.image(
            PR_CURVE,
            caption="Precision Recall Curve",
            use_column_width=True
        )


    with col2:

        st.subheader(
            "Interpretation"
        )

        st.write(
            """
            Precision-Recall Curve focuses on
            positive class prediction.

            This metric is important in
            healthcare because identifying
            diabetes cases correctly is critical.
            """
        )



# ===================================================
# CONFUSION MATRIX
# ===================================================

with tab3:


    col1, col2 = st.columns(
        [2,1]
    )


    with col1:

        st.image(
            CONFUSION_MATRIX,
            caption="CatBoost Confusion Matrix",
            use_column_width=True
        )


    with col2:

        st.subheader(
            "Interpretation"
        )

        st.write(
            """
            Confusion Matrix summarizes:

            ✔ True Positive

            ✔ True Negative

            ✔ False Positive

            ✔ False Negative

            The model prioritizes higher
            recall to reduce missed cases.
            """
        )



# ===================================================
# CALIBRATION
# ===================================================

with tab4:


    col1, col2 = st.columns(
        [2,1]
    )


    with col1:

        st.image(
            CALIBRATION_CURVE,
            caption="CatBoost Calibration Curve",
            use_column_width=True
        )


    with col2:

        st.subheader(
            "Interpretation"
        )

        st.write(
            """
            Calibration evaluates whether
            predicted probabilities represent
            actual observed outcomes.

            CatBoost achieved:

            **Brier Score = 0.1684**

            showing reliable probability estimation.
            """
        )



st.divider()



# ===================================================
# FOOTER NOTE
# ===================================================

st.caption(
    """
    Performance values correspond to the final CatBoost
    model reported in the research manuscript.
    """
)