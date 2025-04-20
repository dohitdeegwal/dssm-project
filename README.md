# 📝 Resume Parser

A FastAPI-based application that uses OpenAI's API to extract skills from job descriptions and resumes, returning a match rate and relevant skills.

---

## ⚙️ System Requirements

- **OS:** Ubuntu 20.04  
- **Python:** 3.10+

---

## 🚀 Setup Instructions

### 1. Create a Virtual Environment and Install Dependencies

```bash
# Create virtual environment
python -m venv venv
# OR (if you have virtualenv installed)
python -m virtualenv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### 2. Configure Environment Variables

Create a `.env` file in the root of the project with the following content:

```env
OPENAI_API_KEY=sk-...
TEMPERATURE=0
CHAT_MODEL=gpt-3.5-turbo
ORIGINS=http://127.0.0.1:5137, http://localhost:5137
```

---

### 3. Run the FastAPI Application

```bash
# Development mode
uvicorn main:app --host 0.0.0.0 --port 5000 --reload

# With multiple workers
uvicorn main:app --host 0.0.0.0 --port 5000 --workers 4

# With custom timeout
uvicorn main:app --host 0.0.0.0 --port 5000 --workers 4 --timeout-keep-alive 600
```

---

### 4. Access API Documentation

Visit: [http://0.0.0.0:5000/docs](http://0.0.0.0:5000/docs)

---

## ✅ Features

- 📊 Resume–JD Relevance Scoring  
- 🔍 Resume Skill Matching  
- 💬 Query Resumes via OpenAI API  
- ⚡ FastAPI with OpenAI Integration
