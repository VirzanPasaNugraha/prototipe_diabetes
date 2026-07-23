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
    st.metric("Final Records", "69,057")

with d3:
    st.metric("Features", "21")

with d4:
    st.metric("Target", "Diabetes_binary")

st.write(
    """
    The BRFSS dataset initially consisted of 70,692 records and
    22 variables, with no missing values found. During
    preprocessing, 1,635 duplicate rows were identified and
    removed, resulting in a final dataset of 69,057 records
    with 21 predictor variables.
    """
)

dataset_table = pd.DataFrame({

    "Characteristic": [
        "Initial Records",
        "Duplicate Rows Removed",
        "Final Records",
        "Missing Values",
        "Mean BMI",
        "Mean GenHlth",
        "HighBP Proportion",
        "HighChol Proportion",
        "Diabetes Cases",
        "Non-Diabetes Cases",
    ],

    "Value": [
        "70,692",
        "1,635",
        "69,057",
        "0",
        "29.86",
        "2.84",
        "0.5635",
        "0.5257",
        "35,097 (50.82%)",
        "33,960 (49.18%)",
    ]

})

st.dataframe(
    dataset_table,
    use_container_width=True,
    hide_index=True
)

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
        The target variable is near-balanced, consisting of
        35,097 diabetes cases (50.82%) and 33,960 non-diabetes
        cases (49.18%) after duplicate removal.

        Since the class distribution remained close to balanced,
        no additional resampling technique such as oversampling,
        undersampling, or SMOTE was required prior to modeling.
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
    same nested cross-validation protocol (Table III of the
    manuscript). CatBoost achieved the highest average ROC-AUC,
    Recall, and MCC, together with the lowest Brier Score,
    making it the final selected model. As shown in the
    Statistical Significance Testing section below, this
    advantage is statistically significant over Logistic
    Regression and Random Forest, but not over XGBoost.
    """
)

full_metrics_table = pd.DataFrame({

    "Model": [
        "CatBoost",
        "XGBoost",
        "Random Forest",
        "Logistic Regression",
    ],

    "Accuracy": [0.7495, 0.7494, 0.7468, 0.7443],
    "Recall": [0.8000, 0.7994, 0.7969, 0.7704],
    "ROC-AUC": [0.8267, 0.8266, 0.8227, 0.8195],
    "MCC": [0.5003, 0.5001, 0.4949, 0.4886],
    "Brier Score": [0.1684, 0.1685, 0.1713, 0.1723],

})

st.dataframe(
    full_metrics_table,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Mean values across nested cross-validation folds. "
    "Standard deviations are reported in Table III of the published manuscript."
)

t1, t2 = st.columns([1, 1])

with t1:
    st.bar_chart(
        full_metrics_table.set_index("Model")["ROC-AUC"]
    )
    st.caption("ROC-AUC comparison across models.")

with t2:
    st.bar_chart(
        full_metrics_table.set_index("Model")["Brier Score"]
    )
    st.caption("Brier Score comparison — lower is better calibrated.")

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
# STATISTICAL SIGNIFICANCE TESTING
# ======================================================

st.subheader("Statistical Significance Testing")

st.write(
    """
    Reporting a higher metric value alone does not confirm that
    one model is genuinely better than another — the difference
    could arise from random variation across cross-validation
    folds. To address this, ROC-AUC values from the outer
    cross-validation folds were compared pairwise across all
    four models using paired t-tests and Wilcoxon signed-rank
    tests, with Cohen's d for effect size and Bonferroni
    correction applied to control for multiple comparisons.
    """
)

significance_table = pd.DataFrame({

    "Model 1": [
        "Logistic Regression",
        "Logistic Regression",
        "Logistic Regression",
        "Random Forest",
        "Random Forest",
        "XGBoost",
    ],

    "Model 2": [
        "Random Forest",
        "XGBoost",
        "CatBoost",
        "XGBoost",
        "CatBoost",
        "CatBoost",
    ],

    "Mean ROC-AUC (1 vs 2)": [
        "0.8195 vs 0.8227",
        "0.8195 vs 0.8266",
        "0.8195 vs 0.8267",
        "0.8227 vs 0.8266",
        "0.8227 vs 0.8267",
        "0.8266 vs 0.8267",
    ],

    "Bonferroni p-value": [
        0.0009,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        1.0000,
    ],

    "Significant": [
        "True",
        "True",
        "True",
        "True",
        "True",
        "False",
    ],

})

st.dataframe(
    significance_table,
    use_container_width=True,
    hide_index=True
)

st.success(
    """
    **Key Finding**

    CatBoost significantly outperformed both Logistic Regression
    and Random Forest in ROC-AUC after Bonferroni correction
    (p < 0.001). However, the difference between CatBoost and
    XGBoost (0.8267 vs 0.8266) was **not statistically
    significant** (paired t-test p = 0.5629; Bonferroni-corrected
    p = 1.0000), indicating that both boosting-based models offer
    comparable discriminative capability for diabetes risk
    prediction. CatBoost was ultimately selected primarily on
    the basis of its lowest Brier Score and highest Recall.
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
    "Journal Authors: Virzan Pasa Nugraha¹, Agung Febrian² — "
    "Informatika, Universitas Sebelas April Sumedang"
)

