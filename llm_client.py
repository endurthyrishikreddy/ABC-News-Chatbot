import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_response(prompt, model="gemini-2.0-flash"):
    gemini_model = genai.GenerativeModel(model)
    response = gemini_model.generate_content(prompt)
    return response.text