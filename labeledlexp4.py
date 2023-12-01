#**********************Description*********************
# This code first clean the received raw text and the
# Annotate the data saving all in outcsv file
#*****************************************************
import xlrd
import csv
import cleanfile as cf #Step 1 : code to clean the raw text
import pandas as pd
import numpy as np ##python library for vectors of words
import selcworcopy as cw #Select the emotion lexicon for the relevant word
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
#This function calls the cleanfile functionality
#and returns cleaned text 
def cleaning(dfilename): #Received raw data CSV
 df = pd.read_csv(dfilename,encoding='mac_roman')
 df = df[df['Text'].notna()] #drop empty line
 text1 = df['Text']
 print("Dataset format")
 print(df.head(5)) #print raw data frame
 print("")
 print("# of Tweets/Sentences :",len(text1))
 cleantext=cf.main(text1) # applying cleaning
 Ctext=cleantext
 return Ctext

#This function returns found lexicon along with rown number
#of the CSV file
def checkword(txt,sheet): #Lexicon list and a tweet/sentence
  
  flag=0
  for w in txt: #for each word search for emotion lexicon
     
      if(flag):
          break
      for row_num in range(1,sheet.nrows): #searching         
        cellvalue=sheet.cell_value(row_num, 0)
        if(w==cellvalue):
            
            flag=1
            break
  return flag,cellvalue,row_num

#This function annotates the Mixed codes , Roman Urdu and Englis 
def open_file(path, Ctext,lexilistuo,outfile,indexf): #Parameters  
     print("Wait for few seconds......")
     wb = xlrd.open_workbook(path)  #open (Exel)sheet
     f = open(outfile,'w',encoding='UTF8',newline='') #create empty outfile CSV
     writer = csv.writer(f)#writer is ready
     
     l1=[]
     l1.append("Text")
     l1.append("Lexicon")
     l1.append("Emotion")
     l1.append("Sentiments")
     l1.append("Mood")
     writer.writerow(l1)#write headings for each column
     #Emty the container for next row
     l1.pop()
     l1.pop()
     l1.pop()
     l1.pop()
     l1.pop()
     #Variables to perform certain checks
     check1=0
     check2=0
     temp1=0
     flag=0
     #setting up the (Exel)sheet at first row
     sheet = wb.sheet_by_index(0)
     sheet.cell_value(1, 0)
     for i in range(0,indexf):#check for each tweet/sentence of cleaned text
      row=0
      temp1=0
      flag=0
      text=Ctext[i]#first tweet/sentence
     
      l1.append(Ctext[i])
      text=[w.lower() for w in text.split()]#tokenized text
      t,lex,ratio,rown=cw.main(text,lexilistuo)#find if Roman Urdu lexicon exists
      temp2=lex #save the lexicon 
      #print(t,lex,ratio,rown)
      if(t==0):
          check2=0
          check1,temp1,row=checkword(text,sheet)#Finding other posibilities for instance first word of the sentence
      else:                                    #is a "neutral" lexicon, then it will search if there is any other
           check1=0                             #lexicon that represents an emotion
           check2=1
           row=rown
      #print(check1,temp1,row)
      
      if(check1):
            v=temp1   #adding type as EU: engllish
            l="(EU)"
      else:
            v=temp2     #or RU Roman Urdu
            l="(RU)"
      v1=sheet.cell_value(row,3) #getting corresponding emotion label
      #print(v1)
      v2=sheet.cell_value(row,4) #Sentiment Label
      #print(v2)
      v3=sheet.cell_value(row,5) #and Mood Label
      #print(v3)
      #print("check1",check1,"check2", check2)
      if (check1 or check2): #adding row to CSV file
            v=v+l
            l1.append(v.lower())
            l1.append(v1)
            l1.append(v2)
            l1.append(v3)
            #print(v,v1,v2)
            writer.writerow(l1)
            l1.pop()
            l1.pop()
            l1.pop()
            l1.pop()
            l1.pop()
            flag=1
      if(flag==0): #if no lexicon has been found then add 'lex not found'
            v1="Neutral"
            v="lex not found"
            v2="Neutral"
            v3="Moderate"
            l1.append(v)
            l1.append(v1)
            l1.append(v2)
            l1.append(v3)
            writer.writerow(l1)
            l1.pop()
            l1.pop()
            l1.pop()
            l1.pop()
            l1.pop()
           
     f.close() #close the CSV file


#main function
def main(textfile,outfile):
     
     
     lexlist=[]
     weighlist=[]
     path1=r'C:\Users\Bahria\AppData\Local\Programs\Python\Python39\MLXISUPOORTRU.xlsx'
     wb = xlrd.open_workbook(path1)
     dfilename=textfile #input file
     Ctext=cleaning(dfilename) #sent to cleanfile
     
     sheet = wb.sheet_by_index(0)#open lexicon (Exel) sheet
     for row_num in range(1,sheet.nrows): #make the list of lexicons
    
          lexlist.append(sheet.cell_value(row_num, 1).lower())# adding priority to Non-Neutral lexicons
          weighlist.append(sheet.cell_value(row_num, 2))

     lexilist = list(zip(lexlist, weighlist)) # combine the lexicons and priporities
     lexilistuo=lexilist
     indexf=len(Ctext) # no. of Cleaned tweets/Sentences
     open_file(path1,Ctext,lexilist,outfile,indexf)# returns annotated file as outfile (CSV)
     
     



if __name__ == "__main__":
   main()
