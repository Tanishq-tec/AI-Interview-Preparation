# THIS IS THE MODEL WHERE THE USER ONLY HAS TO SELECT THEIR INPUT FROM THE DROPDOWN MENU AND WILL GET THE OUTPUT ACCORDINGLY
from urllib import response
import streamlit as st
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    max_new_tokens=4000
)

chat_model=ChatHuggingFace(llm=llm)

st.set_page_config(page_title="🤖 AI Interview Preparation", page_icon="🧠🤖")
st.image("Interview.png", width=150)
st.header('🤖 AI Interview Preparation')

job_role=st.selectbox('Select the level of expertise',['Beginner','Intermediate','Advanced','Expert'])
experience=st.selectbox('Select the experience level',['Beginner','Intermediate','Advanced','Expert'])
interview_type=st.selectbox('Select the interview type',['Technical','Behavioral','Mixed','HR'])
skill_focus=st.selectbox('Select the skill focus',['Data Science','Software Development','System Design','DevOps','Product Management','Machine Learning','Cloud Computing','Cybersecurity','PYTHON','JAVA','C++','JavaScript','SQL'])

template=load_prompt('template.json')
parser=StrOutputParser()

prompt_input={
    'job_role':job_role,
    'experience':experience,
    'interview_type':interview_type,
    'skill_focus':skill_focus
}

if st.button("Start Interview Prep"):
    chain=template|chat_model|parser
    recommendation=chain.invoke(prompt_input)
    recommendation = (
    recommendation.replace("<br>", "\n")\
    )
    st.write(recommendation)