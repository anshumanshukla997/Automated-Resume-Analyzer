import io
from pathlib import Path

import pandas as pd
import PyPDF2
import streamlit as st

st.set_page_config(page_title="Automated Resume Analyzer", page_icon="📄")
st.title("📄 Automated Resume Analyzer")
st.write("Upload your resume and get a job-match score.")

JOB_SKILLS = ["python", "sql", "machine learning", "data analysis", "excel"]


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text safely from an uploaded PDF."""
    reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages).lower()


uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    try:
        text = extract_text_from_pdf(uploaded_file)
    except Exception as exc:
        st.error(f"Could not read this PDF: {exc}")
        st.stop()

    if not text.strip():
        st.warning("No selectable text was found in this PDF. Please upload a text-based resume PDF.")
        st.stop()

    matched_skills = [skill for skill in JOB_SKILLS if skill in text]
    score = (len(matched_skills) / len(JOB_SKILLS)) * 100

    st.subheader("🔍 Analysis Result")
    st.write("✅ Skills Found:")
    st.write(matched_skills if matched_skills else "No target skills found")

    st.write("📊 Resume Score:")
    st.write(f"{score:.2f}%")

    if score > 70:
        st.success("Great Resume! 🎉")
    elif score > 40:
        st.warning("Good, but can improve 👍")
    else:
        st.error("Needs improvement ⚠️")

    result_df = pd.DataFrame(
        {
            "Skills Found": [", ".join(matched_skills)],
            "Score": [round(score, 2)],
        }
    )

    # Save results next to the application, so the location does not depend
    # on the directory from which Streamlit is started.
    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)
    result_path = results_dir / "result.csv"
    result_df.to_csv(result_path, index=False)

    st.write(f"📁 Result saved to `{result_path.relative_to(project_root)}`")

    csv_data = result_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Result",
        data=csv_data,
        file_name="result.csv",
        mime="text/csv",
    )

    st.subheader("📊 Score Visualization")
    st.bar_chart(pd.DataFrame({"Score": [score]}))
