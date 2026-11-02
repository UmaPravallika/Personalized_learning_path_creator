
import streamlit as st
from langchain_groq import ChatGroq

# Page configuration
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

# Application title
st.title("🎓 Personalized AI Learning Assistant")

st.write(
    "Your personal AI-powered learning companion. "
    "Create a learning roadmap based on your goals."
)
groq_api_key=st.secrets["groq_api_key"]
st.header("Learner Profile")

name=st.text_input("Your Name")
topic=st.text_input("Learning topic")
level=st.selectbox("Your Skill Level",
                   ["Beginner","Intermediate","Advanced"])
goal=st.text_area("What is your learning goal?")
hours=st.slider("Daily Study Hours",1,8,1)
duration=st.selectbox("Learning Duration",["2 Weeks","4 Weeks","6 Weeks","8 Weeks","10 Weeks","12 Weeks"])

if st.button("Generate Learning Path"):
    if not groq_api_key or not name or not goal:
        st.warning("Please fill in all the details.")
    else:
        try:
            with st.spinner("Generating your learning path...."):
                llm=ChatGroq(
                    model="openai/gpt-oss-20b",
                    groq_api_key=groq_api_key,
                    temperature=0.7
                )
                prompt= f"""
                You are an expert AI learning mentor.

                Create a personalized learning roadmap.

                Student Name: {name}
                Subject: {topic}
                Skill Level: {level}
                Learning Goal: {goal}
                Daily Study Hours: {hours}
                Duration: {duration}

                Include:
                1. Learning objectives
                2. Week-by-week roadmap
                3. Daily study schedule
                4. Practical exercises
                5. Mini projects
                6. Learning resources

                Use simple explanations and clear headings.
                """
                response=llm.invoke(prompt)
                st.subheader("📚 Your Personalized Learning Path")
                st.markdown(response.content)
        except Exception as e:
            st.error(f"Error : {e}")