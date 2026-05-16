# 🎓 AI OOP Tutor

An intelligent, interactive **Object-Oriented Programming tutor** powered by **Google Gemini AI** and built with **Streamlit**. Teaches OOP concepts like a real teacher — with explanations, Python code examples, and ASCII diagrams.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **Chat Mode** | Ask any OOP question in natural language |
| 📚 **Learn Topic** | Get a full structured lesson on any OOP concept |
| 🧠 **Quiz Mode** | Test your knowledge with AI-generated quiz questions |
| ⚖️ **Compare Mode** | Side-by-side comparison of two OOP concepts |
| 🗂️ **Diagram Mode** | Generate ASCII/text diagrams for any concept |
| 🐍 **Code Examples** | Pre-built, well-commented Python examples |
| 🗂️ **Quick Diagrams** | Reference ASCII diagrams in the sidebar |

---

## 🗂️ Project Structure

```
ai_oop_tutor/
│
├── app.py                    # Main entry point
├── requirements.txt          # Python dependencies
├── .env                      # API key (create this yourself)
├── README.md
│
├── chatbot/
│   ├── gemini_client.py      # Gemini API communication
│   ├── prompts.py            # All prompt templates
│   └── oop_teacher.py        # Teaching logic & routing
│
├── diagrams/
│   ├── ascii_diagrams.py     # Pre-built ASCII diagrams
│   └── mermaid_generator.py  # Mermaid.js diagram generators
│
├── examples/
│   └── python_examples.py    # Ready-to-run OOP code examples
│
└── ui/
    └── streamlit_ui.py       # Full Streamlit UI
```

---

## 🚀 Quick Start

### 1. Clone / Download the project

```bash
cd ai_oop_tutor
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the key

### 5. Configure the API key

Open the `.env` file and replace the placeholder:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 6. Run the app

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501` 🎉

---

## 📖 OOP Topics Covered

- Class & Object
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Constructor (`__init__`)
- Method Overriding
- Method Overloading
- Multiple Inheritance
- Magic/Dunder Methods
- Class vs Instance Variables
- Static & Class Methods
- Properties & Decorators
- Composition vs Inheritance
- SOLID Principles

---

## 🧑‍💻 Tech Stack

| Part | Technology |
|---|---|
| AI | Google Gemini 1.5 Flash |
| Language | Python 3.9+ |
| UI | Streamlit |
| Diagrams | ASCII Text + Mermaid.js |
| Environment | python-dotenv |

---

## 📸 Example Interaction

**User:** Explain encapsulation

**AI Tutor:**

```
## 📖 What is Encapsulation?
Encapsulation means bundling data (attributes) and the methods that operate
on that data into a single unit (a class), and restricting direct access
to some of the object's components.

## 🌍 Real-Life Analogy
Think of a medicine capsule — you can't see or touch the medicine inside,
but you can take it. The internal details are hidden.

## 🐍 Python Example
class BankAccount:
    def __init__(self):
        self.__balance = 0    # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

## 🗂️ Diagram
+------------------+
|   BankAccount    |
+------------------+
| - __balance      |  ← hidden
+------------------+
| + deposit()      |  ← public
| + get_balance()  |  ← public
+------------------+
```

---

## ⚠️ Troubleshooting

**"GEMINI_API_KEY not found"**
→ Make sure `.env` exists and has your actual key (not the placeholder).

**Streamlit not found**
→ Run `pip install -r requirements.txt` inside your virtual environment.

**Module not found errors**
→ Always run `streamlit run app.py` from the `ai_oop_tutor/` folder.

---

## 📄 License

MIT License — free to use, modify, and share.
