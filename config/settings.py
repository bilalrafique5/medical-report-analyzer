

# path to tesseract executable 
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


MODEL_PATHS = {
    
    'diabetes':'models/diabetes_model.pkl',
    'heart':'models/heart_disease_model.pkl',
    'anemia':'models/anemia_model.pkl',
  
}



SCALER_PATHS={
    'diabetes':'models/diabetes_scaler.pkl',
    'heart':'models/heart_scaler.pkl',
    'anemia':'models/anemia_scaler.pkl',
}


#Thresholds (probability) for low/medium/high labeling
THRESHOLDS={
    "low":0.3,
    "high":0.6
}