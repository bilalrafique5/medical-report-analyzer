import streamlit as st
from src.ml.feature_map import FEATURES

def show_manual_input():
    st.header("Manual Input")
    st.write("Enter numeric values from your lab report or manual measurements.")

    # --- Diabetes inputs ---
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, max_value=500.0, value=100.0)
    bp = st.number_input("Blood Pressure (mmHg)", min_value=0, max_value=200, value=80)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin (uIU/mL)", min_value=0.0, max_value=1000.0, value=80.0)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Age", min_value=0, max_value=130, value=30)

    # --- Heart inputs ---
    sex = st.selectbox("Sex (0=F,1=M)", [0,1])
    cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
    trestbps = st.number_input("Resting BP (mmHg)", min_value=0, max_value=300, value=120)
    chol = st.number_input("Cholesterol (mg/dL)", min_value=0, max_value=500, value=180)
    fbs = st.selectbox("Fasting BS>120 (0/1)", [0,1])
    restecg = st.selectbox("Resting ECG (0-2)", [0,1,2])
    thalach = st.number_input("Max Heart Rate", min_value=0, max_value=250, value=150)
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope of ST segment", [0,1,2])
    ca = st.number_input("Major vessels (0-3)", min_value=0, max_value=3, value=0)
    thal = st.selectbox("Thalassemia", [1,2,3])

    # --- Anemia inputs ---
    gender = st.selectbox("Gender (0=F,1=M)", [0,1])
    hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=25.0, value=13.5)
    mch = st.number_input("MCH", min_value=0.0, max_value=50.0, value=28.0)
    mchc = st.number_input("MCHC", min_value=0.0, max_value=40.0, value=33.0)
    mcv = st.number_input("MCV", min_value=0.0, max_value=150.0, value=85.0)

    if st.button("Save & Predict"):
        user_input = {
            # Diabetes
            "pregnancies": pregnancies,
            "glucose": glucose,
            "bloodpressure": bp,
            "skinthickness": skin_thickness,
            "insulin": insulin,
            "bmi": bmi,
            "diabetespedigreefunction": dpf,
            "age": age,
            # Heart
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal,
            # Anemia
            "gender": gender,
            "hemoglobin": hemoglobin,
            "mch": mch,
            "mchc": mchc,
            "mcv": mcv
        }

        st.session_state["input_values"] = user_input
        st.success("Values saved! Go to 'Results' page to see predictions.")
