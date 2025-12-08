from fastapi import FastAPI, UploadFile, File
from ml.predictor import predict_all
from ocr.ocr_extractor import extract_text_from_bytes
from ocr.parse_values import parse_medical_values
from schemas import ManualPredictionInput

app = FastAPI(title="Medical Report Analyzer API")


@app.post("/predict")
def predict_manual(values: ManualPredictionInput):
    """
    Manual prediction endpoint:
    User provides feature values as JSON.
    """
    # Convert Pydantic model to dictionary and filter None values
    input_dict = {k.lower(): v for k, v in values.dict().items() if v is not None}

    # Run prediction
    result = predict_all(input_dict)

    return result


@app.post("/ocr")
async def extract_ocr(file: UploadFile = File(...)):
    """
    OCR prediction endpoint:
    User uploads a PDF/JPG report -> extract text -> parse values -> predict
    """
    # Read uploaded file asynchronously
    content = await file.read()

    # OCR: extract text from PDF/JPG
    text = extract_text_from_bytes(content)

    # Parse medical values from extracted text
    values = parse_medical_values(text)

    # Return text and parsed values to frontend
    return {
        "extracted_text": text,
        "parsed_values": values
    }
