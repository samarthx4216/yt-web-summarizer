# 🦜 SummarizeIt — YT & Website Summarizer

> Paste any YouTube video URL or website link and get a clean 300-word summary in seconds — powered by LangChain + Groq's blazing fast LLMs.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?style=flat-square&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-orange?style=flat-square)

---

## 🚀 Live Demo

👉 **[Try it on Streamlit](https://your-app-link.streamlit.app)**  
*(Replace with your actual Streamlit link after deployment)*

---

## ✨ Features

- 📺 Summarize **YouTube videos** from any public URL
- 🌐 Summarize **any website or article** by pasting the link
- ⚡ Ultra-fast inference using **Groq API** (llama-3.3-70b-versatile)
- 🔁 Fallback to **yt-dlp** if YouTube loader fails (handles 400 errors)
- 🔐 Secure API key input via Streamlit sidebar
- 🎯 Clean 300-word summaries every time

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Streamlit` | Frontend UI |
| `LangChain` | LLM chaining & summarization |
| `Groq API` | Fast LLM inference |
| `llama-3.3-70b-versatile` | Summarization model |
| `YoutubeLoader` | YouTube transcript extraction |
| `yt-dlp` | YouTube fallback loader |
| `UnstructuredURLLoader` | Website content extraction |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/summarize-it.git
cd summarize-it
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📋 Requirements

Create a `requirements.txt` with:

```
streamlit
langchain
langchain-groq
langchain-community
validators
yt-dlp
unstructured
```

---

## 🔑 How to Get Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up / Log in
3. Navigate to **API Keys**
4. Click **Create API Key**
5. Paste it in the Streamlit sidebar

---

## 🧠 How It Works

```
User pastes URL
      ↓
YouTube URL? → YoutubeLoader → (fallback) yt-dlp
Website URL? → UnstructuredURLLoader
      ↓
LangChain stuff chain
      ↓
Groq LLM (llama-3.3-70b-versatile)
      ↓
300-word Summary ✅
```

---

## 📁 Project Structure

```
summarize-it/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Dependencies
└── README.md            # You are here
```

---

## ⚠️ Known Issues & Fixes

| Issue | Fix Applied |
|-------|------------|
| `HTTP 400` from YouTube | Added `yt-dlp` as fallback loader |
| Empty API key crash | Moved `ChatGroq` init inside button handler |
| Age-restricted videos | Use a different public video |

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License — free to use and modify.

---

## 👤 Author

Made with ❤️ by **Samar**  
🔗 [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)
