"""
Threshold Analysis
"""

import streamlit as st
import pandas as pd

from utils.asset_loader import (
    THRESHOLD,
)

st.set_page_config(
    page_title="Threshold Analysis",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Threshold Analysis")

st.caption(
    "Evaluate prediction performance under different probability thresholds (CatBoost, final test set)."
)

st.divider()

# =====================================================
# THRESHOLD OPTIMIZATION FIGURE (previously missing)
# =====================================================

st.subheader("Threshold Optimization Curve")

col1, col2 = st.columns([2, 1])

with col1:
    st.image(
        THRESHOLD,
        caption="Threshold Optimization Results for CatBoost",
        use_column_width=True
    )

with col2:
    st.subheader("Interpretation")
    st.write(
        """
        Lower threshold values increase Recall while
        decreasing Precision.

        Higher threshold values generally improve Precision
        but reduce Recall.

        Threshold optimization was conducted on the final
        held-out test set to determine the optimal
        classification threshold.
        """
    )

st.divider()

# =====================================================
# THRESHOLD SELECTION
# =====================================================

st.subheader("Threshold Selection")

criterion = st.radio(
    "Select threshold criterion (as reported in the manuscript, Table VII)",
    [
        "Best Youden Index (0.50)",
        "Best F1-Score (0.40)",
        "Best Recall (0.10)",
    ],
    horizontal=True,
)

threshold_table = pd.DataFrame({

    "Criterion": [
        "Best Youden Index",
        "Best F1-Score",
        "Best Recall",
    ],

    "Threshold": [0.50, 0.40, 0.10],

    "Accuracy": [0.7485, 0.7440, 0.6224],

    "Precision": [0.7307, 0.6966, 0.5745],

    "Recall": [0.7999, 0.8792, 0.9906],

    "F1 Score": [0.7637, 0.7773, 0.7273],

    "MCC": [0.4983, 0.5040, 0.3529],

    "False Negatives": [1405, 848, 66],

    "False Positives": [2069, 2688, 5150],

})

selected_row = threshold_table[
    threshold_table["Criterion"] == criterion.split(" (")[0]
].iloc[0]

st.divider()

# =====================================================
# METRICS FOR SELECTED CRITERION
# =====================================================

st.subheader(f"Metrics — {selected_row['Criterion']} (threshold {selected_row['Threshold']:.2f})")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Accuracy", f"{selected_row['Accuracy']:.4f}")

with c2:
    st.metric("Recall", f"{selected_row['Recall']:.4f}")

with c3:
    st.metric("Precision", f"{selected_row['Precision']:.4f}")

with c4:
    st.metric("F1 Score", f"{selected_row['F1 Score']:.4f}")

c5, c6, c7, c8 = st.columns(4)

with c5:
    st.metric("MCC", f"{selected_row['MCC']:.4f}")

with c6:
    st.metric("False Negatives", int(selected_row["False Negatives"]))

with c7:
    st.metric("False Positives", int(selected_row["False Positives"]))

with c8:
    st.metric("Threshold", f"{selected_row['Threshold']:.2f}")

st.divider()

# =====================================================
# COMPARISON (all three criteria, Table VII)
# =====================================================

st.subheader("Threshold Comparison (Table VII)")

st.dataframe(
    threshold_table,
    use_container_width=True,
    hide_index=True
)

st.bar_chart(
    threshold_table.set_index("Criterion")[
        ["Accuracy", "Recall", "Precision", "F1 Score"]
    ]
)

st.divider()

# =====================================================
# INTERPRETATION
# =====================================================

st.subheader("Interpretation")

if selected_row["Criterion"] == "Best Youden Index":

    st.success(
        """
        Threshold 0.50 provides the best trade-off between
        Recall and false positive predictions according to
        the Youden Index.

        Suitable for general classification tasks that
        require a balance between Recall and false positive
        predictions.
        """
    )

elif selected_row["Criterion"] == "Best F1-Score":

    st.warning(
        """
        Threshold 0.40 substantially reduces false negatives
        (848 vs 1,405) and increases Recall to 0.8792,
        meaning more diabetes cases are detected earlier.

        However, false positives increase to 2,688.

        Suitable for screening purposes.
        """
    )

else:

    st.error(
        """
        Threshold 0.10 achieves the highest Recall (0.9906)
        but results in 5,150 false positives, making it
        less practical for general healthcare screening.

        In healthcare applications, reducing false negatives
        is often prioritized because missed diabetes cases
        may lead to delayed diagnosis and treatment — but
        this threshold may be too sensitive for practical
        implementation.
        """
    )

st.divider()

st.subheader("Recommendation")

st.info(
"""
Research Recommendation

• Threshold **0.50** → balanced prediction, general
classification tasks.

• Threshold **0.40** → screening scenarios where missing
positive cases is more critical than false alarms.

• Threshold **0.10** → maximum sensitivity, but impractical
due to a very high false positive count; not recommended
for routine use.
"""
)

st.caption(
"Threshold analysis based on the final CatBoost model, reported in Table VII of the manuscript."
)