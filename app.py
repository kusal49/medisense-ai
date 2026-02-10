# app.py
import streamlit as st
import json

from utils.pdf_loader import extract_text_from_pdf
from utils.image_loader import extract_text_from_image
from chains.medical_chain import analyze_medical_report
from utils.llm_risk_assessor import llm_assess_risk
from utils.doctor_mapper import recommend_specialist
from utils.diet_advisor import ai_diet_advice
from utils.why_it_matters import ai_why_it_matters

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="MediSense AI",
    layout="centered"
)

# ---------------- Header ----------------
st.markdown(
    """
    <div style="text-align:center;">
        <h1>MediSense AI</h1>
        <p><b>Understand before you panic</b></p>
        <p>AI Medical Report Analyzer</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- Input Selection ----------------
report_type = st.radio(
    "Select report type",
    ["PDF", "Image (JPG / PNG)"],
    horizontal=True
)

uploaded_file = None

if report_type == "PDF":
    uploaded_file = st.file_uploader(
        "Upload medical report (PDF)",
        type=["pdf"]
    )
else:
    uploaded_file = st.file_uploader(
        "Upload medical report (Image)",
        type=["jpg", "jpeg", "png"]
    )

# ---------------- Processing ----------------
if uploaded_file:
    with st.spinner("Analyzing medical report..."):
        if report_type == "PDF":
            report_text = extract_text_from_pdf(uploaded_file)
        else:
            report_text = extract_text_from_image(uploaded_file)

        result = analyze_medical_report(report_text)

        st.success("Analysis complete ✅")

        # ---------------- Risk Assessment (LLM) ----------------
        risk_json = llm_assess_risk(result)
        risk_data = json.loads(risk_json)

        risk_level = risk_data["risk_level"]
        doctor_action = risk_data["doctor_action"]
        reasoning = risk_data["reasoning"]
        watch_for = risk_data["watch_for"]

        st.subheader("🩺 Risk Assessment")

        if doctor_action == "URGENT":
            st.error(f"🚨 {reasoning}")
        elif doctor_action == "CONSULT":
            st.warning(f"⚠️ {reasoning}")
        else:
            st.success(f"✅ {reasoning}")

        st.caption(f"👀 Watch for: {watch_for}")

        # ---------------- AI Insights ----------------
        st.markdown("---")
        st.subheader("🧠 AI Medical Insights")
        st.markdown(result)

        # ---------------- Specialist Recommendation ----------------
        specialist = recommend_specialist(result)
        st.subheader("👨‍⚕️ Doctor Recommendation")
        st.info(f"Recommended Specialist: **{specialist}**")

        # ---------------- Diet Guidance ----------------
        st.subheader("🥗 Diet Guidance")
        diet_text = ai_diet_advice(result)
        st.markdown(diet_text)

        # ---------------- Why This Matters ----------------
        st.subheader("📌 Why This Matters")
        why_text = ai_why_it_matters(result)
        st.markdown(why_text)

        # ---------------- Disclaimer ----------------
        st.markdown("---")
        st.caption(
            "⚠️ Educational purpose only. This does not replace professional medical advice."
        )
