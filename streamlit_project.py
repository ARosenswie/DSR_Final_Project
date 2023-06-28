
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
#Insert Designer's Names
st.write("Designed and written by: Kátia M. Barros, Juan Brugada, and Andrew Rosenswie")
st.write("Supervised by: Sina Rampe and Markus Hinsche")

st.markdown("## Introducing *MAG*, an educational tool to assist international doctors studying for the Kenntnisprüfung in Germany.")


st.markdown("### Within this application, we employ a Large Language Model (LLM) from OpenAI. Provided is the analysis of medical question and answer pairs (~570K).")


# Insert a text box for users to input OpenAI API key
st.subheader("Please enter your OpenAI API key below:")
openai_api_key = st.text_input("", type="password")

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = openai_api_key

# insert a text box for users to input a question to the model
st.subheader("Please enter your medical question below:")
user_question = st.text_input("")

def ask_ai(query):
    index = GPTSimpleVectorIndex.load_from_disk('./Data/index.json')
    response = index.query(query)
    st.markdown(f"{response.response}")

# Example usage:
if user_question:
    ask_ai(user_question)

# make the soures below be a hyperlink


st.subheader("Data Sources:") 
# url to add is https://github.com/pubmedqa/pubmedqa
st.write("1. PubMedQA: Jin et al., 2019 (273,387 Q&A) [Click here for link](https://github.com/pubmedqa/pubmedqa)")
st.write("2. MedQA: Jin et al., 2020 (12,721 Q&A) [Click here for link](https://github.com/jind11/MedQA)")
st.write("3. MMLU: Hendrycks et al., 2021 (100,338 Q&A) [Click here for link](https://arxiv.org/abs/2009.03300v3)")
st.write("4. MedMCQA: Pal et al., 2022 (187,005 Q&A) [Click here for link](https://medmcqa.github.io/)")