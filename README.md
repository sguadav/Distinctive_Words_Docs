# Distinctive_Words_Docs

Finding distinctive words between txt documents

This program uses the Term Frequency-Inverse Document Frequency numerical statistic analysis to find the 5 most distinctive words between a list of txt files. This can be used to see how two files differenciate each other and have a summary in 5 words about it. This project was done through my Python for Data Science Course at Purdue University.

Getting Started
-
These are the following requirements for this program:
- Python 3.7
- Numpy
- Math
- String
- NLTK

To use this program and analyze your own files, open the doc_summary.py file and change lines 8, 9 and 10 to your own preferences.

<img src='images/lines_change.PNG' height=200>

Running the program
-
Running this program is very simple, if you want to use the txt files in the lecs folder then run the program as it is. If you want to change the files analyze, make sure that the file is correctly referenced and inside the list of files. It's recommendable to use a small number of txt files (2-5 files) if the general topic is similar, due to the way the TF-IDF numerical statistic works.

<img src='images/distinct_results.PNG' width=400>

Acknowledgments
-
- Purdue University
- Prof. Milind Kulkarni
