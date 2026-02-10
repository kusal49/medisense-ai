from langchain_groq import ChatGroq
import os

def ai_why_it_matters(report_text: str) -> str:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.15,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
You are a careful medical assistant.

Explain WHY the findings in this medical report matter:
- Use simple, calm language
- Do NOT diagnose diseases
- Do NOT create fear
- If findings are mild, clearly say so
- Focus on long-term health understanding

Limit response to 4–5 sentences.

Medical Report:
{report_text}
"""

    response = llm.invoke(prompt)
    return response.content.strip()
