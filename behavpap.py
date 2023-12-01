#**********************Description*********************************
# This code reads the emotions annotated file(CSV) ,performs emotion,
#sentiment, mood classification and then show classification report
#and prediction report for some new (random)text 
#*******************************************************************

import nltk
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ignore the warnings
warnings.filterwarnings("ignore")
#reading dataset
conversation = pd.read_csv('myannobeha2.csv',encoding = "ISO-8859-1")
print("Dataset format")
print(conversation.head(3))
col = ['Text','Emotion','Sentiment','Mood']
conversation= conversation[col]
#setting up columns for processing
conversation.columns = ['Text','Emotion','Sentiment','Mood']
#showing graphical representation of data
print("Data Visualization")
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
conversation.groupby('Emotion').Text.count().plot.pie(ylim=0,autopct="%1.1f%%")
plt.show()
conversation.groupby('Sentiment').Text.count().plot.pie(ylim=0,autopct="%1.1f%%")
plt.show()
conversation.groupby('Mood').Text.count().plot.pie(ylim=0,autopct="%1.1f%%")
plt.show()
#method to display classification/prediction report
def classificationreport(clf,X_train,X_test,y_train,y_test,X_train_tfidf,T):
    print("Classification of :" + T + "")
    print("predicted result for 'main khan k khan se shadi karon gi.'")
    print("Predicted "+T+":")
    print(clf.predict(count_vect.transform(["main khan k khan se shadi karon gi."])))
    y_pred=clf.predict(count_vect.transform(X_test))
    #print("y-pred Emotion",y_pred)
    print("Accuracy of the classifier :",clf.score(X_train_tfidf, y_train))
    print("Accuracy score for test data :",accuracy_score(y_pred,y_test))

    y_true = y_test
    print (classification_report(y_true, y_pred))
#Splitting the dataset into training data and test data    
X_train, X_test, y_train, y_test = train_test_split(conversation['Text'], conversation['Emotion'],test_size=0.4, random_state = 0)
count_vect = CountVectorizer()
#Frequency counts
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
#TF-IDF vector
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#Prep[aring data for SEntiments
Xs_train, Xs_test, ys_train, ys_test = train_test_split(conversation['Text'], conversation['Sentiment'],test_size=0.4, random_state = 0)
Xs_train_counts = count_vect.fit_transform(Xs_train)
Xs_train_tfidf = tfidf_transformer.fit_transform(Xs_train_counts)
#Preparing data for Mood
Xm_train, Xm_test, ym_train, ym_test = train_test_split(conversation['Text'], conversation['Mood'],test_size=0.4, random_state = 0)
Xm_train_counts = count_vect.fit_transform(Xm_train)
Xm_train_tfidf = tfidf_transformer.fit_transform(Xm_train_counts)
#This function returns MNB classifier(Multinomial Naiv Bayes) handel
def ClassiMNB(X_train_tfidf, y_train):
    clf = MultinomialNB().fit(X_train_tfidf, y_train)
    return clf
#This function returns LR classifier(Logictic Regression) handel
def ClassiLR(X_train_tfidf, y_train):
     clf = LogisticRegression(random_state=0).fit(X_train_tfidf, y_train)
     return clf
#This function returns SVMclassifier(Super Vector Machine) handel
def ClassiSVM(X_train_tfidf, y_train):
     clf = SVC(C=1.0, kernel='linear', degree=3, gamma='auto').fit(X_train_tfidf, y_train)
     return clf
    
#**********************************************************************************************
#Calling the functions
print("************************MNB************************************")
clfM=ClassiMNB(Xm_train_tfidf, ym_train)
clfS=ClassiMNB(Xs_train_tfidf, ys_train)
clfE=ClassiMNB(X_train_tfidf, y_train)
classificationreport(clfE,X_train,X_test,y_train,y_test,X_train_tfidf,"Emotions")
classificationreport(clfS,Xs_train,Xs_test,ys_train,ys_test,Xs_train_tfidf,"Sentiments")
classificationreport(clfM,Xm_train,Xm_test,ym_train,ym_test,Xm_train_tfidf,"Mood")

#**************************************************************************************************
#Calling the functions
print("*********************LR*********************************************")
LRclfE = ClassiLR(X_train_tfidf, y_train)
LRclfS = ClassiLR(Xs_train_tfidf, ys_train)
LRclfM = ClassiLR(Xm_train_tfidf, ym_train)
classificationreport(LRclfE,X_train,X_test,y_train,y_test,X_train_tfidf,"Emotions")
classificationreport(clfS,Xs_train,Xs_test,ys_train,ys_test,Xs_train_tfidf,"Sentiments")
classificationreport(clfM,Xm_train,Xm_test,ym_train,ym_test,Xm_train_tfidf,"Mood")

#*****************************************************************************************************
#Calling the functionsf
print("***********************SVM***************************************")
from sklearn.svm import SVC
print("SVM for Emotion classification")
SVMclfE = ClassiSVM(X_train_tfidf, y_train)
SVMclfS = ClassiSVM(Xs_train_tfidf, ys_train)
SVMclfM = ClassiSVM(Xm_train_tfidf, ym_train)
classificationreport(SVMclfE,X_train,X_test,y_train,y_test,X_train_tfidf,"Emotions")
classificationreport(SVMclfS,Xs_train,Xs_test,ys_train,ys_test,Xs_train_tfidf,"Emotions")
classificationreport(SVMclfM,Xm_train,Xm_test,ym_train,ym_test,Xm_train_tfidf,"Emotions")
