from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from prompts.medical_prompt import MEDICAL_REPORT_PROMPT
import os



load_dotenv()


def analyze_medical_report(report_text: str) -> str:
    MAX_CHARS = 4000
    report_text = report_text[:MAX_CHARS]

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )


    prompt = MEDICAL_REPORT_PROMPT
    chain = prompt | llm

    response = chain.invoke({"report_text": report_text})
    return response.content

