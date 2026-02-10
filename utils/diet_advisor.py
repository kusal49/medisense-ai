from langchain_groq import ChatGroq
import os

def ai_diet_advice(report_text: str) -> str:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
You are a responsible medical nutrition assistant.

Based on the medical report below:
- Suggest general foods to EAT
- Suggest foods to AVOID
- Keep advice conservative and safe
- Do NOT suggest supplements or medicines
- If abnormalities are mild, say diet alone may be sufficient
- If unclear, give general healthy advice

Respond in this format ONLY:

Eat:
- item
- item

Avoid:
- item
- item

Medical Report:
{report_text}
"""

    response = llm.invoke(prompt)
    return response.content.strip()