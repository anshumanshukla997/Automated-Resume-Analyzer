from pathlib import Path
import csv
import sys

import PyPDF2

JOB_SKILLS = ["python", "sql", "machine learning", "data analysis", "excel"]


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text from a PDF and safely handle pages with no text."""
    with pdf_path.open("rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages).lower()


def analyze_resume(pdf_path: Path) -> float:
    text = extract_text_from_pdf(pdf_path)
    found_skills = [skill for skill in JOB_SKILLS if skill in text]
    return (len(found_skills) / len(JOB_SKILLS)) * 100


def main() -> int:
    # Resolve paths from the project location instead of the current shell directory.
    project_root = Path(__file__).resolve().parent.parent
    folder_path = project_root / "dataset"
    results_dir = project_root / "results"
    output_path = results_dir / "output.csv"

    if not folder_path.exists():
        print(f"Dataset folder not found: {folder_path}")
        print("Create a 'dataset' folder and place sample PDF resumes inside it.")
        return 1

    pdf_files = sorted(folder_path.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF resumes found in: {folder_path}")
        return 1

    results = []
    for pdf_path in pdf_files:
        try:
            score = analyze_resume(pdf_path)
            results.append((pdf_path.name, score))
        except Exception as exc:
            print(f"Skipping {pdf_path.name}: {exc}")

    if not results:
        print("No resumes could be analyzed.")
        return 1

    results.sort(key=lambda item: item[1], reverse=True)

    print("\n===== Resume Ranking =====\n")
    for rank, (resume, score) in enumerate(results, start=1):
        print(f"{rank}. {resume}: {score:.2f}%")

    results_dir.mkdir(exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Resume", "Score"])
        for resume, score in results:
            writer.writerow([resume, round(score, 2)])

    print(f"\nResult saved in: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
