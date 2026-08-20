import os
import PyPDF2
import matplotlib.pyplot as plt

job_skills = ["python", "sql", "machine learning", "data analysis", "excel"]

folder_path = "dataset"
files = os.listdir(folder_path)

results = []

for file in files:
    file_path = os.path.join(folder_path, file)

    pdf = open(file_path, "rb")
    reader = PyPDF2.PdfReader(pdf)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()

    found_skills = []

    for skill in job_skills:
        if skill in text:
            found_skills.append(skill)

    score = (len(found_skills) / len(job_skills)) * 100

    results.append((file, score))

# Sorting
results.sort(key=lambda x: x[1], reverse=True)

print("\n===== Resume Ranking =====\n")

names = []
scores = []

for rank, (resume, score) in enumerate(results, start=1):
    print(rank, "-", resume, ":", score, "%")
    names.append(resume)
    scores.append(score)

# Graph
plt.bar(names, scores)
plt.xlabel("Resumes")
plt.ylabel("Score")
plt.title("Resume Ranking")
plt.xticks(rotation=45)
plt.show()






import csv

with open("results/output,csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow (["Resume","Score"])

    for resume,score in results:
        writer.writerow([resume,score])

print("\nResult saved in results/output.csv")        
