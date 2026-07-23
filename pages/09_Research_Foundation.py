"""
Research Foundation
"""

import streamlit as st
import pandas as pd

from utils.asset_loader import (
    CLASS_DISTRIBUTION,
    HIGHBP_VS_DIABETES,
    HIGHCHOL_VS_DIABETES,
    FEATURE_IMPORTANCE,
    RELIABILITY_LOGISTIC,
    RELIABILITY_RANDOM_FOREST,
    RELIABILITY_XGBOOST,
)

st.set_page_config(
    page_title="Research Foundation",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Research Foundation")

st.caption(
    "Theoretical background, literature foundation, and scientific "
    "methodology underlying the diabetes risk prediction research."
)

st.divider()

# ======================================================
# RESEARCH BACKGROUND
# ======================================================

st.subheader("Research Background")

st.write(
    """
    Diabetes remains one of the fastest-growing public health
    challenges worldwide. According to the International Diabetes
    Federation (IDF) Diabetes Atlas, 11th Edition (2025), an
    estimated 589 million adults aged 20–79 were living with
    diabetes in 2024, a figure projected to rise to 853 million
    by 2050. The World Health Organization further reports that
    global diabetes prevalence among adults nearly doubled from
    7% in 1990 to 14% in 2022.

    A substantial proportion of cases remain undiagnosed, with
    IDF estimating that around 43% of adults living with diabetes
    are unaware of their condition. Early identification of
    at-risk individuals is therefore essential to enable timely
    intervention, lifestyle modification, and reduction of
    long-term complications.

    This research is motivated by the need for a diabetes risk
    prediction approach that is not only accurate, but also
    interpretable, fair across demographic groups, and produces
    reliable probability estimates suitable for decision support.
    """
)

b1, b2, b3 = st.columns(3)

with b1:
    st.metric(
        "Global Adults with Diabetes (2024)",
        "589 Million",
        help="11.1% of adults aged 20–79, IDF Diabetes Atlas 11th Edition (2025)"
    )

with b2:
    st.metric(
        "Projected by 2050",
        "853 Million",
        help="IDF Diabetes Atlas 11th Edition (2025)"
    )

with b3:
    st.metric(
        "Estimated Undiagnosed",
        "~43%",
        help="IDF Diabetes Atlas 11th Edition (2025)"
    )

st.divider()

# ======================================================
# PROBLEM STATEMENT
# ======================================================

st.subheader("Problem Statement")

st.info(
    """
    Most machine learning studies on diabetes risk prediction
    emphasize predictive accuracy alone, while paying limited
    attention to interpretability, fairness across population
    subgroups, and the reliability of predicted probabilities.
    In a healthcare context, these limitations restrict the
    trustworthiness and practical adoption of predictive models.
    """
)

st.markdown(
    """
    **Research Questions**

    1. How accurately can machine learning models predict
       diabetes risk using self-reported behavioral and health
       indicators from the BRFSS 2015 dataset?
    2. Which features contribute most strongly to the model's
       predictions, and are these contributions clinically
       plausible?
    3. Does the model perform consistently across demographic
       subgroups such as sex, age, education, and income?
    4. How well do the model's predicted probabilities reflect
       actual observed outcomes?
    5. How can the classification threshold be adjusted to
       balance sensitivity and specificity for different
       screening scenarios?
    """
)

st.divider()

# ======================================================
# RESEARCH OBJECTIVES
# ======================================================

st.subheader("Research Objectives")

st.success(
    """
    - Develop and compare multiple machine learning models for
    binary diabetes risk classification using BRFSS 2015 data.

    - Select the best-performing model through nested
    cross-validation and multi-metric evaluation.

    - Explain model predictions using SHapley Additive
    exPlanations (SHAP) to ensure interpretability.

    - Evaluate fairness of predictions across demographic
    subgroups (sex, age, education, income).

    - Assess and interpret the calibration quality of predicted
    probabilities.

    - Analyze decision thresholds to support flexible,
    context-specific screening strategies.
    """
)

st.divider()

# ======================================================
# THEORETICAL FOUNDATION
# ======================================================

st.subheader("Theoretical Foundation")

st.write(
    """
    The research is grounded in supervised binary classification
    theory, combined with four complementary evaluation
    perspectives: discriminative performance, explainability,
    algorithmic fairness, and probabilistic calibration. Each
    perspective draws on an established body of literature.
    """
)

theory = pd.DataFrame({

    "Concept": [
        "Gradient Boosting on Decision Trees",
        "Explainable AI (SHAP)",
        "Algorithmic Fairness",
        "Probability Calibration",
        "Nested Cross-Validation",
        "Behavioral Risk Factor Surveillance",
    ],

    "Theoretical Basis": [
        "Prokhorenkova et al. (2018) — CatBoost: unbiased boosting with categorical features",
        "Lundberg & Lee (2017) — Shapley values from cooperative game theory",
        "Group-wise recall / false positive rate parity across sensitive attributes",
        "Brier (1950); Niculescu-Mizil & Caruana (2005) — reliability of predicted probabilities",
        "Cawley & Talbot (2010) — avoiding selection bias in performance evaluation",
        "CDC BRFSS methodology — annual telephone health survey of U.S. adults",
    ]

})

st.dataframe(
    theory,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ======================================================
# RESEARCH GAP & CONTRIBUTION
# ======================================================

st.subheader("Research Gap and Contribution")

left, right = st.columns(2)

with left:
    st.markdown("### Research Gap")
    st.write(
        """
        Existing BRFSS-based diabetes prediction studies
        predominantly report accuracy, ROC-AUC, or F1 Score in
        isolation. Explainability, subgroup fairness, and
        calibration are rarely evaluated together within a
        single, reproducible pipeline — despite each being
        essential for responsible deployment of predictive
        models in healthcare settings.
        """
    )

with right:
    st.markdown("### Contribution")
    st.write(
        """
        This research proposes a comprehensive evaluation
        framework that unifies predictive performance,
        SHAP-based explainability, subgroup fairness analysis,
        probability calibration, and threshold optimization into
        a single methodology — implemented end-to-end as an
        interactive research prototype (SIDIAS).
        """
    )

st.divider()

# ======================================================
# DATASET FOUNDATION
# ======================================================

st.subheader("Dataset Foundation")

d1, d2, d3, d4 = st.columns(4)

with d1:
    st.metric("Source", "BRFSS 2015")

with d2:
    st.metric("Samples", "69,057")

with d3:
    st.metric("Features", "21")

with d4:
    st.metric("Target", "Diabetes_binary")

col1, col2 = st.columns([2, 1])

with col1:
    st.image(
        CLASS_DISTRIBUTION,
        caption="Class Distribution of the Target Variable",
        use_column_width=True
    )

with col2:
    st.markdown("### Interpretation")
    st.write(
        """
        The dataset used in this research was balanced prior to
        modeling, providing an equal representation of diabetic
        and non-diabetic cases.

        A balanced class distribution reduces bias toward the
        majority class and supports more reliable estimation of
        recall, which is critical for a diabetes screening
        context.
        """
    )

st.divider()

# ======================================================
# EXPLORATORY RISK FACTOR FOUNDATION
# ======================================================

st.subheader("Exploratory Risk Factor Foundation")

st.caption(
    "Bivariate relationships between key clinical indicators and diabetes status, "
    "forming the empirical basis for feature selection."
)

exp_tab1, exp_tab2 = st.tabs(
    [
        "🩸 High Blood Pressure",
        "🧪 High Cholesterol",
    ]
)

with exp_tab1:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            HIGHBP_VS_DIABETES,
            caption="High Blood Pressure vs Diabetes Status",
            use_column_width=True
        )

    with col2:
        st.markdown("### Interpretation")
        st.write(
            """
            Individuals with high blood pressure show a
            markedly higher proportion of diabetes cases
            compared to those without.

            This supports the well-established clinical
            association between hypertension and type 2
            diabetes, reinforcing HighBP as a meaningful
            predictive feature.
            """
        )

with exp_tab2:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            HIGHCHOL_VS_DIABETES,
            caption="High Cholesterol vs Diabetes Status",
            use_column_width=True
        )

    with col2:
        st.markdown("### Interpretation")
        st.write(
            """
            Individuals with high cholesterol are more likely
            to be diagnosed with diabetes than individuals with
            normal cholesterol levels.

            This aligns with the known clustering of metabolic
            risk factors, motivating the inclusion of
            cholesterol status alongside BMI and blood pressure.
            """
        )

