# src/ocr/parse_values.py

import re

def _find_number_after_keyword(text,keywords):
    """ Search for a number after any of the keywords inside text.
        Returnsfloat or None"""
        
    for kw in keywords:
        pattern=rf"{kw}[^0-9\-—:]*(?:[:\-]?\s*)(\d+\.?\d*)"
        m=re.search(pattern,text, flags=re.IGNORECASE)
        if m:
            try:
                return float(m.group(1))
            except:
                continue
    return None


def parse_medical_values(ocr_text):
    """ 
    Return dictionary of detected medical values.
    Add more keys / keywords as needed for your local lab formats.
    
    
    """
    text = ocr_text.lower()
    out = {}
    # glucose / blood sugar
    out["glucose"] = _find_number_after_keyword(text, ["glucose", "blood sugar", "sugar"])
    # cholesterol
    out["cholesterol"] = _find_number_after_keyword(text, ["cholesterol", "chol"])
    # hemoglobin
    out["hemoglobin"] = _find_number_after_keyword(text, ["hemoglobin", "hb"])
    # rbc
    out["rbc"] = _find_number_after_keyword(text, ["rbc"])
    # platelets
    out["platelets"] = _find_number_after_keyword(text, ["platelets", "plt"])
    # systolic / diastolic common labels
    out["systolic"] = _find_number_after_keyword(text, ["systolic", "sbp"])
    out["diastolic"] = _find_number_after_keyword(text, ["diastolic", "dbp"])
    # bmi
    out["bmi"] = _find_number_after_keyword(text, ["bmi"])
    # filter None values
    return {k: v for k, v in out.items() if v is not None}
    