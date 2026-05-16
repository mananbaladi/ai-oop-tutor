notepad C:\Users\HP\Desktop\ai_oop_tutor\requirements.txt
"""
gemini_client.py
Handles all communication with the Gemini API with streaming support.
"""

import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


def ask_gemini(prompt: str, chat_history: list = None) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY not found."
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "503" in str(e) and attempt < 2:
                time.sleep((attempt + 1) * 5)
                continue
            return f"Error: {e}"


def ask_gemini_stream(prompt: str, chat_history: list = None):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        yield "GEMINI_API_KEY not found."
        return
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    for attempt in range(3):
        try:
            response = model.generate_content(prompt, stream=True)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
            return
        except Exception as e:
            if "503" in str(e) and attempt < 2:
                time.sleep((attempt + 1) * 5)
                continue
            yield f"Error: {e}"
            return