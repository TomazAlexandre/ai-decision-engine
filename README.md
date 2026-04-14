# AI Decision Engine

An intelligent backend API built with **Python**, **FastAPI**, and **OpenAI**, designed to analyze input data, generate decisions using AI, and persist results in a database.

This project demonstrates a real-world backend architecture with:

* AI-powered decision analysis
* structured API endpoints
* fallback handling
* persistence with SQLite + SQLAlchemy
* decision history tracking

---

## Features

* REST API built with FastAPI
* AI-based decision engine using OpenAI
* Structured JSON response parsing
* Fallback handling when AI response fails
* Persistence layer using SQLite + SQLAlchemy
* Decision history endpoint
* Environment-based configuration

---

## Tech Stack

* Python
* FastAPI
* OpenAI API
* SQLAlchemy
* SQLite
* Uvicorn
* python-dotenv

---

## Project Structure

```bash
ai-decision-engine/
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── analyze.py
│   ├── services/
│   │   ├── ai_service.py
│   │   └── decision_engine.py
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## How It Works

The API receives input data through the `/analyze` endpoint.

Flow:

1. The request is sent to the decision engine
2. The AI model analyzes the input
3. The response is parsed and validated
4. The result is saved to the database
5. The API returns the structured decision
6. The `/history` endpoint can be used to inspect previous decisions

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TomazAlexandre/ai-decision-engine.git
cd ai-decision-engine
```

### 2. Create and activate a virtual environment

#### Windows (cmd)

```bash
python -m venv venv
venv\Scripts\activate
```

#### Windows (PowerShell)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root of the project.

Use `.env.example` as reference:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_ID=gpt-4o-mini
```

---

## Running the Project

Start the API locally with:

```bash
python -m uvicorn app.main:app --reload
```

Swagger docs will be available at:

```bash
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### `GET /`

Health/root endpoint

#### Response

```json
{
  "message": "AI Decision Engine running"
}
```

---

### `POST /analyze`

Analyzes input data and returns an AI-based decision.

#### Example request

```json
{
  "value": 80,
  "user": "test"
}
```

#### Example response

```json
{
  "decision": "APPROVE",
  "confidence": 0.84,
  "source": "ai",
  "input": {
    "value": 80,
    "user": "test"
  },
  "id": 1,
  "created_at": "2026-04-14T10:00:00.000000"
}
```

#### Fallback response example

```json
{
  "decision": "ERROR",
  "confidence": 0,
  "source": "fallback",
  "input": {
    "value": 80,
    "user": "test"
  },
  "error": "Invalid decision returned by AI"
}
```

---

### `GET /history`

Returns the list of stored decisions.

#### Example response

```json
[
  {
    "id": 1,
    "input_data": {
      "value": 80,
      "user": "test"
    },
    "decision": "APPROVE",
    "confidence": 0.84,
    "source": "ai",
    "created_at": "2026-04-14T10:00:00.000000"
  }
]
```

---

## Database

This project uses **SQLite** for simplicity and **SQLAlchemy** as ORM.

A local database file is created automatically:

```bash
decision_engine.db
```

The database stores:

* input payload
* AI decision
* confidence score
* source of response
* timestamp

---

## Example Use Cases

This project can be extended for scenarios such as:

* approval/rejection workflows
* intelligent scoring systems
* document or text evaluation
* AI-assisted automation pipelines
* internal decision support systems

---

## Engineering Highlights

This project was built with focus on:

* clean backend structure
* separation of concerns
* AI integration
* data persistence
* practical production-oriented design

It is intended as a portfolio project to demonstrate backend and AI engineering skills.

---

## Next Steps

Planned improvements:

* Docker support
* automated tests with pytest
* deployment to Render or Railway
* request validation with Pydantic schemas
* improved logging
* support for multiple decision strategies

---

## Author

**Tomaz Alexandre**

* GitHub: https://github.com/TomazAlexandre
* LinkedIn: https://www.linkedin.com/in/tomaz-santos-a0b545369/
