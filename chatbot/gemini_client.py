"""
gemini_client.py
Handles all communication with the Gemini API with streaming support.
"""

import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()


def ask_gemini(prompt: str, chat_history: list = None) -> str:
    """Non-streaming — returns full response (used for sidebar buttons)."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ Configuration Error: GEMINI_API_KEY not found in .env file."

    client = genai.Client(api_key=api_key)
    contents = chat_history + [{"role": "user", "parts": [{"text": prompt}]}] if chat_history else prompt

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents,
            )
            return response.text
        except Exception as e:
            error_str = str(e)
            if "503" in error_str or "UNAVAILABLE" in error_str:
                if attempt < 2:
                    time.sleep((attempt + 1) * 5)
                    continue
                return "⚠️ Gemini servers are busy. Please try again."
            elif "429" in error_str:
                return "⚠️ API quota exceeded. Please wait a few minutes."
            else:
                return f"⚠️ Error: {error_str}"


def ask_gemini_stream(prompt: str, chat_history: list = None):
    """Streaming — yields text chunks as they arrive."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        yield "⚠️ Configuration Error: GEMINI_API_KEY not found in .env file."
        return

    client = genai.Client(api_key=api_key)
    contents = chat_history + [{"role": "user", "parts": [{"text": prompt}]}] if chat_history else prompt

    for attempt in range(3):
        try:
            for chunk in client.models.generate_content_stream(
                model="gemini-2.5-flash",
                contents=contents,
            ):
                if chunk.text:
                    yield chunk.text
            return  # success — exit loop
        except Exception as e:
            error_str = str(e)
            if "503" in error_str or "UNAVAILABLE" in error_str:
                if attempt < 2:
                    time.sleep((attempt + 1) * 5)
                    continue
                yield "⚠️ Gemini servers are busy. Please try again."
            elif "429" in error_str:
                yield "⚠️ API quota exceeded. Please wait a few minutes."
            else:
                yield f"⚠️ Error: {error_str}"
            return