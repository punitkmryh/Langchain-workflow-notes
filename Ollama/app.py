import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms.ollama import Ollama  # ✅ Fixed import
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Set up environment
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt setup
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant.'),
        ('user', 'Question: {question}')
    ]
)

# Streamlit UI
st.title('LangChain + Ollama (Gemma3) Demo')
input_text = st.text_input("What's on your mind?")

# Ollama LLM
llm = Ollama(model='gemma3')  # ✅ Fixed this line
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write('Response:')
    st.write(response)
