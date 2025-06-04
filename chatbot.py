import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load your .env file

# ✅ Correct: use the OpenAI class in v1.x
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an IT support assistant."},
                {"role": "user", "content": query}
            ],
            temperature=0.6,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

