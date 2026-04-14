import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_ID = os.getenv("MODEL_ID", "gpt-4o-mini")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=API_KEY)


def analyze_with_ai(data: dict) -> str:
    """
    Sends the input data to the LLM and returns the raw text response.
    The expected output is a valid JSON string only.
    """
    prompt = f"""
You are an AI decision engine.

Your task is to analyze the input data and return ONLY a valid JSON object.

Rules:
- Return ONLY JSON
- Do not include markdown
- Do not include explanations
- The JSON must contain:
  - decision: "APPROVE" or "REJECT"
  - confidence: number between 0 and 1

Input data:
{data}

Example valid response:
{{
  "decision": "APPROVE",
  "confidence": 0.84
}}
"""

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "system",
                "content": "You are a strict JSON-only decision engine."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("Empty response from AI model.")

    return content.strip()