# Personalized AI Learning Path Creator 🎯

An AI-powered web application that generates personalized learning roadmaps based on users' skill levels, interests, career goals, and available study time using Python, Streamlit, LangChain, and Groq API.

## 📌 Project Overview

The Personalized AI Learning Path Creator helps learners plan their educational journey through customized, structured learning roadmaps.

By collecting information about a user's learning interests, current skill level, career objectives, and available study hours, the application uses a Large Language Model (LLM) to generate a tailored learning plan.

## ✨ Features

- **Personalized Learning Roadmap:** Generates customized learning paths based on user preferences.
- **Skill-Level Selection:** Supports different learning levels.
- **Goal-Based Learning:** Creates roadmaps aligned with individual learning and career goals.
- **Weekly Learning Schedule:** Organizes topics into a structured learning timeline.
- **Practical Exercises:** Suggests hands-on activities to reinforce learning.
- **Project Recommendations:** Provides practical project ideas.
- **Learning Resources:** Recommends useful learning materials.
- **Download Roadmap:** Allows users to download their generated roadmap in Markdown format.
- **Interactive Interface:** Provides a simple and user-friendly Streamlit interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | LLM integration |
| Groq API | AI inference |
| GPT-OSS-20B | Language model |
| Markdown | Roadmap formatting |

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Personalized_Learning_Path_Creator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Groq API key

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Never upload your actual API key to GitHub.

### 7. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
langchain
langchain-groq
python-dotenv
```

## 🔄 Application Workflow

1. The user opens the Streamlit application.
2. Enters their learning interests and career goals.
3. Selects their current skill level.
4. Specifies available study hours and learning duration.
5. The application processes the information using LangChain.
6. Groq API generates a personalized learning roadmap.
7. The roadmap is displayed in the Streamlit interface.
8. The user can download the generated roadmap.

## 🧠 AI Integration

The application integrates LangChain with Groq's API to communicate with the GPT-OSS-20B language model.

The model processes user inputs and generates structured learning recommendations, including topics, schedules, exercises, projects, and learning resources.

## 🔐 Security

- API keys are stored in environment variables.
- Sensitive credentials should not be committed to GitHub.
- The `.env` file should be included in `.gitignore`.

## 🚀 Future Enhancements

- User authentication and profile management.
- Learning progress tracking.
- AI-powered quizzes and assessments.
- Interactive AI learning assistant.
- Saving and retrieving previous learning roadmaps.
- RAG-based learning resource recommendations.

## 👩‍💻 Author

**Uma Pravallika Chikkam**

GitHub: [UmaPravallika](https://github.com/UmaPravallika)

## 📄 License

This project is intended for educational and learning purposes.
