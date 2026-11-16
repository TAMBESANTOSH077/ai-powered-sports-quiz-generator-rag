# 🏆 AI-Powered Sports Quiz Generator using RAG

An intelligent sports quiz generator that combines **Historical Sports Facts**, **Live Web Search**, and **Google Gemini AI** to generate accurate and engaging multiple-choice quizzes.

The project demonstrates **Retrieval-Augmented Generation (RAG)** by retrieving information from a local **ChromaDB Vector Database** and the internet before generating quiz questions.

---




# 📌 Project Overview

Traditional quiz applications use fixed questions stored in a database, making them repetitive and outdated.

This project solves that problem by:

- Retrieving historical sports facts from ChromaDB
- Retrieving recent sports news using DuckDuckGo
- Combining both sources using RAG
- Generating AI-powered quizzes using Google Gemini

---

# 🎯 Project Goal

Develop an AI application that generates:

- Accurate quizzes
- Up-to-date sports questions
- Multiple-choice questions
- Answer explanations
- Context-aware quizzes

---

# 🚀 Features

✅ AI-Powered Quiz Generation

✅ Retrieval-Augmented Generation (RAG)

✅ ChromaDB Vector Database

✅ Live Sports News Search

✅ Google Gemini AI Integration

✅ Streamlit Web Interface

✅ Multiple Sports Support

✅ Difficulty Selection

✅ Historical + Latest Knowledge

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | Web UI |
| ChromaDB | Vector Database |
| DuckDuckGo Search | Live Search |
| Google Gemini API | AI Quiz Generation |
| JSON | Historical Sports Data |
| dotenv | API Key Management |

---

# 📂 Project Structure

```
sports-quiz-agent/

│

├── app.py

├── requirements.txt

├── README.md

├── .env.example

│

├── data/

│ └── sports_facts.json

│

├── chroma_db/

│

├── src/

│ ├── __init__.py

│ ├── config.py

│ ├── database.py

│ ├── search.py

│ ├── generator.py

│ └── utils.py

│

└── screenshots/

```

---

# ⚙ Installation

## 1 Clone Repository

```bash
git clone https://github.com/yourusername/sports-quiz-agent.git

cd sports-quiz-agent
```

---

## 2 Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Create .env

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 5 Run Application

```bash
streamlit run app.py
```

---

# 🏗 Project Workflow

```
User

↓

Select Sport

↓

Select Difficulty

↓

Search Historical Facts

(ChromaDB)

+

Search Latest Sports News

(DuckDuckGo)

↓

Combine Context

(RAG)

↓

Google Gemini AI

↓

Generate Quiz

↓

Display Quiz
```

---

# 🧠 Architecture

```
                    User

                      │

                      ▼

             Streamlit Application

                      │

          ┌───────────┴───────────┐

          ▼                       ▼

     ChromaDB               DuckDuckGo

(Historical Facts)       (Latest News)

          │                       │

          └───────────┬───────────┘

                      ▼

              Context Builder (RAG)

                      │

                      ▼

                Gemini AI Model

                      │

                      ▼

           Generate Multiple Choice Quiz

                      │

                      ▼

               Streamlit User Interface
```

---

# 📷 Screenshots

## Home Page

<img src="screenshots/home.png" width="900">

---

## Generated Quiz

<img src="screenshots/quiz.png" width="900">

---

## RAG Context

<img src="screenshots/context.png" width="900">

---

# 💡 Real-Life Applications

- Sports Education Platforms
- Schools & Colleges
- Online Quiz Websites
- Fantasy Sports Platforms
- Sports News Websites
- Sports Coaching Institutes
- E-Learning Platforms

---

# ✅ Advantages

- Generates quizzes automatically
- Uses latest sports information
- Reduces AI hallucinations
- Easy to use
- Fast quiz generation
- Modern AI architecture
- Scalable design

---

# ⚠ Limitations

- Requires internet connection
- Depends on Gemini API
- Small historical dataset
- Search result quality depends on available web content

---

# 🔮 Future Enhancements

- User Authentication
- Quiz Timer
- Leaderboard
- Score Calculation
- PDF Export
- Voice Assistant
- Multi-language Support
- Sports Image Generation
- Admin Dashboard
- Dedicated Sports News APIs

---

# 👨‍💻 Author

**Santosh Tambe**

BE Computer Engineering

Python Developer | AI Enthusiast | Full Stack Learner

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

Portfolio: https://yourportfolio.com

---

# 📜 License

This project is developed for educational purposes and assignment submission.

---

# ⭐ Acknowledgements

- Google Gemini API
- Streamlit
- ChromaDB
- DuckDuckGo Search
- Python Community

---

## ⭐ If you like this project, consider giving it a star on GitHub.
