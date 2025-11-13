# 🧠 Singularity.AI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-green)
![Gemini](https://img.shields.io/badge/Google%20Gemini-API-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

**Singularity.AI** is a minimalist, space-themed AI chatbot built using **Flask**, **Gemini API**, and a **retro terminal-style web interface** powered by HTML, CSS, and JavaScript.

---

## 🚀 Features
- 💬 Real-time chat powered by Google Gemini API  
- 🌌 Space/terminal themed UI with CRT glow effect  
- ⚙️ Flask backend for API handling  
- 🔒 Secure `.env` key loading (no hardcoded secrets)  
- 🧩 Lightweight — runs locally with no database  

---

## 🏗️ Project Structure
```

.
├── app.py              # Flask backend using Gemini API
├── templates/
│   └── index.html       # Frontend layout
├── static/
│   ├── style.css        # Retro terminal styling
│   └── script.js        # Chat logic and fetch requests
├── .env                 # Contains GOOGLE_API_KEY (not pushed)
└── README.md

````

---

## ⚙️ Requirements
- Python 3.8+
- Flask
- python-dotenv
- google-generativeai

---

## 🔧 Setup & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/SingularityAI.git
cd SingularityAI
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install flask python-dotenv google-generativeai
```

### 4️⃣ Add your Google Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run the Flask app

```bash
python app.py
```

### 6️⃣ Visit the app

Open your browser and go to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🖥️ How It Works

* The user types a message in the web UI
* `script.js` sends the message to `/chat` via POST
* `app.py` calls **Gemini API** for a response
* The AI reply is shown dynamically on the chat screen

---

## 🎨 UI Preview

A glowing green retro console-style chat with a **red “Send” button**, pixelated text, and a CRT flicker overlay — giving the illusion of an old-school AI terminal.

---

## 🧩 Example Interaction

**You:** Hello, who are you?
**AI:** I’m Singularity.AI — your intelligent digital friend from the stars 🌌

---

## 🧠 Tech Stack

* **Backend:** Flask (Python)
* **AI Engine:** Google Gemini API (`models/gemini-2.5-flash-lite`)
* **Frontend:** HTML, CSS, JavaScript
* **Styling:** CRT & retro terminal aesthetic
* **Environment:** dotenv for secure API key handling

---

## ⚠️ Notes

* Keep your `.env` file private — do **not** push it to GitHub.
* If API key is leaked, regenerate it immediately.
* For deployment (Render, Vercel, etc.), add your API key as an environment variable.

---

## 📜 License

This project is licensed under the **MIT License** — free for personal and commercial use.

---

## 💡 Author

Developed by **SRINIVASAN**
Built for learning, fun, and exploring conversational AI. 🌠
