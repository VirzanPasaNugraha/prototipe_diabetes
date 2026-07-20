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
            "Cholesterol Check",
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
            "Smoker",
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
            "Heart Disease",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        PhysActivity = st.selectbox(
            "Physical Activity",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        Fruits = st.selectbox(
            "Consume Fruits",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        Veggies = st.selectbox(
            "Consume Vegetables",
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
            "Healthcare Access",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )



    with col3:


        NoDocbcCost = st.selectbox(
            "Unable Medical Cost",
            [0,1],
            format_func=lambda x:
            "Yes" if x else "No"
        )


        GenHlth = st.slider(
            "General Health",
            1,
            5,
            3
        )


        MentHlth = st.slider(
            "Mental Health Days",
            0,
            30,
            0
        )


        PhysHlth = st.slider(
            "Physical Health Days",
            0,
            30,
            0
        )


        DiffWalk = st.selectbox(
            "Difficulty Walking",
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


        Age = st.slider(
            "Age Category",
            1,
            13,
            7
        )



    col4, col5 = st.columns(2)


    with col4:

        Education = st.slider(
            "Education Level",
            1,
            6,
            5
        )


    with col5:

        Income = st.slider(
            "Income Level",
            1,
            8,
            5
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

        predictor = Predictor()


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