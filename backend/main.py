from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resume import router as resume_router
from dotenv import load_dotenv
import os

app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Access environment variables
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
THRESHOLD = float(os.getenv("THRESHOLD", 0.6))
SUMMARY_MODEL = os.getenv("SUMMARY_MODEL", "facebook/bart-large-cnn")

# Print loaded environment variables for debugging
print(f"Loaded MODEL_NAME: {MODEL_NAME}")
print(f"Loaded THRESHOLD: {THRESHOLD}")
print(f"Loaded SUMMARY_MODEL: {SUMMARY_MODEL}")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router, prefix="/resume")
