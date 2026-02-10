
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)

RISK_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a careful medical risk assessor.

Your task:
- Decide if a patient should:
  - NO_CONSULT
  - CONSULT (non-urgent)
  - URGENT medical attention

Rules:
- Kidney stones ALWAYS require CONSULT (not urgent unless red flags)
- Do NOT exaggerate
- Do NOT use percentages
- Base decisions on medical safety

Return ONLY valid JSON in this format:
{{
  "risk_level": "LOW | MEDIUM | HIGH",
  "doctor_action": "NO_CONSULT | CONSULT | URGENT",
  "reasoning": "short explanation",
  "watch_for": "symptoms to monitor"
}}
"""
    ),
    ("human", "{report_text}")
])

def llm_assess_risk(report_text: str) -> str:
    chain = RISK_PROMPT | llm
    response = chain.invoke({"report_text": report_text})
    return response.content
