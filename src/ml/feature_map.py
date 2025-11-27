"""
Map extracted OCR keys to model features.
This should reflect the columns used during training.
Adjust lists for your trained models.
"""

FEATURES={
    
    "diabetes":["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"],
    "heart":["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","condition"],
    "anemia":["Gender","Hemoglobin","MCH","MCHC","MCV","Result"]
}

def get_feature_list(model_key):
    return FEATURES.get(model_key, [])