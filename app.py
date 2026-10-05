import streamlit as st
import pdfplumber
from PIL import Image
from pdf2image import convert_from_bytes

from ocr import extract_text_from_image
from resume_parser import parse_resume
from matcher import calculate_skill_score, semantic_similarity


st.set_page_config(
    page_title="Resume Scanner",
    layout="wide"
)

st.title("Resume Scanner - Job Match")

st.write("Upload your resume and paste the job description.")


# Resume Upload
resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "png", "jpg", "jpeg"]
)


# Job Description
jd_text = st.text_area(
    "Paste Job Description",
    height=200
)


# Analyze
if st.button("Analyze Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")

    elif jd_text.strip() == "":
        st.error("Please enter the job description.")

    else:

        resume_text = ""

        # PDF
        if resume_file.name.endswith(".pdf"):

            pdf_bytes = resume_file.read()

            with pdfplumber.open(resume_file) as pdf:

                for page in pdf.pages:

                    text = page.extract_text()

                    if text:
                        resume_text += text + "\n"

            # Scanned PDF
            if len(resume_text.strip()) < 50:

                pages = convert_from_bytes(pdf_bytes)

                for page in pages:
                    resume_text += extract_text_from_image(page)

        # Image
        else:

            image = Image.open(resume_file)

            resume_text = extract_text_from_image(image)


        # Parse Resume
        profile = parse_resume(resume_text)


        # Parse Job Description
        jd_profile = parse_resume(jd_text)


        # Skills
        resume_skills = profile["skills"]
        jd_skills = jd_profile["skills"]


        # Match Skills
        skill_score, matched_skills = calculate_skill_score(
            resume_skills,
            jd_skills
        )


        # Missing Skills
        missing_skills = []

        for skill in jd_skills:

            if skill not in matched_skills:
                missing_skills.append(skill)


        # Semantic Score
        semantic_score = semantic_similarity(
            resume_text,
            jd_text
        )


        # Final Score
        final_score = (
            skill_score * 0.50
            + semantic_score * 0.50
        )


        # Result
        st.success("Resume analysis completed!")


        col1, col2, col3 = st.columns(3)


        with col1:
            st.metric(
                "Match Score",
                f"{final_score:.1f}%"
            )


        with col2:
            st.metric(
                "Matched Skills",
                len(matched_skills)
            )


        with col3:
            st.metric(
                "Missing Skills",
                len(missing_skills)
            )


        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "Extracted Profile",
                "Matched Skills",
                "Missing Skills",
                "Resume Text"
            ]
        )


        # Extracted Profile
        with tab1:

            st.header("Extracted Profile")

            st.write(
                "Name:",
                profile.get("name", "Not found")
            )

            st.write(
                "Email:",
                profile.get("email", "Not found")
            )

            st.write(
                "Phone:",
                profile.get("phone", "Not found")
            )

            st.write(
                "LinkedIn:",
                profile.get("linkedin", "Not found")
            )

            st.write(
                "GitHub:",
                profile.get("github", "Not found")
            )


            st.subheader("Skills")

            if profile["skills"]:

                st.write(
                    ", ".join(profile["skills"])
                )

            else:

                st.write("No skills found.")


            st.subheader("Education")

            education = profile.get(
                "education",
                []
            )

            if education:

                for item in education:
                    st.write(item)

            else:

                st.write("Education not found.")


            st.subheader("Experience")

            experience = profile.get(
                "experience",
                []
            )

            if experience:

                for item in experience:
                    st.write(item)

            else:

                st.write("Experience not found.")


        # Matched Skills
        with tab2:

            st.header("Matched Skills")

            if matched_skills:

                for skill in matched_skills:

                    st.success(skill)

            else:

                st.info(
                    "No matching skills found."
                )


            st.write(
                f"Skill Match Score: {skill_score:.1f}%"
            )

            st.write(
                f"Semantic Score: {semantic_score:.1f}%"
            )


        # Missing Skills
        with tab3:

            st.header("Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.warning(
                        skill
                    )

            else:

                st.success(
                    "No major missing skills."
                )


        # Resume Text
        with tab4:

            st.header("Extracted Resume Text")

            st.text_area(
                "OCR Text",
                resume_text,
                height=500
            )