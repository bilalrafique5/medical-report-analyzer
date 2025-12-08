from pydantic import BaseModel
from typing import Optional

class ManualPredictionInput(BaseModel):
    # Diabetes
    pregnancies: Optional[float] = None
    glucose: Optional[float] = None
    blood_pressure: Optional[float] = None
    skin_thickness: Optional[float] = None
    insulin: Optional[float] = None
    bmi: Optional[float] = None
    diabetes_pedigree_function: Optional[float] = None
    age: Optional[float] = None
    
    # Heart
    sex: Optional[int] = None
    chest_pain_type: Optional[int] = None
    resting_bp: Optional[float] = None
    cholesterol: Optional[float] = None
    fasting_bs: Optional[int] = None
    resting_ecg: Optional[int] = None
    max_heart_rate: Optional[float] = None
    exercise_induced_angina: Optional[int] = None
    st_depression: Optional[float] = None
    slope: Optional[int] = None
    ca: Optional[int] = None
    thal: Optional[int] = None

    # Anemia
    hemoglobin: Optional[float] = None
    mch: Optional[float] = None
    mchc: Optional[float] = None
    mcv: Optional[float] = None
    gender: Optional[int] = None
