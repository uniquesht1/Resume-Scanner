
---

## 🧠 Resume Scanner API

A Dockerized FastAPI backend that extracts skills and generates summaries from uploaded resumes.

---

## 🔧 Quick Start Guide

1. **Clone the repo**
```
git clone https://github.com/your-username/resume-scanner.git
cd resume-scanner
```
2. **Build the Docker image**
```
docker-compose build
```
3. **Run the app**
```
docker-compose up
```
4. **Access API Docs**
```
Open http://localhost:8000/docs in your browser.
```
5. **Run tests**
```
docker-compose run backend pytest
```

## 🚀 Features

- Upload PDF resumes
- Extract skills using embeddings
- Summarize resumes with HuggingFace
- JSON output: `skills`, `score`, `suggestions`
- Docker + Pytest + GitHub Actions CI

---

## 🧱 Project Structure



```

backend/
├── main.py          # FastAPI app
├── resume.py        # Upload route
├── skills.py        # Skill extraction
├── tests/           # Pytest cases
├── Dockerfile
├── .env
└── requirements.txt

```


---

## 🐳 Run with Docker

```
docker-compose build
docker-compose up
```
```
Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
```
```
Run tests:

```bash
docker-compose run backend pytest
```


## CI with GitHub Actions

* Auto builds + tests on push
* Uses Docker-based pipeline (`.github/workflows/ci.yml`)

---

## 12-Factor App Principles (Implemented)

* ✅ **Codebase** in Git
* ✅ **Dependencies** via `requirements.txt`
* ✅ **Config** via `.env`
* ✅ **Port Binding** (8000)
* ✅ **Build/Run** separation with Docker
* ✅ **Logs** to stdout (Uvicorn)
* ✅ **Stateless** processes
* ✅ **CI parity** via Docker

---

Example Output:
![image](https://github.com/user-attachments/assets/33fc8991-cdd7-42f0-b8fb-77a6ff6652bc)
