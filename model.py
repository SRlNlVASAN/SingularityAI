import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    models = genai.list_models()
    print("Available Gemini models:")
    for m in models:
        print("-", m.name)
except Exception as e:
    print("Error:", e)
