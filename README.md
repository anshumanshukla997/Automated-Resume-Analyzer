# Automated Resume Analyzer

Automated Resume Analyzer is a Python-based project that checks a resume according to a given job description. It reads the resume, looks for relevant skills and keywords, and gives a simple matching result.

## About the Project

The main idea behind this project is to make the initial resume checking process easier and faster.

The application takes a resume in PDF format and compares its content with the requirements of a particular job. It then identifies the skills found in the resume and provides a matching score.

This project was developed as a practical Python project to understand how resume data can be processed and analyzed automatically.

## Features

- Upload resume in PDF format
- Extract text from the resume
- Compare resume with job requirements
- Find relevant skills and keywords
- Calculate a matching score
- Generate analysis results
- Save results in CSV format
- Simple Streamlit interface

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Pandas
- Regular Expressions
- CSV

## Project Structure

```text
Automated-Resume-Analyzer/
│
├── code/
│   ├── app.py
│   └── resume_analyzer.py
│
├── dataset/
│   ├── Resume1.pdf
│   ├── Resume2.pdf
│   ├── Resume3.pdf
│   └── ...
│
├── results/
│   └── output.csv
│
├── Automated Resume Analyzer.pptx
├── Resume_Analyzer_Report.pdf
├── requirements.txt
└── README.md
