"""
oop_teacher.py
High-level OOP teaching logic — routes questions to the right prompts.
"""

from chatbot.gemini_client import ask_gemini
from chatbot.prompts import (
    build_teach_prompt,
    build_chat_prompt,
    build_quiz_prompt,
    build_compare_prompt,
    build_diagram_prompt,
)

# Core OOP topics the tutor knows about
OOP_TOPICS = [
    "Class & Object",
    "Encapsulation",
    "Inheritance",
    "Polymorphism",
    "Abstraction",
    "Constructor (__init__)",
    "Method Overriding",
    "Method Overloading",
    "Multiple Inheritance",
    "Magic/Dunder Methods",
    "Class vs Instance Variables",
    "Static & Class Methods",
    "Properties & Decorators",
    "Composition vs Inheritance",
    "SOLID Principles",
]


def teach_topic(topic: str) -> str:
    """Teach a specific OOP concept in full depth."""
    prompt = build_teach_prompt(topic)
    return ask_gemini(prompt)


def answer_question(user_message: str, chat_history: list = None) -> str:
    """Answer a general OOP question in chat mode."""
    prompt = build_chat_prompt(user_message)
    return ask_gemini(prompt, chat_history)


def generate_quiz(topic: str) -> str:
    """Generate a quiz question for a given OOP topic."""
    prompt = build_quiz_prompt(topic)
    return ask_gemini(prompt)


def compare_concepts(concept1: str, concept2: str) -> str:
    """Compare two OOP concepts side by side."""
    prompt = build_compare_prompt(concept1, concept2)
    return ask_gemini(prompt)


def generate_diagram(concept: str) -> str:
    """Generate an ASCII diagram for a concept."""
    prompt = build_diagram_prompt(concept)
    return ask_gemini(prompt)


def get_topic_list() -> list:
    """Return the list of available OOP topics."""
    return OOP_TOPICS
