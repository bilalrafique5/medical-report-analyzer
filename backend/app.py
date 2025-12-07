from fastapi import FastAPI, UploadFile, File
from .ml.predictor import predict_all
from .ocr.ocr_extractor import extract_text_from_bytes
from .ocr.parse_values import parse_medical_values

app = FastAPI(title="Medical Report Analyzer API")

@app.post("/predict") 
def predict_manual(values: dict):
    results = predict_all(values)
    return results

@app.post("/ocr")
def extract_ocr(file: UploadFile = File(...)):
    content = file.file.read()
    text = extract_text_from_bytes(content)
    values = parse_medical_values(text)
    return {"text": text, "values": values}
