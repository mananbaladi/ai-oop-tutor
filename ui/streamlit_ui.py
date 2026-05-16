"""
streamlit_ui.py
Full Streamlit UI for the AI OOP Tutor.
"""

import streamlit as st
from chatbot.oop_teacher import (
    teach_topic,
    answer_question,
    generate_quiz,
    compare_concepts,
    generate_diagram,
    get_topic_list,
)
from examples.python_examples import get_example, list_examples, format_topic_name
from diagrams.ascii_diagrams import get_diagram, list_diagrams


# ── Page config ──────────────────────────────────────────────────────────────
def setup_page():
    st.set_page_config(
        page_title="AI OOP Tutor",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
    )


# ── Custom CSS ────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Header */
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(100, 200, 255, 0.15);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }
    .main-header h1 {
        color: #e0f2fe;
        font-size: 2.4rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .main-header p {
        color: #7dd3fc;
        font-size: 1rem;
        margin: 0.4rem 0 0 0;
        font-weight: 300;
    }

    /* Chat messages */
    .user-message {
        background: linear-gradient(135deg, #0f3460, #1a4a7a);
        border-left: 4px solid #38bdf8;
        border-radius: 0 12px 12px 12px;
        padding: 1rem 1.2rem;
        margin: 0.8rem 0;
        color: #e0f2fe;
    }
    .ai-message {
        background: linear-gradient(135deg, #1e1e2e, #252540);
        border-left: 4px solid #a78bfa;
        border-radius: 0 12px 12px 12px;
        padding: 1rem 1.2rem;
        margin: 0.8rem 0;
        color: #f1f5f9;
    }
    .message-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.4rem;
        opacity: 0.7;
    }

    /* Topic chips */
    .topic-chip {
        display: inline-block;
        background: rgba(56, 189, 248, 0.1);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.8rem;
        color: #38bdf8;
        margin: 3px;
        cursor: pointer;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #0f0f1a;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: #cbd5e1;
    }

    /* Code blocks */
    code {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.85rem !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0f3460, #1e3a5f);
        color: #e0f2fe;
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1a4a7a, #2a5a8a);
        border-color: #38bdf8;
        transform: translateY(-1px);
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.08) !important;
    }

    /* Info boxes */
    .tip-box {
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 8px;
        padding: 0.8rem 1rem;
        margin: 1rem 0;
        color: #86efac;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)


# ── Session state helpers ─────────────────────────────────────────────────────
def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "mode" not in st.session_state:
        st.session_state.mode = "💬 Chat"
    if "quiz_topic" not in st.session_state:
        st.session_state.quiz_topic = None


def add_message(role: str, content: str):
    st.session_state.messages.append({"role": role, "content": content})


def display_messages():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="user-message">
                <div class="message-label">👤 You</div>
                {msg['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="ai-message">
                <div class="message-label">🎓 AI Tutor</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(msg["content"])


# ── Sidebar ──────────────────────────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("## 🎓 AI OOP Tutor")
        st.markdown("---")

        # Mode selector
        st.markdown("### 🧭 Mode")
        mode = st.radio(
            "Select mode:",
            ["💬 Chat", "📚 Learn Topic", "🧠 Quiz", "⚖️ Compare", "🗂️ Diagram"],
            label_visibility="collapsed",
        )
        st.session_state.mode = mode
        st.markdown("---")

        # Quick topics
        st.markdown("### 📋 Quick Topics")
        topics = get_topic_list()
        for topic in topics:
            if st.button(topic, key=f"topic_{topic}", use_container_width=True):
                handle_topic_click(topic)

        st.markdown("---")

        # Code examples reference
        st.markdown("### 💻 C++ Code Examples")
        example_keys = list_examples()
        selected_ex = st.selectbox(
            "View example:",
            ["Select..."] + example_keys,
            format_func=lambda k: "Select..." if k == "Select..." else format_topic_name(k),
        )
        if selected_ex and selected_ex != "Select...":
            st.code(get_example(selected_ex), language="cpp")

        st.markdown("---")

        # ASCII diagrams reference
        st.markdown("### 🗂️ Quick Diagrams")
        diagram_keys = list_diagrams()
        selected_diag = st.selectbox(
            "View diagram:",
            ["Select..."] + diagram_keys,
            format_func=lambda k: "Select..." if k == "Select..." else k.replace("_", " ").title(),
        )
        if selected_diag and selected_diag != "Select...":
            st.code(get_diagram(selected_diag))

        st.markdown("---")

        # Clear chat
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.markdown("""
        <div style="text-align:center; font-size:0.75rem; color:#475569; margin-top:1rem;">
        Powered by Manan<br>Built with Streamlit
        </div>
        """, unsafe_allow_html=True)


def handle_topic_click(topic: str):
    """Instantly teach a topic when clicked from sidebar."""
    add_message("user", f"Teach me about: {topic}")
    with st.spinner(f"📖 Preparing lesson on {topic}..."):
        response = teach_topic(topic)
    add_message("assistant", response)
    st.rerun()


# ── Main content modes ────────────────────────────────────────────────────────
def render_chat_mode():
    """Standard ChatGPT-style Q&A chat."""
    st.markdown("""
    <div class="tip-box">
    💡 <strong>Ask anything about OOP!</strong>
    Try: "What is a class in C++?", "Explain inheritance with code", "What is the difference between struct and class?"
    </div>
    """, unsafe_allow_html=True)

    display_messages()

    user_input = st.chat_input("Ask an OOP question in C++...")
    if user_input:
        add_message("user", user_input)
        with st.spinner("🤔 Thinking..."):
            response = answer_question(user_input)
        add_message("assistant", response)
        st.rerun()


def render_learn_mode():
    """Structured topic learning."""
    st.markdown("### 📚 Learn an OOP Concept")
    st.markdown("Select a topic and get a complete, structured lesson.")

    topics = get_topic_list()
    col1, col2 = st.columns([3, 1])
    with col1:
        selected = st.selectbox("Choose a topic:", topics)
    with col2:
        st.write("")
        st.write("")
        teach_btn = st.button("📖 Teach Me!", use_container_width=True)

    if teach_btn:
        add_message("user", f"Teach me about: {selected}")
        with st.spinner(f"Preparing lesson on **{selected}**..."):
            response = teach_topic(selected)
        add_message("assistant", response)

    display_messages()


def render_quiz_mode():
    """Quiz mode — test your knowledge."""
    st.markdown("### 🧠 Test Your Knowledge")
    st.markdown("Pick a topic and get a quiz question with answer explanation.")

    topics = get_topic_list()
    col1, col2 = st.columns([3, 1])
    with col1:
        quiz_topic = st.selectbox("Quiz topic:", topics, key="quiz_select")
    with col2:
        st.write("")
        st.write("")
        quiz_btn = st.button("🎲 Generate Quiz", use_container_width=True)

    if quiz_btn:
        add_message("user", f"Quiz me on: {quiz_topic}")
        with st.spinner("Generating quiz question..."):
            response = generate_quiz(quiz_topic)
        add_message("assistant", response)

    display_messages()


def render_compare_mode():
    """Compare two OOP concepts."""
    st.markdown("### ⚖️ Compare Two Concepts")
    st.markdown("See how two OOP concepts differ with side-by-side examples.")

    topics = get_topic_list()
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        c1 = st.selectbox("First concept:", topics, index=2)
    with col2:
        c2 = st.selectbox("Second concept:", topics, index=3)
    with col3:
        st.write("")
        st.write("")
        cmp_btn = st.button("⚖️ Compare", use_container_width=True)

    if cmp_btn:
        if c1 == c2:
            st.warning("Please select two different concepts!")
        else:
            add_message("user", f"Compare {c1} vs {c2}")
            with st.spinner(f"Comparing {c1} and {c2}..."):
                response = compare_concepts(c1, c2)
            add_message("assistant", response)

    display_messages()


def render_diagram_mode():
    """Generate an ASCII diagram for a concept."""
    st.markdown("### 🗂️ Generate a Diagram")
    st.markdown("Get a visual text diagram for any OOP concept.")

    col1, col2 = st.columns([3, 1])
    with col1:
        concept = st.text_input(
            "Enter concept:",
            placeholder="e.g. 'multiple inheritance', 'observer pattern'",
        )
    with col2:
        st.write("")
        st.write("")
        diag_btn = st.button("🎨 Draw Diagram", use_container_width=True)

    if diag_btn and concept:
        add_message("user", f"Draw an ASCII diagram for: {concept}")
        with st.spinner("Drawing diagram..."):
            response = generate_diagram(concept)
        add_message("assistant", response)

    display_messages()


# ── Main app ──────────────────────────────────────────────────────────────────
def run_app():
    setup_page()
    inject_css()
    init_session()

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 AI OOP Tutor</h1>
        <p>Your personal teacher for Object-Oriented Programming in C++ (Dev C++) — powered by Manan</p>
    </div>
    """, unsafe_allow_html=True)

    render_sidebar()

    # Route to the selected mode
    mode = st.session_state.mode
    if mode == "💬 Chat":
        render_chat_mode()
    elif mode == "📚 Learn Topic":
        render_learn_mode()
    elif mode == "🧠 Quiz":
        render_quiz_mode()
    elif mode == "⚖️ Compare":
        render_compare_mode()
    elif mode == "🗂️ Diagram":
        render_diagram_mode()
