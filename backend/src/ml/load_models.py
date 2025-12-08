import joblib 
import os
from config import settings


def safe_load(path):
    if path and os.path.exists(path):
        return joblib.load(path)
    return None

def load_all_models():
    models={}
    scalers={}
    
    for key, path in settings.MODEL_PATHS.items():
        models[key] = safe_load(path)
    for key, path in settings.SCALER_PATHS.items():
        scalers[key]=safe_load(path)
        
    return models, scalers