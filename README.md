# DSR_Final_Project
Created by Kátia Barros, Juan Brugada, and Andrew Rosenswie, under the mentorship of Sina Rampe and Markus Hinsche.


## Purpose of Project
* We designed a medical Q&A chatbot, titled *MAG* (Medical Advice Generator).
* Our project's goal is to assist medical doctors who wish to continue their career in Germany, however this can be done with the passing of the 'Kenntnisprüfung'.
* Provided within this repositiory is the analysis of ~570K medical question and answer (Q&A) pairs (insert amount here) taken from (PubMedQA; Jin et al., 2019), (MedQA; Jin et al., 2020), Massive Multi-task Language Understanding (MMLU; Hendrycks et al., 2021), and (MedMCQA; Pal et al., 2022).
* We utilized a llama index from OpenAI using the Generative Pre-trained Transformer (GPT) model <tt>text-davinci-003</tt>.

### Steps to run *MAG*
1. Go to releases (right hand side of the GitHub repository),
2. Click on the Data_29.06.2023 button,
3. Download index.json.bz2,
4. Uncompress index.json.bz2,
5. Save it in the same folder where the cloned files are located,
6. Posses an OpenAI API key (Needed for the running of *MAG*),
7. Run <tt>streamlit_project.py</tt> to have a local app.
..
