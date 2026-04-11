from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_ai(data: dict):
    prompt = f"""
You are a decision engine.

Analyze the input data and return a JSON with:
- decision: APPROVE or REJECT
- confidence: number between 0 and 1

Data:
{data}

Respond ONLY with valid JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a decision engine."},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content