st.divider()

# ======================================================
# METHODOLOGICAL FRAMEWORK
# ======================================================

st.subheader("Methodological Framework")

st.write(
    """
    The research follows a structured, reproducible scientific
    workflow, from problem formulation through to interactive
    prototype deployment.
    """
)

st.code(
"""
Research Problem & Literature Review

   │

Data Collection (BRFSS 2015)

   │

Data Cleaning & Validation

   │

Exploratory Data Analysis (EDA)

   │

Feature Engineering & Multicollinearity Check (VIF)

   │

Nested Cross Validation (10x5)

   │

Hyperparameter Optimization (GridSearchCV)

   │

Baseline Model Training
(Logistic Regression, Random Forest, XGBoost, CatBoost)

   │

Multi-Metric Model Evaluation

   │

Best Model Selection (CatBoost)

   │

Explainability Analysis (SHAP)

   │

Fairness Evaluation Across Subgroups

   │

Calibration & Reliability Assessment

   │

Threshold Optimization

   │

Interactive Research Prototype (SIDIAS / Streamlit)
""",
language="text"
)

st.divider()

# ======================================================
# BASELINE MODEL COMPARISON FOUNDATION
# ======================================================

st.subheader("Baseline Model Comparison Foundation")

st.write(
    """
    Four candidate models were trained and evaluated under the
    same nested cross-validation protocol. CatBoost was selected
    as the final model based on its discrimination ability,
    recall balance, and probability calibration quality.
    """
)

