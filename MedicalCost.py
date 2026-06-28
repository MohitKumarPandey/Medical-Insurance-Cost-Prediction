import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("Medical_InsuranceCostPrediction.pkl")

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #38bdf8;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 30px;
    }

    .result-box {
        background: linear-gradient(135deg, #22c55e, #16a34a);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: white;
    }

    .stButton>button {
        background-color: #38bdf8;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("<div class='title'>💰 Insurance Cost Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter details to estimate your medical insurance cost</div>", unsafe_allow_html=True)

# ---------------- INPUTS ---------------- #
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 25)
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    children = st.number_input("Children", 0, 10, 0)

with col2:
    gender = st.selectbox("Gender", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# ---------------- PREDICTION ---------------- #
if st.button("Predict Insurance Cost 🚀"):

    sex = 1 if gender == "male" else 0
    smoke = 1 if smoker == "yes" else 0

    data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoke,
        "region_northeast": 1 if region == "northeast" else 0,
        "region_northwest": 1 if region == "northwest" else 0,
        "region_southeast": 1 if region == "southeast" else 0,
        "region_southwest": 1 if region == "southwest" else 0,
    }

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    st.markdown(f"""
        <div class='result-box'>
            💰 Estimated Insurance Cost: ${prediction:,.2f}
        </div>
    """, unsafe_allow_html=True)
