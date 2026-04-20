# RAIKO
My personal AI assistant. 

# ⚡ RAIKO - AI Assistant

> *"Built by Rabbie. Powered by AI. Inspired by Iron Man."*

RAIKO is a personal AI assistant built with Python and Google Gemini API. Designed with a clean modular architecture, RAIKO is not just a chatbot — it's the beginning of something much bigger.

---

## 🚀 Features

- 💬 Natural AI conversation powered by Google Gemini
- 🔒 Secure API key management with .env
- 🧩 Clean modular architecture — easy to expand
- ⚡ Fast and lightweight

---

## 🗂️ Project Structure

```
RAIKO/
├── raiko.py          — entry point, runs everything
├── config.py         — API keys and settings
├── .env              — secret keys (never pushed to GitHub)
├── .gitignore        — protects secrets
└── modules/
    ├── chat.py       — AI brain, processes and responds
    ├── model_input.py  — handles user input
    └── model_output.py — handles response output
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Shashankpatelc/RAIKO.git
cd RAIKO
```

**2. Install dependencies**
```bash
pip install google-genai python-dotenv
```

**3. Create your .env file**
```
GEMINI_API_KEY=your-gemini-api-key-here
```

**4. Run RAIKO**
```bash
python raiko.py
```

---

## 🛣️ Roadmap

- [x] Base architecture
- [x] AI conversation
- [ ] Personality & memory
- [ ] Custom commands
- [ ] Voice input & output
- [ ] Desktop UI
- [ ] Offline mode with local LLM

---

## 👤 About

Built by **Rabbie** — a developer who turns ideas into reality, one line at a time. Because why use existing tools when you can build your own.

Inspired by JARVIS from Iron Man. This is just the beginning. ⚡

---

> *"Every expert was once a beginner. Every pro was once an amateur."*