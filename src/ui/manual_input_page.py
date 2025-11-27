# src/ui/manual_input_page.py
import streamlit as st

def show_manual_input():
    st.header("Manual Input")
    st.write("Enter numeric values from your lab report or manual measurements.")
    # Common fields (extend as needed)
    age = st.number_input("Age", min_value=0, max_value=130, value=30)
    glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, max_value=500.0, value=100.0)
    hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=25.0, value=13.5)
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, max_value=1000.0, value=180.0)
    systolic = st.number_input("Systolic BP (mmHg)", min_value=0, max_value=300, value=120)
    diastolic = st.number_input("Diastolic BP (mmHg)", min_value=0, max_value=200, value=80)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, format="%.1f")

    if st.button("Save & Predict"):
        # Put values in session state so results page picks them up
        st.session_state["input_values"] = {
            "age": age,
            "glucose": glucose,
            "hemoglobin": hemoglobin,
            "cholesterol": cholesterol,
            "systolic": systolic,
            "diastolic": diastolic,
            "bmi": bmi
        }
        st.success("Values saved. Go to 'Results' to view predictions.")
