import os
from dotenv import load_dotenv
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain + Groq 🔥 | Mixtral Demo")
input_text = st.text_input("What question do you have in mind?")

# LLM Setup
try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.environ["GROQ_API_KEY"]
    )

    chain = prompt | llm | StrOutputParser()
except Exception as e:
    st.error(f"Error initializing Groq LLM: {e}")
    st.stop()

# Inference
if input_text:
    try:
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": input_text})
        st.success("Response:")
        st.write(response)
    except Exception as e:
        st.error(f"Error while generating response: {e}")
