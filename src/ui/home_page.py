import streamlit as st


def show_home():
    st.title("AI Medical Report Analyzer")
    st.subheader("Automated Medical Report Analyzer & Multi-Diseas Rist Prediction")
    st.write("""
    This application extracts common values from medical test reports (via OCR) and predicts risks for:
    - Diabetes
    - Heart disease
    - Anemia
    - High blood pressure

    Use the left sidebar to navigate:
    - Manual Input: enter values yourself
    - Upload Report (OCR): upload a lab report image and extract values automatically
    - Results: view predictions & explanations
    """)
    st.info("This tool is for educational purposes only. Not a substitute for professional medical advice.")