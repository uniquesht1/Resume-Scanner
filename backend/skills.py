from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
KNOWN_SKILLS = [
    "python", "machine learning", "docker", "react", "node.js", "fastapi", "django", "postgresql", "sql", "aws",
    "data analysis", "deep learning", "nlp", "pandas", "numpy", "tensorflow", "keras", "flask", "azure", "git"
]
skill_embeddings = model.encode(KNOWN_SKILLS, convert_to_tensor=True)

def extract_skills(text):
    sentences = text.split(".")
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    matched_skills = set()
    total_score = 0
    suggestions = []

    for emb in sentence_embeddings:
        cosine_scores = util.cos_sim(emb, skill_embeddings)[0]
        top_index = cosine_scores.argmax().item()
        if cosine_scores[top_index] > 0.4:
            matched_skills.add(KNOWN_SKILLS[top_index])
            total_score += float(cosine_scores[top_index])

    missing_skills = [s for s in KNOWN_SKILLS if s not in matched_skills]
    suggestions.append(f"Consider highlighting skills like: {', '.join(missing_skills[:5])}")

    return list(matched_skills), round(total_score, 2), suggestions
