import streamlit as st
import PyPDF2
import pandas as pd

st.title("📄 Automated Resume Analyzer")
st.write("Upload your resume and get job match score")

job_skills = ["python", "sql", "machine learning", "data analysis", "excel"]

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()

    matched_skills = []

    for skill in job_skills:
        if skill in text:
            matched_skills.append(skill)

    score = (len(matched_skills) / len(job_skills)) * 100

    # 🔍 RESULT
    st.subheader("🔍 Analysis Result")

    st.write("✅ Skills Found:")
    st.write(matched_skills)

    st.write("📊 Resume Score:")
    st.write(f"{score:.2f}%")

    # 🎯 Message
    if score > 70:
        st.success("Great Resume! 🎉")
    elif score > 40:
        st.warning("Good, but can improve 👍")
    else:
        st.error("Needs improvement ⚠️")

    # 📁 CSV Save
    data = {
        "Skills Found": [", ".join(matched_skills)],
        "Score": [score]
    }

    df = pd.DataFrame(data)
    df.to_csv("result.csv", index=False)

    st.write("📁 Result saved as result.csv")

    # 📥 Download Button
    st.download_button(
        label="Download Result",
        data=df.to_csv(index=False),
        file_name="result.csv",
        mime="text/csv"
    )

    # 📊 GRAPH (FIXED)
    st.subheader("📊 Score Visualization")

    chart_data = pd.DataFrame({
        "Score": [score]
    })

    st.bar_chart(chart_data)