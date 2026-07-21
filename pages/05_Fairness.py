"""
Fairness Analysis
"""

import streamlit as st
import pandas as pd

from utils.asset_loader import (
    AGE_DISTRIBUTION,
)

st.set_page_config(
    page_title="Fairness Analysis",
    page_icon="⚖️",
    layout="wide"
)


st.title(
    "⚖️ Fairness Analysis"
)

st.caption(
    "Evaluation of model fairness across demographic groups (Sex, Age, Education, Income)."
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
        "Largest Recall Gap (Age)",
        "0.8130",
        help="Recall group 11 (0.8899) - Recall group 1 (0.0769)"
    )


with c2:

    st.metric(
        "Most Disparate Attribute",
        "Age"
    )


with c3:

    st.metric(
        "Groups Evaluated",
        "Sex, Age, Education, Income"
    )


with c4:

    st.metric(
        "Model",
        "CatBoost"
    )


st.divider()


# =====================================================
# AGE DISTRIBUTION (previously missing figure)
# =====================================================

st.subheader(
    "Age Distribution by Diabetes Status"
)

col1, col2 = st.columns([2, 1])

with col1:
    st.image(
        AGE_DISTRIBUTION,
        caption="Age Distribution by Diabetes Status",
        use_column_width=True
    )

with col2:
    st.subheader("Interpretation")
    st.write(
        """
        Diabetes cases are more common in older age
        categories, particularly groups 9-13.

        Younger age groups are dominated by non-diabetes
        cases, indicating that diabetes prevalence
        increases with age.
        """
    )


st.divider()


# =====================================================
# FAIRNESS BY DEMOGRAPHIC GROUP
# =====================================================

st.subheader(
    "Fairness Evaluation Results"
)

tab_sex, tab_age, tab_edu, tab_income = st.tabs(
    [
        "🚻 Sex",
        "🎂 Age",
        "🎓 Education",
        "💰 Income",
    ]
)

# ---------------------------------------------------
# SEX
# ---------------------------------------------------

with tab_sex:

    sex_data = pd.DataFrame({

        "Group": ["0", "1"],

        "Sample Size": [7438, 6374],

        "Accuracy": [0.7606, 0.7344],

        "Recall": [0.7986, 0.8012],

        "FPR": [0.2757, 0.3415],

        "FNR": [0.2014, 0.1988],

        "ROC-AUC": [0.8375, 0.8074],

    })

    st.dataframe(
        sex_data,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        sex_data.set_index("Group")[["Recall", "FPR"]]
    )

    st.write(
        """
        Recall is relatively similar between the two sex
        groups (0.7986 vs 0.8012). However, group 1 shows
        a higher false positive rate (0.3415) compared to
        group 0 (0.2757), meaning the model produces more
        false positive predictions for this group.
        """
    )

# ---------------------------------------------------
# AGE
# ---------------------------------------------------

