def recommend_specialist(text: str):
    text = text.lower()

    mapping = {
        "cardiologist": [
            "cholesterol", "ldl", "hdl", "triglyceride", "blood pressure"
        ],
        "endocrinologist": [
            "hba1c", "glucose", "diabetes", "thyroid", "tsh"
        ],
        "nephrologist": [
            "creatinine", "urea", "egfr", "kidney"
        ],
        "hepatologist": [
            "sgpt", "sgot", "alt", "ast", "bilirubin", "liver"
        ],
        "hematologist": [
            "hemoglobin", "rbc", "wbc", "platelet", "anemia"
        ],
    }

    for doctor, keywords in mapping.items():
        if any(k in text for k in keywords):
            return doctor.capitalize()

    return "General Physician"
