from PIL import Image
import pytesseract

def extract_text_from_image(uploaded_file) -> str:
    try:
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception:
        return ""
