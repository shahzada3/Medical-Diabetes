import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Load saved files

model = joblib.load(
    "models/diabetes_model.pkl"
)

scaler = joblib.load(
    "models/scaler.pkl"
)

features = joblib.load(
    "models/features.pkl"
)


# Page configuration

st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)


# Title

st.title("🩺 AI Diabetes Prediction System")

st.write(
    "Enter patient health information to predict diabetes risk."
)


st.divider()


# Create input dictionary

input_data = {}


# Generate input fields automatically

for feature in features:

    if feature in [
        "BMI",
        "GenHlth",
        "MentHlth",
        "PhysHlth",
        "Age"
    ]:

        value = st.number_input(
            feature,
            min_value=0,
            max_value=100,
            value=0
        )

    else:

        value = st.selectbox(
            feature,
            options=[0,1]
        )


    input_data[feature] = value



# Convert input to dataframe

input_df = pd.DataFrame(
    [input_data]
)


st.subheader("Patient Information")

st.dataframe(
    input_df
)


# Prediction button

if st.button("🔍 Predict Diabetes Risk"):

    prediction = model.predict(
        input_df
    )[0]


    probability = model.predict_proba(
        input_df
    )


    st.divider()


    if prediction == 0:
        result = "No Diabetes Risk"

    elif prediction == 1:
        result = "Prediabetes Risk"

    else:
        result = "Diabetes Risk"


    st.success(
        f"Prediction: {result}"
    )


    confidence = np.max(probability)*100


    st.info(
        f"Confidence Score: {confidence:.2f}%"
    )