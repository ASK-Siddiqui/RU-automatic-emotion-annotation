#**********************Description*********************************
# This code sends input CSV (incsv) to clean theraw text and then
# display the contents of annotated output CSV file (outcsv)
#*******************************************************************
import cleanfile as cf #cleaning Module
import pandas as pd    # Python library to get data frames
import labeledlexp4 as ll #annotation module

#Phase 1
incsv='paper4RU.csv'
outcsv='myannoRU.csv'
ll.main(incsv,outcsv) # calling main function
pd.set_option('max_row', None)  #Show contents of all rows
pd.set_option('display.max_columns', None) #Show contents of all columns
print("")
print('File annotated..')
print("")
df = pd.read_csv(outcsv,encoding='mac_roman') #open output CSV file as data frame
print(df.head(5)) #display contents of first 5 lines
