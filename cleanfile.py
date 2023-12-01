#***************Description***********************************
#This code will return the clean text in term of list of words
#**************************************************************
#All functions to perform  NLP tasks

from bs4 import BeautifulSoup
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import re

RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
#Functions for NLP
#Returns lowercase text
def Make_LowerCase(inputext):
   #inputext=str(inputext)
  return inputext.lower()
#Returns text without punctuation
def Remove_Punctuation(inputext):
 
  return inputext.translate(str.maketrans('','', string.punctuation))
# Returns text without extra whitespaces
def Remove_Whitespaces(inputext):
 
  return " ".join(inputext.split())
# Returns text without HTML tags 
def Remove_HtmlTags(inputext):
  soup = BeautifulSoup(inputext, "html.parser")
  stripped_input = soup.get_text(separator=" ")
  return stripped_input
#Returns ascii characters
def Remove_Nonascii(a_str):
    ascii_chars = set(string.printable)

    return ''.join(filter(lambda x: x in ascii_chars, a_str))
#Returns text removin all unnecessary tags/symbils
def Remove_Otags(text1):
  text1 = " ".join([word for word in text1.split()
                                if 'http' not in word and '@' not in word and '<' not in word and '#' not in word])
  text1= re.sub('[!@#$:).;,?&]', '', text1.lower())
  text1= re.sub('  ', ' ', text1)
  text1=Remove_Nonascii(text1)
  return text1
#Returns tokenized version of text
def tokenize(inputext):
  return word_tokenize(inputext)
#Returns text without stop words
def Remove_RUEstopwords(inputext):
  stopwordsu=open("stopwords.txt","r").read()
  inputext = word_tokenize(inputext)
  return [word for word in inputext if word not in stopwords.words('english')and word not in stopwordsu]
#Returns no. of repeatitions of characer c 
def CCount(word):
    l=0
    for c in word:
       l=l+1
       
    return l
#Remove useless words
def Remove_UselessWords(inputext):
    inputext = word_tokenize(inputext)
    
    new_words=[]
    for w in inputext:
       
        if CCount(w)<3 :
            continue
        else:
            new_words.append(w)
    return ' '.join(new_words)

#Remove Repeated characters
def Remove_Repeatdc(inputext):
    inputext = word_tokenize(inputext)
    
    new_words=[]
    for w in inputext:
       if (w=="allah"):
         continue
       w=w+' '+' '

       t=''
       for c in range(len(w)):
          if(w[c]==' '):
            break
          if(w[c]==w[c+1]==w[c+2]):
            continue
          else:
            t=t+w[c]
       new_words.append(t)
       
    return ' '.join(new_words)
#Lemmatizes input using NLTK's WordNetLemmatizer
def Make_Lemmatize(inputext):
  lemmatizer=WordNetLemmatizer()
  input_str=word_tokenize(inputext)
  new_words = []
  for word in input_str:
    new_words.append(lemmatizer.lemmatize(word))
  return ' '.join(new_words)
#Returns text without emoji
def Remove_Emoji(inputext):
    return RE_EMOJI.sub(r'', inputext)
#NLP cleaning Pipeline
def NLP_pipeline(inputext):
  return Make_Lemmatize(' '.join(Remove_RUEstopwords(Remove_UselessWords(Remove_Repeatdc(Remove_Emoji(Remove_Whitespaces(Remove_Punctuation(Remove_Otags(Remove_HtmlTags(Make_LowerCase(inputext)))))))))))


def main(text):
  
    text2=[NLP_pipeline(x) for x in text]
    while("" in text2):
      text2.remove("")
    
    return text2

if __name__ == "__main__":
   main()


