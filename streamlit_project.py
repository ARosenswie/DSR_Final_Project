import streamlit as st

st.markdown("# *MAG* (Medical Advice Generator)")

st.header("Introducing *MAG*, an educational tool to assist doctors studying for the Kenntnisprüfung in Germany.")

#Insert Designer's Names
st.subheader("Designed and written by: ")
st.write("1. Kátia M. Barros,")
st.write("2. Juan Brugada,")
st.write("3. and Andrew Rosenswie.")

st.subheader("Within this application, we employ a Large Language Model (LLM) from OpenAI. Provided is the analysis of medical question and answer pairs (167,793).")



# insert a text box for users to input OpenaAI API key
st.subheader("Please enter your OpenAI API key below:")

# insert a text box for users to input a question to the model
st.subheader("Please enter your medical question below:")

# Provide the output of the model
st.subheader("The model's answer to your question is:")
st.write("Answer:")

st.subheader("Data Sources:")
st.write("1. PubMedQA: Jin et al., 2019")
st.write("2. MedQA: Jin et al., 2020")
st.write("3. MMLU: Hendrycks et al., 2020")