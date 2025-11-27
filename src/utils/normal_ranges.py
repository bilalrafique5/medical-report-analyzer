# src/utils/normal_ranges.py
NORMAL_RANGES={
    
    "glucose":{"unit":"mg/dL","low":70,"high":140},
    "cholesterol": {"unit": "mg/dL", "low": 125, "high": 200},
    "hemoglobin": {"unit": "g/dL", "low": 13.5, "high": 17.5},  # male typical; adjust for sex if available
    "rbc": {"unit": "10^6/uL", "low": 4.5, "high": 5.9},
    "platelets": {"unit": "10^3/uL", "low": 150, "high": 450},
    "systolic": {"unit": "mmHg", "low": 90, "high": 120},
    "diastolic": {"unit": "mmHg", "low": 60, "high": 80},
    "bmi": {"unit": "", "low": 18.5, "high": 24.9}
    
}