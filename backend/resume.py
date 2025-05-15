from fastapi import APIRouter, UploadFile, File
from PyPDF2 import PdfReader
from transformers import pipeline
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend.skills import extract_skills

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

router = APIRouter()

def extract_text_from_pdf(file: UploadFile) -> str:
    reader = PdfReader(file.file)
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text

def generate_summary(text: str) -> str:
    if len(text.split()) < 50:
        return text.strip()
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    results = summarizer(chunks, max_length=60, min_length=25, do_sample=False)
    return " ".join([r['summary_text'] for r in results])

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content_type = file.content_type
    if content_type == "application/pdf":
        text = extract_text_from_pdf(file)
    else:
        try:
            text = (await file.read()).decode("utf-8")
        except UnicodeDecodeError:
            text = (await file.read()).decode("latin-1")

    skills, score, suggestions = extract_skills(text)
    summary = generate_summary(text)
    return {"summary": summary, "skills": skills, "score": score, "suggestions": suggestions}
