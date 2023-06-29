# DSR_Final_Project
Created by Kátia Barros, Juan Brugada, and Andrew Rosenswie, under the mentorship of Sina Rampe and Markus Hinsche.

## Motivation:
Germany is in the midst of a skilled labor shortage, which includes medical doctors (https://www.dw.com/en/germany-seeks-to-attract-foreign-skilled-workers/video-66016649). The solution for their problem is to bring international doctors in who can practice medicine.

## Purpose of Project
* In order for doctors to practice medicine, they have to pass a knowledge test (Kenntnisprüfung), irrespective of their career length.
* Therefore, we designed an interactive medical question and answer (Q&A) chatbot, titled *MAG* (Medical Advice Generator).
* Provided within this repositiory is the analysis of ~570K medical Q&A pairs taken from PubMedQA (Jin et al., 2019), MedQA (Jin et al., 2020), MMLU (Hendrycks et al., 2021), and MedMCQA (Pal et al., 2022).
* We utilized llama indexing from OpenAI using the Generative Pre-trained Transformer (GPT) model <tt>text-davinci-003</tt>, with inference temperature set to 0.1.

### Steps to run *MAG*
1. Go to "Releases" ([click here](https://github.com/ARosenswie/DSR_Final_Project/releases/tag/29.06.2023)),
2. Click on the Data_29.06.2023 button,
3. Download index.json.bz2,
4. Uncompress index.json.bz2,
5. Save it in the same folder where the cloned files are located,
6. Posses an OpenAI API key (needed for the running of *MAG*),
7. Open terminal window and create Conda environment in same folder,
8. To install all needed packages, run <tt>pip install -r requirements.txt</tt>,
9. Run <tt>streamlit run streamlit_project.py</tt> to have a local Streamlit application.
10. Insert your personal OpenAI API key,
11. Enter your medical question,
12. Sit back and enjoy the power of *MAG* :) .
