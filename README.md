# SAARTHI – AI Study Coach

SAARTHI is a lightweight Flask-based AI study assistant built during a hackathon sprint.  
It generates structured explanations based on the selected learning level (Beginner / Intermediate / Advanced).

---

## Project Objective

The goal of SAARTHI was to:

- Build a modular Flask backend
- Implement adaptive explanation logic
- Integrate an external LLM API securely
- Follow proper Git and secret-handling practices

---

## Versions

### SAARTHI 1.0
Rule-based adaptive explanation engine with level-based structured responses.

### SAARTHI 2.0
LLM-powered version integrated with Groq API for dynamic AI-generated explanations.

---

## Tech Stack

- Python
- Flask
- HTML (Embedded Template)
- REST API Integration
- Git & GitHub

---

## Features

- Beginner / Intermediate / Advanced explanation modes
- Clean minimal UI
- Secure API key management using environment variables
- Modular backend structure
- Structured AI-generated responses

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/ManoharJavvaji/hackathon-2026.git
cd hackathon-2026
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variable (Required for SAARTHI 2.0)

Windows:
```bash
setx GROQ_API_KEY "your_api_key_here"
```

Mac/Linux:
```bash
export GROQ_API_KEY="your_api_key_here"
```

### 4. Run the application

```bash
python SAARTHI2.0.py
```

---

## Learning Outcomes

- Git secret scanning & commit history cleanup
- Secure API handling using environment variables
- Flask routing & form handling
- LLM integration via REST APIs
- Clean repository management

---

Built as part of a focused hackathon engineering sprint.
