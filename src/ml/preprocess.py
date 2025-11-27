import pandas as pd
import numpy as np

def make_input_df(feature_names, values_dict):
    """ 
    Createa single-row DataFrame with columns=features_names,
    values_dict contains keys like 'glucose','hemoglobin' etc (lowercase).
    
    """
    
    row={}
    for f in feature_names:
        key_lower=f.lower()
        # direct if exists in values_dict
        if key_lower in values_dict:
            row[f]=values_dict[key_lower]
        else:
            row[f]=np.nan
            
    df=pd.DataFrame([row], columns=feature_names)
    
    df=df.fillna(df.median(axis=0).iloc[0] if df.shape[1] >0 else 0)
    return df