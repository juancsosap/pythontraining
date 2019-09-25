import pandas as pd
import os
#import xlrd 

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

# Reading tabular data from URL (Good Default Formated)
url = 'data/chiporders.data'  #'http://bit.ly/chiporders'
data = pd.read_table(url) # Deprecated
print(data.head(), end='\n\n')

# Reading tabular data from URL (Bad Default Formated)
url = 'data/movieusers.data'  #'http://bit.ly/movieusers'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

# Reading tabular data from URL setting separator symbol
data = pd.read_csv(url, sep='|')
print(data.head(), end='\n\n')

# Reading tabular data from URL without header
data = pd.read_csv(url, sep='|', header=None)
print(data.head(), end='\n\n')

# Reading tabular data from URL defining header
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
data = pd.read_csv(url, sep='|', header=None, names=user_cols)
print(data.head(), end='\n\n')

# Reading CSV file from URL using read_csv
url = 'data/uforeports.csv'   #'http://bit.ly/uforeports'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

#wb = xlrd.open_workbook(path)
#data = pd.read_excel(wb)