models_table = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost",
        "CatBoost",
    ],

    "Role": [
        "Linear baseline",
        "Ensemble baseline",
        "Gradient boosting baseline",
        "Selected final model",
    ],

    "Brier Score": [
        0.1723,
        0.1713,
        0.1685,
        0.1684,
    ]

})

t1, t2 = st.columns([1, 1])

with t1:
    st.dataframe(
        models_table,
        use_container_width=True,
        hide_index=True
    )

with t2:
    st.bar_chart(
        models_table.set_index("Model")["Brier Score"]
    )

st.caption(
    "Lower Brier Score indicates better-calibrated probability estimates. "
    "Full comparative metrics are reported in Table III of the published manuscript."
)

st.markdown("#### Reliability of Baseline Models")

rel_tab1, rel_tab2, rel_tab3 = st.tabs(
    [
        "📐 Logistic Regression",
        "🌲 Random Forest",
        "🚀 XGBoost",
    ]
)

with rel_tab1:
    st.image(
        RELIABILITY_LOGISTIC,
        caption="Logistic Regression Reliability Diagram",
        use_column_width=True
    )
    st.write(
        """
        As a linear probabilistic classifier, Logistic
        Regression provides a reference point for calibration
        behavior against which the more complex ensemble
        models are compared.
        """
    )

with rel_tab2:
    st.image(
        RELIABILITY_RANDOM_FOREST,
        caption="Random Forest Reliability Diagram",
        use_column_width=True
    )
    st.write(
        """
        Tree-based ensembles such as Random Forest can produce
        probability estimates that deviate from the diagonal
        reference line, motivating explicit calibration
        assessment rather than relying on raw model output.
        """
    )

with rel_tab3:
    st.image(
        RELIABILITY_XGBOOST,
        caption="XGBoost Reliability Diagram",
        use_column_width=True
    )
    st.write(
        """
        XGBoost achieved a Brier Score close to CatBoost,
        indicating comparably strong calibration among the
        boosting-based models evaluated in this research.
        """
    )

st.divider()

# ======================================================
# METHODOLOGICAL TRIANGULATION
# ======================================================

st.subheader("Methodological Triangulation of Feature Relevance")

col1, col2 = st.columns([2, 1])

with col1:
    st.image(
        FEATURE_IMPORTANCE,
        caption="Permutation Importance of Model Features",
        use_column_width=True
    )

