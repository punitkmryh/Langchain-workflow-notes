# 📚 Complete Generative AI Application using LangChain, Streamlit & Open-Source LLMs (LLaMA/Gemma)

## 🎯 Objective

In this lecture, we will build a **Generative AI web application** using:

- **LangChain** for prompt management and chaining
    
- **Streamlit** for web interface
    
- **Ollama** for integrating **open-source LLMs** like LLaMA 2, Gemma, or Mistral
    
- No use of OpenAI — making it **cost-free and open-source**

![](https://github.com/punitkmryh/Ollama-chatbot-using-LangChain/blob/main/Ollama-langchain-chatbot.png)

---

## 🗂️ Project Structure

Our project folder is structured as follows:

```
langchain/
  └── 1.20_llama/
      ├── app.py
      ├── requirements.txt
      └── other necessary files
```

Make sure your terminal is pointed inside the correct folder (`1.20_llama`) when running Streamlit.

---

## ⚙️ Step 1: Setting Up the Environment

### 📄 Create `requirements.txt`

```txt
streamlit
langchain
langchain-community
ollama
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Step 2: Application Boilerplate (app.py)

### 🔹 Import Required Libraries

```python
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
```

> ✅ `langchain_community.llms.Ollama` allows you to run LLMs like `llama2`, `gemma`, etc. locally using Ollama backend.

---

## 📝 Step 3: Define Prompt Template

### 🔹 What is a Prompt Template?

A prompt template defines:

- System Instructions
    
- User Input Format
    

### 🔹 Example Code

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "{question}")
])
```

Here, `{question}` is a **placeholder** that will be dynamically filled with user input.

---

## 🧱 Step 4: Create LLM with Ollama

### 🔹 Load the Model

```python
llm = Ollama(model="gemma")  # or llama2, mistral etc.
```

Make sure the model is downloaded using:

```bash
ollama run gemma
```

To list available models:

```bash
ollama list
```

> 📦 You can switch models by changing the `model` argument.

---

## 🔄 Step 5: Output Parser and Chain Creation

### 🔹 What is an Output Parser?

It parses the model output string into usable text.

```python
output_parser = StrOutputParser()
```

### 🔹 Define the Chain

```python
chain = prompt | llm | output_parser
```

---

## 🎨 Step 6: Streamlit Frontend

### 🔹 Define UI Elements

```python
st.title("LangChain Demo with LLaMA2 / Gemma")

input_text = st.text_input("What question do you have in mind?")
```

### 🔹 Handle Response

```python
if input_text:
    response = chain.invoke({"question": input_text})
    st.write("Response:")
    st.write(response)
```

---

## 🚀 Step 7: Running the Application

Make sure you're inside the folder `1.20_llama` where `app.py` is located.

Run:

```bash
streamlit run app.py
```

It will launch a local server at `http://localhost:8501` displaying your app.

---

## 📌 Notes

- No OpenAI key is required.
    
- You can switch between models (`gemma`, `llama2`, `mistral`) just by changing the model name.
    
- Make sure the model is downloaded via Ollama before use.
    
- LangSmith tracking can be enabled optionally for performance monitoring and debugging.
    

---

## ✅ Final Thoughts

By the end of this, you will have:

- Built an interactive Generative AI App using **LangChain + Streamlit**
    
- Used **open-source LLMs** with **Ollama** backend (cost-free)
    
- Understood the full app architecture: **Prompt → LLM → Output Parser → UI**
    

---
