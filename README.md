# 🎓 Smart Student Assistant - AI Chatbot Using Natural Language Processing

A comprehensive, full-stack academic assistant and pair-programming platform designed for engineering and computer science students. Built with Python, Flask, Scikit-Learn, and NLTK, featuring an NLP conversational engine, curriculum materials across 28 disciplines, adaptive topic-level quizzes, and an automated AI study planner.

---

## 🌟 Key Features

### 1. 🤖 Universal AI Academic Chatbot
- **Natural Language Understanding (NLU)**: Powered by TF-IDF vectorization and multi-class classification for academic query classification.
- **Universal Question Answering**: Answers general computer science questions, complex math equations (via SymPy symbolic solver), and engineering concepts with no unhandled queries.
- **Rich Output Formatting**: Renders responses with formatted markdown code blocks, highlighted keywords, structured bullet points, and copyable snippets.

### 2. 📚 28 Engineering Disciplines (Study Materials)
- Exhaustive syllabus, theoretical bounds, architecture principles, code implementations, and interview preparation questions across **28 subjects**:
  - *Software & Web*: Python, Java, Software Engineering, Object-Oriented Design, Web Development, Mobile App Development, DevOps.
  - *Core Systems & Theory*: Data Structures, DBMS, Operating Systems, Computer Networks, Theory of Computation, Compiler Design, Distributed Systems, Discrete Mathematics.
  - *AI & Data Science*: Artificial Intelligence, Machine Learning, Natural Language Processing, Big Data Analytics.
  - *Hardware & IoT*: Computer Architecture, Digital Electronics, Microprocessors, Internet of Things, Robotics, Computer Graphics.
  - *Security & Cloud*: Cyber Security, Information Security, Cloud Computing.
- Interactive category filter chips and real-time instantaneous keyword search.

### 3. 🎯 Advanced Adaptive Quiz Engine
- **Subject & Topic Selection**: Students can select their engineering subject and choose specific sub-topics or take comprehensive tests.
- **Adaptive Configuration**: Choose between 5, 10, or 15 questions and adjust difficulty (Beginner, Intermediate, Advanced).
- **Interactive Exam Interface**: Live countdown timer, question navigator grid, and instant option selection.
- **In-Depth Academic Review**: Post-quiz breakdown providing correct answers, student choices, and technical explanations for every question.

### 4. 🗓️ AI Study Planner (NLP-Powered)
- **AI Roadmap Generator**: Automatically synthesizes day-by-day milestone schedules based on exam dates, daily hours, and subject difficulty.
- **Milestone Progress Tracking**: 1-click status toggling (Pending / Completed) and plan deletion.
- **Manual Customization**: Add personal study targets with deadlines and detailed task breakdowns.

### 5. 🌓 Light & Dark Theme Engine
- High-contrast, sleek Light and Dark mode toggle button present on every header.
- Persistent user preference saved in browser `localStorage`.
- Fully responsive across mobile, tablet, and desktop viewports.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python 3.10+, Flask, Jinja2, Werkzeug |
| **Machine Learning & NLP** | Scikit-Learn, NLTK, SymPy, NumPy, Pandas |
| **Database** | SQLite3 (Relational persistence for users, plans, quizzes, chats) |
| **Frontend** | Semantic HTML5, Modern CSS3 (Variables, Flexbox, Grid), Vanilla ES6+ JavaScript |

---

## 📂 Project Architecture

```
SmartStudentAssistantNlpProjectt/
│
├── app/
│   ├── __init__.py               # Flask app factory, 25+ API routes & endpoints
│   ├── chatbot.py                # Dual-compatible NLP chatbot & synthesis engine
│   ├── database.py               # SQLite database schemas and CRUD operations
│   ├── knowledge_retriever.py    # Wikipedia and real-time academic retrieval
│   └── quiz_data.py              # 28-subject question bank with topic tags & explanations
│
├── data/
│   ├── intents.json              # NLP training intents and pattern definitions
│   ├── intent_dataset.csv        # Intent classification dataset
│   └── student_assistant.db      # SQLite production database
│
├── models/
│   ├── intent_model.pkl          # Trained intent classifier
│   ├── topic_model.pkl           # Trained topic classifier
│   └── vectorizer.pkl            # Trained TF-IDF vectorizer
│
├── static/
│   └── style.css                 # Global CSS rules and theme variables
│
├── templates/
│   ├── auth.html                 # Login and registration portal
│   ├── history.html              # Chat history and clear history
│   ├── index.html                # Main AI assistant chat interface
│   ├── material_detail.html      # 28-subject curriculum & lessons
│   ├── quiz.html                 # Advanced subject & topic quiz interface
│   ├── study_materials.html      # 28-subject directory with category filters
│   └── study_planner.html        # AI study plan generator & milestone tracker
│
├── requirements.txt              # Production dependency manifest
├── run.py                        # Application entry point
└── README.md                     # Documentation and setup guide
```

---

## 🚀 Step-by-Step Execution Guide

### 1. Extract the Project
Extract `SmartStudentAssistantNlpProjectt.zip` to your preferred folder.

### 2. Open in VS Code or Terminal
Open terminal in the project directory:
```bash
cd SmartStudentAssistantNlpProjectt
```

### 3. Create and Activate Virtual Environment
**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**On Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the Application
```bash
python run.py
```

### 6. Access in Browser
Navigate to:
```
http://127.0.0.1:5000
```
- Create a student account or log in.
- Explore the AI Chatbot, 28 Study Materials, Practice Quizzes, and AI Study Planner!

---

## 📜 License
Developed for educational excellence and academic evaluation. All rights reserved © 2026.
