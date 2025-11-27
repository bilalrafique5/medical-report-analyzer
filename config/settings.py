# path to tesseract executable 
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


MODEL_PATHS = {
    'diabetes':'models/diabetes_model.pkl',
    'heart':'models/heart_disease_model.pkl',
    'anemia':'models/anemia_model.pkl',
}

SCALER_PATHS={
    'diabetes':'models/scaler_diabetes.pkl',  # corrected from scaler_diabetes.pkl
    'heart':'models/scaler_heart.pkl',
    'anemia':'models/scaler_anemia.pkl',
}

# Thresholds for low/medium/high labeling
THRESHOLDS={
    "low":0.3,
    "high":0.6
}
