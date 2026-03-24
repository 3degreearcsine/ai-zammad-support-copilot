from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_ticket(title):
    prompt = f"""
    You are a support engineer.

    Analyze:
    "{title}"

    Provide:
    - Issue Type
    - Priority
    - Root Cause
    - Debug Steps
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
