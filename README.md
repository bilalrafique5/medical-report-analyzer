# Medical-Report-Analyzer

AI-Based Medical Report Analyzer & Multi-Disease Prediction System

## Features
- Train ML models for Diabetes, Heart Disease, Anemia, Blood Pressure.
- Streamlit web UI: manual input + OCR upload.
- Tesseract OCR for extracting numbers from reports.
- Clear explanations and normal-range comparisons.

## Setup
1. Create virtualenv and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux / Mac
   venv\Scripts\activate       # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Install Tesseract OCR:

Windows: https://github.com/UB-Mannheim/tesseract/wiki

Linux: sudo apt install tesseract-ocr

Set path in config/settings.py if needed.

Put datasets in data/raw/ and train models (or copy pre-trained .pkl to models/).

Run Streamlit app:

bash
Copy code
streamlit run app.py
Notes
Align feature names and order used in training with src/ml/feature_map.py.

OCR parsing is heuristic — refine regex for lab formats you have.