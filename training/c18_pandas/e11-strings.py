import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'data/chiporders.data'  #'http://bit.ly/chiporders'
data = pd.read_table(url)
print(data.head(), end='\n\n')

# STR UPPER Method
serie = data.item_name.str.upper()
print(serie.head(), end='\n\n')

# STR CONTAINS Method
serie = data.item_name.str.contains('Chicken')
print(serie.head(), end='\n\n')
print(data[serie].head(), end='\n\n')

# STR cascade Methods
datafilter1 = ~data['choice_description'].isnull()
print(data.shape, end='\n\n')
cleandata = data[datafilter1]
print(cleandata.shape, end='\n\n')
datafilter2 = cleandata['choice_description'].str.lower().str.contains('chicken')
chickendata = cleandata[datafilter2]
print(chickendata.shape, end='\n\n')
print(chickendata.head(), end='\n\n')
chickendata['choice_description'] = chickendata.choice_description.str.replace('[', '').str.replace(']', '')
print(chickendata.head(), end='\n\n')
