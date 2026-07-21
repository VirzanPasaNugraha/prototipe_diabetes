"""
About Developer
"""

import streamlit as st


st.set_page_config(
    page_title="About Developer",
    page_icon="👨‍💻",
    layout="wide"
)


st.title("👨‍💻 About Developer")

st.caption(
    "Developer profile and project information."
)


st.divider()


# ======================================================
# PROFILE
# ======================================================

st.subheader(
    "Developer Profile"
)


col1, col2 = st.columns(
    [1, 2]
)


with col1:

    st.markdown(
        """
        ## 👨‍💻

        """
    )


with col2:

    st.write(
        """
        **Virzan Pasa Nugraha and Agung Febrian**

        Informatics Student

        Universitas Sebelas April (UNSAP)

        Faculty of Information Technology

        Program Studi Informatika
        """
    )


st.divider()


# ======================================================
# PROJECT
# ======================================================

st.subheader(
    "Project Information"
)


project_col1, project_col2, project_col3 = st.columns(3)


with project_col1:

    st.metric(
        "Project",
        "Diabetes AI"
    )


with project_col2:

    st.metric(
        "Model",
        "CatBoost"
    )


with project_col3:

    st.metric(
        "Framework",
        "Streamlit"
    )


st.divider()


# ======================================================
# SKILLS
# ======================================================

st.subheader(
    "Technical Skills"
)


skill1, skill2, skill3 = st.columns(3)


with skill1:

    st.write(
        """
        ### Machine Learning

        - Python
        - Scikit-Learn
        - CatBoost
        - SHAP
        - Model Evaluation
        """
    )


with skill2:

    st.write(
        """
        ### Software Development

        - Streamlit
        - React
        - Astro
        - REST API
        - Database
        """
    )


with skill3:

    st.write(
        """
        ### Research

        - Data Analysis
        - Explainable AI
        - Fairness Evaluation
        - Calibration
        - Scientific Writing
        """
    )


st.divider()


# ======================================================
# PROJECT FEATURES
# ======================================================

st.subheader(
    "Application Features"
)


features = [

    "Machine Learning Diabetes Risk Prediction",

    "CatBoost Classification Model",

    "Probability-based Risk Assessment",

    "Explainable AI using SHAP",

    "Fairness Evaluation",

    "Calibration Analysis",

    "Threshold Optimization",

    "Research-oriented Dashboard"

]


for item in features:

    st.success(
        item
    )


st.divider()


# ======================================================
# ARCHITECTURE
# ======================================================

st.subheader(
    "System Architecture"
)


st.code(
"""
User

 |

Streamlit Interface

 |

Prediction Engine

 |

Validation + Preprocessing

 |

CatBoost Model

 |

Result Formatter

 |

Risk Assessment

 |
 
Recommendation System
""",
language="text"
)


st.divider()


# ======================================================
# CONTACT
# ======================================================

st.subheader(
    "Contact"
)


st.info(
"""
This application was developed as a machine learning
research implementation and portfolio project.

For collaboration and research discussion,
please contact the developer.
"""
)


st.caption(
"Diabetes Risk Prediction System | Version 1.0.0"
)