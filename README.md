# RU-automatic-emotion-annotation
%This  work details the automatic creation of a emotions labeled  dataset for a short Roman Urdu-English mixed text, describing the lack of specific structure or grammar rules in Roman Urdu. The development of the software consists of two phases: cleaning and automatic annotation of raw text and classification of emotion and prediction, respectively. This software simplifies the creation of new datasets applying NLP methods particularly for mixed codes of Roman Urdu and English . 
# Functionality
This software makes the process of developing a new dataset hassle-free, especially for mixed RU and English wordings.

% Getting input CSV and perform cleaning and annotation then returns annoted CSV(Behavemo.py)

Cleaning of data(cleanfile.py):

Behavemo.py calls cleanfile.py to remove tags, web addresses,Urdu useless words and other unncessarydata such as especial characters.

Annotation of clean data (labeledlexp4.py):

calling the list of lexicons of emotions for Roman Urdu and then matching each word of a clean sentence to find the right emotion, sentiment, and mood.

% Getting annoted CSV and performs classification of emotions and predition  (behavpap.py) 
Prediction and classification:

Uses Multinomial Naive Bayes, Logistic Regression and SVM for classification and prediction for some new text .
