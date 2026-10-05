from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_skill_score(resume_skills, jd_skills):

    if not jd_skills:
        return 0

    matched = []

    for jd_skill in jd_skills:

        for resume_skill in resume_skills:

            similarity = fuzz.ratio(
                jd_skill.lower(),
                resume_skill.lower()
            )

            if similarity >= 80:
                matched.append(jd_skill)
                break

    score = (len(set(matched)) / len(jd_skills)) * 100

    return score, list(set(matched))


def semantic_similarity(resume_text, jd_text):

    embeddings = model.encode([
        resume_text,
        jd_text
    ])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity * 100


def calculate_final_score(
    skill_score,
    semantic_score,
    experience_score,
    education_score
):

    final_score = (
        skill_score * 0.50 +
        semantic_score * 0.25 +
        experience_score * 0.15 +
        education_score * 0.10
    )

    return round(final_score, 2)