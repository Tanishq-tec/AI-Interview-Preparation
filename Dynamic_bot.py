import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/ministral-8b-2512",
    temperature=0.7,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "LangChain Chatbot"
    }
)

st.set_page_config(page_title="🤖 AI Interview Preparation", page_icon="🧠🤖")
st.image("Interview.png", width=150)
st.header("🤖 AI Interview Preparation")

job_role = st.selectbox(
    "Select the level of expertise",
    ["Beginner", "Intermediate", "Advanced", "Expert"]
)

experience = st.selectbox(
    "Select the experience level",
    ["Beginner", "Intermediate", "Advanced", "Expert"]
)

interview_type = st.selectbox(
    "Select the interview type",
    ["Technical", "Behavioral", "Mixed", "HR"]
)

skill_focus = st.selectbox(
    "Select the skill focus",
    [
        "Data Science", "Software Development", "System Design",
        "DevOps", "Product Management", "Machine Learning",
        "Cloud Computing", "Cybersecurity",
        "PYTHON", "JAVA", "C++", "JavaScript", "SQL"
    ]
)

template = load_prompt("template.json")
parser = StrOutputParser()

prompt_input = {
    "job_role": job_role,
    "experience": experience,
    "interview_type": interview_type,
    "skill_focus": skill_focus
}

if st.button("Start Interview Prep"):
    chain = template | llm | parser  
    recommendation = chain.invoke(prompt_input)
    st.write(recommendation.replace("<br>", "\n"))

