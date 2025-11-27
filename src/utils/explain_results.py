# src/utils/explain_results.py

from .normal_ranges import NORMAL_RANGES
from config import settings


def risk_label(prob):
    if prob is None:
        return "Unknown"
    if prob >= settings.THRESHOLDS["high"]:
        return "High Risk"
    elif prob>= settings.THRESHOLDS["low"]:
        return "Moderate Risk"
    else:
        return "Low Risk"
    
    
def explain(values_dict, predictions):
    """
    Create human-friendly explanation based on values & probs.
    Returns dict with messages.
    """
    
    messages={}
    for k,v in predictions.items():
        prob=v.get("probability")
        label=risk_label(prob) if prob is not None else "Unknown"
        msg=f"{k.title()} risk:{label}"
        if prob is not None:
            msg+=f"({prob*100:1.f}%)"
            
        reasons=[]
        if k=="diabetes":
            g=values_dict.get("glucose")
            if g:
                if g > NORMAL_RANGES["glucose"]["high"]:
                    reasons.append(f"elevated glucose level of {g}{NORMAL_RANGES['glucose']['unit']}")
                    
        if k=="anemia":
            hb=values_dict.get("hemoglobin")
            if hb:
                if hb< NORMAL_RANGES["hemoglobin"]["low"]:
                    reasons.append(f"low hemoglobin level of {hb}{NORMAL_RANGES['hemoglobin']['unit']}")
                    
        if reasons:
            msg+=". Reasons: "+" ; ".join(reasons)
        messages[k]=msg
    return messages