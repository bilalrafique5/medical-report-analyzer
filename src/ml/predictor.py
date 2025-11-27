from .load_models import load_all_models
from .feature_map import get_feature_list
from .preprocess import make_input_df
import numpy as np

models, scalers = load_all_models()

def _predict_for_key(key, values_dict):
    model = models.get(key)
    scaler = scalers.get(key)
    feature_list = get_feature_list(key)

    if model is None:
        return None, "model_not_loaded"

    if not feature_list:
        return None, "no_feature"

    X, missing_features = make_input_df(feature_list, values_dict)

    try:
        if scaler is not None:
            X_scaled = scaler.transform(X)
        else:
            X_scaled = X.values

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X_scaled)[:,1][0]
        else:
            proba = float(model.predict(X_scaled)[0])

        return float(proba), missing_features if missing_features else None
    except Exception as e:
        return None, str(e)

def predict_all(values_dict):
    """
    Takes values extracted from OCR or manual input (keys lowercase).
    Returns dict: { 'diabetes': {prob, error}, ... }
    """
    results = {}
    for key in ["diabetes", "heart", "anemia"]:
        proba, error_or_missing = _predict_for_key(key, values_dict)
        results[key] = {"probability": proba, "error": error_or_missing}
    return results
