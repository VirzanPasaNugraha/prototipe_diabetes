"""
Diabetes Risk Prediction
"""

import streamlit as st

from utils.predictor import Predictor


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Prediction",
    page_icon="🩺",
    layout="wide"
)


# ==========================
# CACHED MODEL LOADING
# ==========================

@st.cache_resource(show_spinner="Loading model...")
def get_predictor() -> Predictor:
    """
    Load the Predictor (and its underlying CatBoost pipeline)
    once per session instead of on every form submission.
    """
    return Predictor()


# ==========================
# SCALE LABELS (BRFSS 2015 codebook)
# ==========================

GENHLTH_LABELS = {
    1: "Excellent",
    2: "Very Good",
    3: "Good",
    4: "Fair",
    5: "Poor",
}

AGE_LABELS = {
    1: "18-24",
    2: "25-29",
    3: "30-34",
    4: "35-39",
    5: "40-44",
    6: "45-49",
    7: "50-54",
    8: "55-59",
    9: "60-64",
    10: "65-69",
    11: "70-74",
    12: "75-79",
    13: "80+",
}

EDUCATION_LABELS = {
    1: "Never attended school / Kindergarten only",
    2: "Elementary (Grades 1-8)",
    3: "Some High School (Grades 9-11)",
    4: "High School Graduate / GED",
    5: "Some College / Technical School",
    6: "College Graduate",
}

INCOME_LABELS = {
    1: "< $10,000",
    2: "$10,000 - $14,999",
    3: "$15,000 - $19,999",
    4: "$20,000 - $24,999",
    5: "$25,000 - $34,999",
    6: "$35,000 - $49,999",
    7: "$50,000 - $74,999",
    8: "$75,000+",
}


# ==========================
# TITLE
# ==========================

st.title(
    "🩺 Diabetes Risk Prediction"
)

st.caption(
    "Predict diabetes risk using CatBoost model trained on BRFSS 2015 dataset."
)


st.divider()


# ==========================
# INPUT FORM
# ==========================

st.subheader(
    "Patient Health Information"
)


with st.form("prediction_form"):


    col1, col2, col3 = st.columns(3)


    with col1:

        HighBP = st.selectbox(
            "High Blood Pressure",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        HighChol = st.selectbox(
            "High Cholesterol",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        CholCheck = st.selectbox(
            "Cholesterol Check (last 5 years)",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        BMI = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=80.0,
            value=25.0
        )


        Smoker = st.selectbox(
            "Smoker (100+ cigarettes lifetime)",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        Stroke = st.selectbox(
            "Stroke History",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


    with col2:


        HeartDiseaseorAttack = st.selectbox(
            "Heart Disease / Heart Attack",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        PhysActivity = st.selectbox(
            "Physical Activity (past 30 days)",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        Fruits = st.selectbox(
            "Consume Fruits (1+ per day)",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        Veggies = st.selectbox(
            "Consume Vegetables (1+ per day)",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        HvyAlcoholConsump = st.selectbox(
            "Heavy Alcohol Consumption",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        AnyHealthcare = st.selectbox(
            "Has Healthcare Coverage",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )



    with col3:


        NoDocbcCost = st.selectbox(
            "Skipped Doctor Due to Cost",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        GenHlth = st.selectbox(
            "General Health",
            list(GENHLTH_LABELS.keys()),
            index=2,
            format_func=lambda x:
            f"{x} - {GENHLTH_LABELS[x]}"
        )


        MentHlth = st.slider(
            "Mental Health — Poor Days (past 30 days)",
            0,
            30,
            0
        )


        PhysHlth = st.slider(
            "Physical Health — Poor Days (past 30 days)",
            0,
            30,
            0
        )


        DiffWalk = st.selectbox(
            "Difficulty Walking / Climbing Stairs",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        Sex = st.selectbox(
            "Sex",
            [0,1],
            format_func=lambda x:
            "Female" if x == 0 else "Male"
        )


        Age = st.selectbox(
            "Age Category",
            list(AGE_LABELS.keys()),
            index=6,
            format_func=lambda x:
            f"{x} - {AGE_LABELS[x]}"
        )



    col4, col5 = st.columns(2)


    with col4:

        Education = st.selectbox(
            "Education Level",
            list(EDUCATION_LABELS.keys()),
            index=4,
            format_func=lambda x:
            f"{x} - {EDUCATION_LABELS[x]}"
        )


    with col5:

        Income = st.selectbox(
            "Income Level",
            list(INCOME_LABELS.keys()),
            index=4,
            format_func=lambda x:
            f"{x} - {INCOME_LABELS[x]}"
        )


    submit = st.form_submit_button(
        "🔍 Predict Diabetes Risk",
        use_container_width=True
    )



# ==========================
# RESULT
# ==========================


if submit:


    patient = {


        "HighBP": HighBP,

        "HighChol": HighChol,

        "CholCheck": CholCheck,

        "BMI": BMI,

        "Smoker": Smoker,

        "Stroke": Stroke,

        "HeartDiseaseorAttack":
            HeartDiseaseorAttack,

        "PhysActivity":
            PhysActivity,

        "Fruits":
            Fruits,

        "Veggies":
            Veggies,

        "HvyAlcoholConsump":
            HvyAlcoholConsump,

        "AnyHealthcare":
            AnyHealthcare,

        "NoDocbcCost":
            NoDocbcCost,

        "GenHlth":
            GenHlth,

        "MentHlth":
            MentHlth,

        "PhysHlth":
            PhysHlth,

        "DiffWalk":
            DiffWalk,

        "Sex":
            Sex,

        "Age":
            Age,

        "Education":
            Education,

        "Income":
            Income

    }


    try:

        predictor = get_predictor()


        result = predictor.predict_result(
            patient
        )



        st.divider()


        st.subheader(
            "Prediction Result"
        )


        col1,col2,col3 = st.columns(3)


        with col1:

            st.metric(
                "Prediction",
                result["prediction"]
            )


        with col2:

            st.metric(
                "Probability",
                result["probability"]
            )


        with col3:

            st.metric(
                "Risk Level",
                result["risk_level"]
            )


        st.divider()


        st.subheader(
            "Recommendations"
        )


        for item in result["recommendations"]:

            st.success(
                item
            )


        st.divider()


        st.subheader(
            "Model Information"
        )


        info1,info2,info3 = st.columns(3)


        with info1:

            st.write(
                "Model"
            )

            st.write(
                result["model"]
            )


        with info2:

            st.write(
                "Dataset"
            )

            st.write(
                result["dataset"]
            )


        with info3:

            st.write(
                "Version"
            )

            st.write(
                result["version"]
            )



    except Exception as e:


        st.error(
            str(e)
        )