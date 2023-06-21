
# !pip install langchain==0.0.148
# !pip install rouge
import streamlit as st
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

def ask_ai():
    index = GPTSimpleVectorIndex.load_from_disk('./Data/index.json')
    while True:
        query = input("What do you want to ask? ")
        response = index.query(query)
        display(Markdown(f"<b>{response.response}</b>"))


st.markdown("# *MAG* (Medical Advice Generator)")

st.header("Introducing *MAG*, an educational tool to assist doctors studying for the Kenntnisprüfung in Germany.")

#Insert Designer's Names
st.subheader("Designed and written by: ")
st.write("1. Kátia M. Barros,")
st.write("2. Juan Brugada,")
st.write("3. and Andrew Rosenswie.")

st.subheader("Within this application, we employ a Large Language Model (LLM) from OpenAI. Provided is the analysis of medical question and answer pairs (570,712).")


# Insert a text box for users to input OpenAI API key
st.subheader("Please enter your OpenAI API key below:")
openai_api_key = st.text_input("Enter OpenAI key:")

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = openai_api_key

# insert a text box for users to input a question to the model
st.subheader("Please enter your medical question below:")
user_question = st.text_input("Submit your question:")

def ask_ai(query):
    index = GPTSimpleVectorIndex.load_from_disk('./Data/index.json')
    response = index.query(query)
    display(Markdown(f"<b>{response.response}</b>"))

# Example usage:
if user_question:
    ask_ai(user_question)

st.subheader("Data Sources:")
st.write("1. PubMedQA: Jin et al., 2019")
st.write("2. MedQA: Jin et al., 2020")
st.write("3. MMLU: Hendrycks et al., 2020")