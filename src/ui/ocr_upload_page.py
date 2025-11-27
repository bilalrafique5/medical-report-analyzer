import streamlit as st 
from src.ocr.ocr_extractor import extract_text_from_bytes
from src.ocr.parse_values import parse_medical_values
from src.utils.file_handler import save_temp_file, cleanup_file

def show_ocr_upload():
    st.header("Upload Medical Report (OCR)")
    uploaded=st.file_uploader("Upload image (jpg, png, tiff). Crop report area for best results.", 
                              type=["jpg","jpeg","png","tiff"])
    if uploaded is not None:
        tmp_path = save_temp_file(uploaded, prefix="report_")
        with open(tmp_path,"rb") as f:
            b = f.read()
        text = extract_text_from_bytes(b)
        st.subheader("OCR Extracted Text (preview)")
        st.text_area("OCR Text", value=text[:3000], height=250)

        parsed = parse_medical_values(text)
        if parsed:
            st.subheader("Extracted Values")
            st.json(parsed)
            if st.button("Use extracted values & Predict"):
                st.session_state["input_values"] = parsed
                st.success("Values saved. Go to Results to view predictions.")
        else:
            st.warning("No numeric values automatically detected. Try a clearer image or manual input.")
        cleanup_file(tmp_path)
