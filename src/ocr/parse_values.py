# src/ocr/parse_values.py
import re
from src.ml.feature_map import get_feature_list

def parse_medical_values(text):
    """
    Parse numeric values from OCR text and map them to lowercase keys.
    Returns dict suitable for predictor (all lowercase keys).
    """
    # Convert text to lowercase for easier matching
    text_lower = text.lower()

    # Regex to capture "key: value" or "key value" patterns
    pattern = r'([a-zA-Z ]+)[\s:]+([\d.]+)'
    matches = re.findall(pattern, text_lower)

    extracted = {}
    for key, val in matches:
        key_clean = key.strip().replace(" ", "")  # remove spaces
        try:
            val_float = float(val)
            extracted[key_clean] = val_float
        except:
            continue

    # Map extracted keys to expected feature names
    features_needed = set()
    for model_key in ["diabetes","heart","anemia"]:
        features_needed.update([f.lower() for f in get_feature_list(model_key)])

    # Keep only needed keys
    mapped = {}
    for f in features_needed:
        if f in extracted:
            mapped[f] = extracted[f]
        else:
            mapped[f] = 0  # default value if not found

    return mapped
