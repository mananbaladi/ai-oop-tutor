"""
app.py
Entry point for the AI OOP Tutor Streamlit application.

Run with:
    streamlit run app.py
"""

from ui.streamlit_ui import run_app

if __name__ == "__main__":
    run_app()
else:
    # Streamlit runs this module directly, so also call run_app() at module level
    run_app()