with col2:
    st.markdown("### Interpretation")
    st.write(
        """
        Permutation importance provides a model-agnostic
        cross-check for the SHAP-based explainability results
        presented on the SHAP Explainability page.

        Consistency between permutation importance and SHAP
        rankings — particularly for General Health, BMI, Age,
        High Cholesterol, and High Blood Pressure — strengthens
        confidence that these features carry genuine predictive
        signal rather than model-specific artifacts.
        """
    )

st.divider()

# ======================================================
# PUBLICATION PROVENANCE
# ======================================================

st.subheader("Publication Provenance")

st.markdown(
    """
    This research prototype is the official implementation of a
    peer-reviewed study published in the **Journal of Applied
    Informatics and Computing (JAIC)**, Politeknik Negeri Batam
    (Polibatam), e-ISSN: 2548-6861.

    🔗 [Comprehensive Diabetes Risk Prediction Using BRFSS Data: Performance, Explainability, Fairness, and Calibration](https://www.researchgate.net/publication/408415092_Comprehensive_Diabetes_Risk_Prediction_Using_BRFSS_Data_Performance_Explainability_Fairness_and_Calibration)
    """
)

st.caption(
    "Authors: Virzan Pasa Nugraha, Agung Febrian, Fidi Supriadi — "
    "Informatika, Universitas Sebelas April Sumedang"
)

st.divider()

# ======================================================
# LIMITATIONS & FUTURE RESEARCH
# ======================================================

st.subheader("Limitations and Future Research Directions")

st.warning(
    """
    - BRFSS 2015 relies on self-reported survey responses,
    which may be subject to recall and social desirability bias.

    - The dataset is cross-sectional; no temporal or
    longitudinal validation was performed.

    - The model was trained and evaluated on a single dataset,
    and external validation on independent populations is
    still required.

    - Fairness evaluation revealed disparities across age and
    education subgroups that warrant further investigation and
    mitigation strategies.
    """
)

st.write(
    """
    Future research directions include external validation on
    independent or more recent BRFSS survey years, exploration
    of fairness-aware training techniques, and prospective
    evaluation of the threshold-based decision support approach
    in a real screening context.
    """
)

st.divider()

# ======================================================
# BIBLIOGRAPHY
# ======================================================

st.subheader("Bibliography")

st.markdown(
    """
    1. Nugraha, V. P., & Febrian, A. (2026). *Comprehensive
       Diabetes Risk Prediction Using BRFSS Data: Performance,
       Explainability, Fairness, and Calibration*. Journal of
       Applied Informatics and Computing (JAIC), Politeknik
       Negeri Batam.
    2. Centers for Disease Control and Prevention (CDC). *Behavioral
       Risk Factor Surveillance System (BRFSS) 2015 Codebook*.
    3. Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V.,
       & Gulin, A. (2018). *CatBoost: Unbiased Boosting with
       Categorical Features*. NeurIPS.
    4. Lundberg, S. M., & Lee, S.-I. (2017). *A Unified Approach to
       Interpreting Model Predictions*. NeurIPS.
    5. Niculescu-Mizil, A., & Caruana, R. (2005). *Predicting Good
       Probabilities with Supervised Learning*. ICML.
    6. Brier, G. W. (1950). *Verification of Forecasts Expressed in
       Terms of Probability*. Monthly Weather Review.
    7. Cawley, G. C., & Talbot, N. L. C. (2010). *On Over-fitting in
       Model Selection and Subsequent Selection Bias in Performance
       Evaluation*. Journal of Machine Learning Research.
    8. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning
       in Python*. Journal of Machine Learning Research.
    9. International Diabetes Federation (2025). *IDF Diabetes
       Atlas*, 11th Edition.
    10. World Health Organization (2024). *Diabetes Fact Sheet*.
    """
)

st.divider()

# ======================================================
# FOOTER
# ======================================================

st.caption(
    """
    Research Foundation dashboard —
    theoretical background for the SIDIAS diabetes risk
    prediction system.

    Diabetes Risk Prediction System |
    CatBoost |
    BRFSS 2015 |
    Explainable AI Research
    """
)