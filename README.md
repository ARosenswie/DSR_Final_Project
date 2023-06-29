# DSR_Final_Project (Data Source)

## Methods
* We accessed different public data sources and made question and answer (Q&A) pairs from each dataset (e.g. when incorrect optional answers or context and methods were given, they were deleted).
* With the formated data from each dataset, we then grouped it together and perfomed data cleaning, generating two files (Download the <tt>train_output.txt</tt> and <tt>test_output.txt</tt> files inside 'Release' ([click here](https://github.com/ARosenswie/DSR_Final_Project/releases/tag/29.06.2023)) ).
* Apart from that, 36 Q&A were extracted from five different medical textbooks for the validation of the model.
* The questions with their answers provided by the book and by MAG can be found at <tt>MAG_q_a.csv</tt>.
* Various metrics can also be found at <tt>Evaluating_MAG.ipynb</tt>.

 
## Data Sources:
1. PubMedQA (Jin et al., 2019)
   - 273,387 Q&A,
2. MedQA (Jin et al., 2020)
   - 12,721 Q&A,
3. MMLU (Hendrycks et al., 2021),
   - 100,338 Q&A,
4. and MedMCQA (Pal et al., 2022)
   - 187,005 Q&A.
