# app.py
import streamlit as st
from src.ui.home_page import show_home
from src.ui.manual_input_page import show_manual_input
from src.ui.ocr_upload_page import show_ocr_upload
from src.ui.results_page import show_results

st.set_page_config(page_title="Medical Report Analyzer", layout="centered")

PAGES = {
    "Home": show_home,
    "Manual Input": show_manual_input,
    "Upload Report (OCR)": show_ocr_upload,
    "Results": show_results
}

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", list(PAGES.keys()))

# Initialize session state for inputs & results
if "input_values" not in st.session_state:
    st.session_state["input_values"] = {}
if "predictions" not in st.session_state:
    st.session_state["predictions"] = {}

# Call the selected page function
page = PAGES[choice]
page()
