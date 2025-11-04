import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Test message from my backend — reply with '✅ working' if you received this."}
    ],
}

response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print("Response:", result["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)