# src/ocr/parse_values.py

import re
from ml.feature_map import get_feature_list

# Map OCR labels to model feature keys
OCR_LABEL_MAP = {
    # Diabetes
    "pregnancies": "Pregnancies",
    "glucose": "Glucose",
    "blood pressure": "BloodPressure",
    "skin thickness": "SkinThickness",
    "insulin": "Insulin",
    "bmi": "BMI",
    "diabetes pedigree function": "DiabetesPedigreeFunction",
    "age": "Age",
    # Heart
    "sex": "sex",
    "chest pain type": "cp",
    "resting bp": "trestbps",
    "cholesterol": "chol",
    "fasting bs": "fbs",
    "resting ecg": "restecg",
    "max heart rate": "thalach",
    "exercise induced angina": "exang",
    "st depression": "oldpeak",
    "slope": "slope",
    "ca": "ca",
    "thal": "thal",
    # Anemia
    "hemoglobin": "Hemoglobin",
    "mch": "MCH",
    "mchc": "MCHC",
    "mcv": "MCV",
    "gender": "Gender"
}


def parse_medical_values(text):
    """
    Parse numeric values from OCR text and map them to model feature keys.
    Returns dict suitable for prediction models.
    """
    text_lower = text.lower()
    extracted = {}

    for ocr_label, model_key in OCR_LABEL_MAP.items():
        # Regex: match number after label, ignore parentheses and extra text
        pattern = rf"{ocr_label}.*?([\d.]+)"
        match = re.search(pattern, text_lower)
        if match:
            val = match.group(1)
            extracted[model_key] = float(val) if '.' in val else int(val)
        else:
            extracted[model_key] = 0  # default if not found

    # Filter only features needed by the models
    final_mapped = {}
    for model_key in ["diabetes", "heart", "anemia"]:
        for feature in get_feature_list(model_key):
            final_mapped[feature] = extracted.get(feature, 0)

    return final_mapped
