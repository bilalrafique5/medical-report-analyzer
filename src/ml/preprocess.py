import pandas as pd
import numpy as np

def make_input_df(feature_names, values_dict):
    """
    Create a single-row DataFrame with columns=feature_names.
    Fills missing features with 0 and returns a list of missing features.
    """
    row = {}
    missing_features = []

    for f in feature_names:
        key_lower = f.lower()
        if key_lower in values_dict:
            row[f] = values_dict[key_lower]
        else:
            row[f] = 0  # default for missing features
            missing_features.append(f)

    df = pd.DataFrame([row], columns=feature_names)
    return df, missing_features
