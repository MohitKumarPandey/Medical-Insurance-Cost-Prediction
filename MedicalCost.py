import streamlit as st
import joblib
import pandas as pd

# Load Trained Model
model = joblib.load("Medical_InsuranceCostPrediction.pkl")

st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Medical Insurance Cost Prediction")
st.write("Enter the details below to predict your medical insurance charges.")

# ---------------- Inputs ---------------- #

age = st.number_input(
    "Enter Your Age",
    min_value=18,
    max_value=100,
    step=1
)

gender = st.selectbox(
    "Select Gender",
    ["male", "female"]
)

bmi = st.number_input(
    "Enter BMI",
    min_value=10.0,
    max_value=60.0,
    step=0.1
)

childNo = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    step=1
)

smoker = st.selectbox(
    "Are You a Smoker?",
    ["yes", "no"]
)

region = st.selectbox(
    "Select Region",
    [
        "northeast",
        "northwest",
        "southeast",
        "southwest"
    ]
)

# ---------------- Prediction ---------------- #

if st.button("Predict Insurance Cost"):

    # Label Encoding (same as your notebook)
    gender = 1 if gender == "male" else 0
    smoker = 1 if smoker == "yes" else 0

    # One Hot Encoding
    region_northeast = False
    region_northwest = False
    region_southeast = False
    region_southwest = False

    if region == "northeast":
        region_northeast = True

    elif region == "northwest":
        region_northwest = True

    elif region == "southeast":
        region_southeast = True

    else:
        region_southwest = True

    newData = pd.DataFrame({
        "age":[age],
        "sex":[gender],
        "bmi":[bmi],
        "children":[childNo],
        "smoker":[smoker],
        "region_northeast":[region_northeast],
        "region_northwest":[region_northwest],
        "region_southeast":[region_southeast],
        "region_southwest":[region_southwest]
    })

    prediction = model.predict(newData)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")