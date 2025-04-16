import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Langsmith Tracking (Optional)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "Langchain-Ollama-Demo")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with 🧠 Gemma (Ollama)")
input_text = st.text_input("What question do you have in mind?")

# Initialize Ollama LLM with explicit base_url (important if remote/port issues)
try:
    llm = Ollama(
        model="gemma:2b",
        base_url="http://localhost:11434"  # You can change this if exposing via tunnel
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
except Exception as e:
    st.error(f"Error initializing Ollama LLM: {e}")
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
