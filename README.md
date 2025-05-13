# ✉️ AI Email Generator

A simple AI-powered app that generates professional or friendly emails based on a subject and tone. Built using **LangChain**, **OpenAI**, and **Streamlit**.

---

## 🚀 Features

- 🤖 Uses OpenAI's `gpt-3.5-turbo` via LangChain
- 💬 Accepts subject and tone to generate relevant email content
- 🎨 Supports tone selection: Formal, Friendly (extendable)
- ⚡ Built with a minimal, user-friendly Streamlit UI
- 🔐 API key handled securely using `.env`

---

## 📁 Project Structure

email-generator/
├── app.py # Streamlit UI code
├── email_generator.py # Core LangChain logic
├── .env # Stores your OpenAI API key (not committed)
├── requirements.txt # Dependencies
└── README.md # Project overview (this file)

---

## Run the App:

streamlit run app.py
