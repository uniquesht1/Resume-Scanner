
---

## 🧠 Resume Scanner API

A Dockerized FastAPI backend that extracts skills and generates summaries from uploaded resumes.

---

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