st.caption(
    "Prototype Contribution: Fidi Supriadi supported the development "
    "and review of the interactive web prototype (SIDIAS), and is not "
    "listed as an author of the published manuscript."
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

st.caption(
    "References [1]–[15] as cited in the published manuscript. "
    "Numbering follows the original manuscript reference list."
)

st.markdown(
    """
    1. Pinandito, A., Wicaksono, S. A., & Wijoyo, S. H. (2023).
       Implementasi Machine Learning dalam Deteksi Risiko Tinggi
       Diabetes Melitus pada Kehamilan. *Jurnal Teknologi
       Informasi dan Ilmu Komputer*, 10(4), 739–746.
    2. Tasin, I., Nabil, T. U., Islam, S., & Khan, R. (2023).
       Diabetes prediction using machine learning and explainable
       AI techniques. *Healthcare Technology Letters*, 10(1–2),
       1–10.
    3. Netayawijit, P., Chansanam, W., & Sorn-In, K. (2025).
       Interpretable Machine Learning Framework for Diabetes
       Prediction: Integrating SMOTE Balancing with SHAP
       Explainability for Clinical Decision Support.
       *Healthcare*, 13(20), 2588.
    4. Alkhanbouli, R., Almadhaani, H. M. A., Alhosani, F., &
       Simsekler, M. C. E. (2025). The role of explainable
       artificial intelligence in disease prediction: a
       systematic literature review and future research
       directions. *BMC Medical Informatics and Decision
       Making*, 25(1), 110.
    5. Pereira, E. D. C., & Andriyani, W. (2025). Diabetes
       Prediction Using Machine Learning. *JIKO (Jurnal
       Informatika dan Komputer)*, 9(3), 639.
    6. Fabiyanto, D., & Putra, Z. P. (2024). Validasi Efektivitas
       Logistic Regression untuk Diagnosa Penyakit Jantung
       melalui Pendekatan Machine Learning. *Jurnal Ilmiah
       FIFO*, 16(2), 158.
    7. Nisa', I. M. K., & Nooraeni, R. (2020). Penerapan Metode
       Random Forest untuk Klasifikasi Wanita Usia Subur di
       Perdesaan dalam Menggunakan Internet (SDKI 2017). *Jurnal
       MSA (Matematika dan Statistika serta Aplikasinya)*, 8(1),
       72.
    8. Dzaky, M., & Kuncoro, A. P. (2026). Optimizing XGBoost for
       Heart Disease Risk Classification Using Optuna and Random
       Search on the BRFSS 2023 Dataset. *JAIC*.
    9. Jasman, T. Z., Fadhlullah, M. A., Pratama, A. L., &
       Rismayani, R. (2022). Analisis Algoritma Gradient
       Boosting, Adaboost dan Catboost dalam Klasifikasi Kualitas
       Air. *Jurnal Teknik Informatika dan Sistem Informasi*,
       8(2).
    10. Van Calster, B., et al. (2025). Evaluation of performance
        measures in predictive artificial intelligence models to
        support medical decisions: overview and guidance. *The
        Lancet Digital Health*, 7(12).
    11. Feng, Q., Du, M., Zou, N., & Hu, X. (2025). Fair Machine
        Learning in Healthcare: A Survey. *IEEE Transactions on
        Artificial Intelligence*, 6(3), 493–507.
    12. Simanjuntak, W. O., Bijaksana, A., Negara, P., &
        Septriana, R. (2023). Perbandingan Algoritma Logistic
        Regression dan Random Forest (Studi Kasus: Klasifikasi
        Emosi Tweet). *JUARA*, 2(1).
    13. Purba, M., Asri, S. D., Ayumi, V., Salamah, U., & Iryani,
        L. (2024). Klasifikasi Dataset Teks Pengaduan Masyarakat
        Terhadap Pemerintah di Sosial Media Menggunakan Logistic
        Regression. *JSAI (Journal Scientific and Applied
        Informatics)*, 7(1), 78–83.
    14. Supriyanto, M. I. A., Hasan, A. A. R., Dharmaesa, D.,
        Aththar, R. F., Febrinato, S. A., & Sari, C. M. (2025).
        Integrasi Mobile Aplikasi untuk Klasifikasi Harga Laptop
        Menggunakan Metode Support Vector Classification dan
        Logistic Regression. *Jurnal Media Informatika*, 6(4),
        2342–2350.
    15. Salim, A., & Alfian, M. R. (2019). Optimalisasi Regresi
        Logistik Menggunakan Algoritma Genetika pada Data
        Klasifikasi. *Jurnal Teknologi Informasi dan Terapan*,
        6(2), 50–55.
    """
)

st.caption(
    "The primary published research underlying this prototype "
    "(Nugraha & Febrian, 2026, JAIC) is described in the "
    "Publication Provenance section above; references [1]–[15] "
    "are the supporting literature cited within that manuscript."
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