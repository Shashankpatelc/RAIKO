# ⚡ RAIKO - AI Assistant

> *"Built by Rabbie. Powered by AI. Inspired by Iron Man."*

RAIKO is a personal AI assistant built with Python and Ollama. Designed with a clean modular architecture, RAIKO is not just a chatbot — it's the beginning of something much bigger.

---

## 🚀 Features

- 💬 Natural AI conversation powered by Ollama (local LLM)
- 🔒 Secure configuration management
- 🧩 Clean modular architecture — easy to expand
- ⚡ Fast and lightweight
- 📴 Fully offline — no API keys, no quotas, no internet needed

---

## 🗂️ Project Structure

```
RAIKO/
├── raiko.py            — entry point, runs everything
├── config.py           — model settings
├── .gitignore          — protects secrets
└── modules/
    ├── chat.py         — AI brain, processes and responds
    ├── model_input.py  — handles user input
    ├── model_output.py — handles response output
    └── memory.json     — stores conversation summary
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Shashankpatelc/RAIKO.git
cd RAIKO
```

**2. Install Ollama**

Download and install from https://ollama.com then pull a model:
```bash
ollama pull llama3.2:1b
```

**3. Install dependencies**
```bash
pip install ollama
```

**4. Run RAIKO**
```bash
python raiko.py
```

---

## 🛣️ Roadmap

- [x] Base architecture
- [x] AI conversation
- [x] Memory
- [x] Offline mode with local LLM
- [ ] Custom commands
- [ ] Personality
- [ ] Voice input & output
- [ ] Desktop UI

---

## 👤 About

Built by **Rabbie** — a developer who turns ideas into reality, one line at a time. Because why use existing tools when you can build your own.

Inspired by JARVIS from Iron Man. This is just the beginning. ⚡

---

> *"Every expert was once a beginner. Every pro was once an amateur."*

-Rabbie