"""
Map extracted OCR / manual input keys to model features.
Keys must match your trained models.
"""

FEATURES={
    "diabetes":["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"],
    "heart":["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"],
    "anemia":["Gender","Hemoglobin","MCH","MCHC","MCV"]
}

def get_feature_list(model_key):
    return FEATURES.get(model_key, [])
