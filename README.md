# 🚀 AI Decision Engine API

A production-ready decision engine API built with FastAPI, designed to analyze input data and return structured decisions based on business rules, with full database persistence.

---

## 🌐 Live API

👉 https://ai-decision-engine-583f.onrender.com/docs

---

## ⚙️ Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## 🧠 Overview

This API processes incoming data and generates decisions using rule-based logic.

Each request:

* is validated using Pydantic schemas
* processed through a decision engine service
* stored in a database for traceability
* returns a structured response with decision metadata

---

## 📥 Example Request

```json
{
  "user": "tomaz",
  "value": 150
}
```

---

## 📤 Example Response

```json
{
  "decision": "APPROVED",
  "confidence": 0.9,
  "source": "rule"
}
```

---

## 🏗️ Architecture

The project follows a layered architecture:

* `routers/` → API endpoints
* `services/` → business logic (decision engine)
* `schemas/` → request/response validation
* `database/` → models and DB connection

---

## 💾 Database Persistence

All decisions are stored using SQLAlchemy, enabling:

* historical tracking
* auditability
* future analytics

---

## 🚀 Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📌 Features

* Rule-based decision engine
* Fallback mechanism for error handling
* Clean architecture (service-oriented design)
* Database persistence
* Production deployment

---

## 🎯 Purpose

This project was built to demonstrate backend engineering skills, including:

* API development
* system architecture
* data persistence
* real-world deployment

---

## 🔮 Next Steps

* API Key authentication
* logging system
* dashboard for data visualization
* AI-based decision enhancement

---

## 👨‍💻 Author

**Tomaz Alexandre**

* GitHub: https://github.com/TomazAlexandre
* LinkedIn: https://www.linkedin.com/in/tomaz-santos-a0b545369/
