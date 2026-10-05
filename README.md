# Resume Scanner - Job Match

## Project Overview

Resume Scanner - Job Match is a Streamlit-based application that analyzes a resume and compares it with a given job description.

The application can extract resume text from images and PDF files using OCR and text extraction techniques. It identifies important resume details such as contact information, skills, education, and experience. It then compares the extracted skills and resume content with the job description and generates a match score.

## Features

* Upload resume as PDF or image
* Extract text from normal PDF resumes
* Extract text from scanned PDF and images using OCR
* Extract resume information

  * Name
  * Email
  * Phone number
  * LinkedIn
  * GitHub
  * Skills
  * Education
  * Experience
* Paste a job description
* Compare resume with job description
* Calculate resume-job match score
* Display matched skills
* Display missing skills
* Provide resume improvement suggestions
* View extracted resume text

## Technologies Used

* Python
* Streamlit
* Tesseract OCR
* pdfplumber
* pdf2image
* Pillow
* Sentence Transformers
* Scikit-learn
* RapidFuzz
* Plotly

## Project Structure

```text
Resume Scanner/
│
├── app.py
├── resume_parser.py
├── ocr.py
├── matcher.py
├── requirements.txt
└── README.md
```

## How It Works

```text
Upload Resume
      |
      v
PDF / Image Detection
      |
      v
Text Extraction / OCR
      |
      v
Resume Parsing
      |
      v
Paste Job Description
      |
      v
Skill Matching
      |
      v
Semantic Similarity
      |
      v
Match Score
      |
      v
Matched Skills + Missing Skills
```

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd "Resume Scanner"
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 5. Install Requirements

```powershell
python -m pip install -r requirements.txt
```

## Tesseract OCR Setup

This project uses Tesseract OCR to read text from resume images and scanned PDFs.

Install Tesseract OCR on Windows and set its path in `ocr.py`.

Example:

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

To check whether Tesseract is installed:

```powershell
& "C:\Program Files\Tesseract-OCR\tesseract.exe" --version
```

## Run the Application

Use:

```powershell
python -m streamlit run app.py
```

The Streamlit application will open in the browser.

## Example Job Description

```text
Job Title: Python Developer

We are looking for a Python Developer to join our software development team.

Requirements:

- Good knowledge of Python
- Knowledge of SQL and databases
- Experience with Flask or Django
- Knowledge of REST API
- Basic knowledge of Machine Learning
- Knowledge of Git and GitHub
- Good problem-solving skills
- Good communication skills

Education:

Bachelor's degree in Computer Science, Information Technology,
Artificial Intelligence, or a related field.

Experience:

0-2 years of experience. Freshers with good programming skills
can also apply.

Responsibilities:

- Develop and maintain Python applications
- Work with SQL databases
- Build REST APIs
- Debug and test applications
- Use Git and GitHub for version control
- Work with the development team on software projects
```

## Output

The application displays:

* Resume Match Score
* Matched Skills
* Missing Skills
* Extracted Profile
* Education
* Experience
* Extracted Resume Text

## Future Enhancements

* Add AI-powered resume suggestions
* Support multiple resumes
* Rank resumes based on job requirements
* Add downloadable analysis reports
* Add database storage
* Add multiple job descriptions
* Improve skill extraction using NLP
* Add resume keyword optimization
* Deploy the application online

## Conclusion

Resume Scanner - Job Match helps students and job seekers understand how well their resume matches a particular job description. It combines OCR, NLP, skill matching, and semantic similarity to provide a simple resume analysis system.
