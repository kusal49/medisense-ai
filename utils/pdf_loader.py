import pdfplumber

def extract_text_from_pdf(uploaded_file) -> str:
    text = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text.append(page.extract_text() or "")
    return "\n".join(text)
