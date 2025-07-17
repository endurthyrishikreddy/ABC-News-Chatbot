import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(query, articles):
    context_blocks = []
    for i, doc in enumerate(articles):
        context_blocks.append(
            f"""Article {i+1}:
Title: {doc['title']}
Summary: {doc['description']}
Details: {doc['spell']}
URL: {doc['url']}"""
        )
    context = "\n\n".join(context_blocks)

    prompt = f"""Answer the question below based only on the news context provided.

Question: {query}

Context:
{context}
"""

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text