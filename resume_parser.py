import re


SKILLS = [
    "Python", "Java", "C++", "C", "SQL", "MySQL", "Oracle",
    "MongoDB", "HTML", "CSS", "JavaScript", "React", "Node.js",
    "Flask", "Django", "Git", "GitHub", "Docker", "Kubernetes",
    "AWS", "Azure", "Machine Learning", "Deep Learning",
    "Artificial Intelligence", "Data Science", "Data Analytics",
    "Power BI", "Pandas", "NumPy", "TensorFlow", "PyTorch",
    "NLP", "LLM", "LangChain", "REST API", "Excel",
    "Tableau", "Linux", "Cloud Computing"
]


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    result = re.findall(pattern, text)

    return result[0] if result else "Not found"


def extract_phone(text):
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"
    result = re.findall(pattern, text)

    return result[0] if result else "Not found"


def extract_linkedin(text):
    pattern = r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    result = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    return result[0] if result else "Not found"


def extract_github(text):
    pattern = r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+"

    result = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    return result[0] if result else "Not found"


def extract_skills(text):

    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return list(dict.fromkeys(found_skills))


def find_section(text, section_names):

    lines = text.splitlines()

    start = -1

    for i, line in enumerate(lines):

        clean_line = line.strip().lower()

        if clean_line in section_names:

            start = i + 1
            break

    if start == -1:
        return "Not found"

    section = []

    stop_words = [
        "skills",
        "education",
        "experience",
        "work experience",
        "projects",
        "certifications",
        "achievements",
        "interests",
        "languages"
    ]

    for line in lines[start:]:

        clean_line = line.strip().lower()

        if clean_line in stop_words:
            break

        if line.strip():
            section.append(line.strip())

    return "\n".join(section) if section else "Not found"


def extract_education(text):

    education_keywords = [
        "b.sc",
        "bsc",
        "b.e",
        "be",
        "b.tech",
        "btech",
        "m.sc",
        "msc",
        "m.e",
        "m.tech",
        "mba",
        "computer science",
        "artificial intelligence"
    ]

    lines = text.splitlines()

    education = []

    for line in lines:

        line_lower = line.lower()

        for keyword in education_keywords:

            if keyword in line_lower:

                education.append(line.strip())
                break

    return list(dict.fromkeys(education))


def extract_experience(text):

    pattern = r"\b\d+(?:\.\d+)?\+?\s*(?:years?|yrs?)\b"

    result = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    return list(dict.fromkeys(result))


def extract_name(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return "Not found"

    for line in lines[:8]:

        lower = line.lower()

        if (
            "resume" not in lower
            and "curriculum" not in lower
            and "email" not in lower
            and "phone" not in lower
            and "linkedin" not in lower
            and "github" not in lower
        ):

            if not any(char.isdigit() for char in line):

                return line

    return "Not found"


def parse_resume(text):

    profile = {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "linkedin": extract_linkedin(text),

        "github": extract_github(text),

        "skills": extract_skills(text),

        "education": extract_education(text),

        "experience": extract_experience(text),

        "projects": find_section(
            text,
            ["projects", "project"]
        ),

        "certifications": find_section(
            text,
            ["certifications", "certificates", "certification"]
        ),

        "experience_details": find_section(
            text,
            ["experience", "work experience", "employment"]
        )
    }

    return profile