with tab_age:

    age_data = pd.DataFrame({

        "Group": [str(i) for i in range(1, 14)],

        "Sample Size": [197, 279, 383, 549, 673, 882, 1324,
                         1631, 2015, 2142, 1568, 1060, 1109],

        "Accuracy": [0.9340, 0.9319, 0.8564, 0.8106, 0.7816,
                     0.7619, 0.7432, 0.7315, 0.7424, 0.7502,
                     0.7404, 0.6991, 0.6682],

        "Recall": [0.0769, 0.3043, 0.3387, 0.3561, 0.5856,
                   0.6830, 0.7342, 0.7756, 0.8206, 0.8669,
                   0.8899, 0.8462, 0.8341],

        "FPR": [0.0054, 0.0117, 0.0436, 0.0456, 0.1220,
                0.1869, 0.2493, 0.3132, 0.3610, 0.4435,
                0.5094, 0.5599, 0.5730],

        "FNR": [0.9231, 0.6957, 0.6613, 0.6439, 0.4144,
                0.3170, 0.2658, 0.2244, 0.1794, 0.1331,
                0.1101, 0.1538, 0.1659],

        "ROC-AUC": [0.8537, 0.8894, 0.8290, 0.8535, 0.8482,
                    0.8308, 0.8156, 0.8144, 0.7996, 0.7982,
                    0.7783, 0.7303, 0.7029],

    })

    st.dataframe(
        age_data,
        use_container_width=True,
        hide_index=True
    )

    st.line_chart(
        age_data.set_index("Group")[["Recall", "FNR"]]
    )

    st.warning(
        """
        Younger age groups (1-4) show very low Recall
        (0.0769-0.3561) and very high false negative rates
        (0.6439-0.9231), meaning many diabetes cases in
        younger individuals are missed.

        Older age groups (10-13) achieve much higher Recall
        (above 0.83) with lower false negative rates.

        This indicates a potential bias toward older age
        groups, likely because younger age groups contain
        fewer diabetes-positive cases and smaller sample
        sizes during training.
        """
    )

# ---------------------------------------------------
# EDUCATION
# ---------------------------------------------------

with tab_edu:

    edu_data = pd.DataFrame({

        "Group": ["2", "3", "4", "5", "6"],

        "Sample Size": [330, 684, 3917, 3906, 4956],

        "Accuracy": [0.7182, 0.7617, 0.7302, 0.7611, 0.7534],

        "Recall": [0.9144, 0.9122, 0.8435, 0.8162, 0.7001],

        "FPR": [0.6852, 0.5167, 0.4188, 0.2990, 0.2080],

        "FNR": [0.0856, 0.0878, 0.1565, 0.1838, 0.2999],

        "ROC-AUC": [0.7680, 0.7699, 0.7928, 0.8365, 0.8311],

    })

    st.dataframe(
        edu_data,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        edu_data.set_index("Group")[["Recall", "FPR"]]
    )

    st.write(
        """
        Lower education groups (2 and 3) achieve very high
        Recall (above 0.91) but also show high false
        positive rates (above 0.50).

        Higher education groups tend to have lower false
        positive rates but slightly lower Recall, indicating
        that sensitivity and error distribution vary across
        education levels.
        """
    )

# ---------------------------------------------------
# INCOME
# ---------------------------------------------------

with tab_income:

    st.write(
        "Average fairness metrics across analyzed income categories:"
    )

    income_summary = pd.DataFrame({
        "Metric": ["Accuracy", "Recall", "FPR", "FNR", "ROC-AUC"],
        "Value": [0.7463, 0.8263, 0.4108, 0.1737, 0.7942],
    })

    st.dataframe(
        income_summary,
        use_container_width=True,
        hide_index=True
    )

    st.write(
        """
        Model performance also varies across socioeconomic
        levels, suggesting that income may influence the
        model's ability to identify diabetes risk
        consistently across different population groups.

        Per-group income breakdown was not reported in
        detail in the manuscript; only the aggregate
        results above are available.
        """
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
The fairness evaluation shows that the CatBoost model is
relatively consistent between sex groups, but exhibits
substantial disparities across age and education groups.

The largest disparity is observed in age groups, where
younger individuals are significantly under-detected
(lower Recall, higher FNR) compared to older individuals.

From a clinical perspective, this may lead to delayed
diagnosis in younger populations. From an ethical
standpoint, these disparities highlight the need for bias
mitigation strategies in future work.
"""
)


st.divider()


# =====================================================
# RESEARCH NOTE
# =====================================================


st.info(
"""
Fairness analysis follows the research evaluation
framework (Equal Opportunity concept), measuring Accuracy,
Recall, FPR, FNR, and ROC-AUC disparity between
demographic groups: Sex, Age, Education, and Income.
"""
)


st.caption(
"Fairness evaluation based on the final CatBoost model, reported in Table IV of the manuscript."
)