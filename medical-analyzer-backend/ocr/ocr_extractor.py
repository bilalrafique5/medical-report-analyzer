# src/ocr/ocr_extractor.py

from PIL import Image
import pytesseract
import io
from config import settings


def setup_tesseract():
    """Set tesseract command if provided in settings."""
    if settings.TESSERACT_CMD:
        pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD


def extract_text_from_bytes(file_bytes):
    """
    Return extracted text from image bytes (supports image files).
    """
    setup_tesseract()
    img = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    text = pytesseract.image_to_string(img)
    return text


def extract_text_from_pil(img_pil):
    """
    Return extracted text from a PIL image object.
    """
    setup_tesseract()
    text = pytesseract.image_to_string(img_pil)
    return text
