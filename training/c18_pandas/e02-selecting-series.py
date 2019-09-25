import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

# Reading DataFrame from URL
url = 'data/uforeports.csv'   #'http://bit.ly/uforeports'
data = pd.read_csv(url)
print('LOADED DATA')
print(data.head(), end='\n\n')

# Verifying DataFrame Type
print('TYPE: ', type(data), end='\n\n')

# Accessing Series using [] notation
print('CITY SERIES')
print(data['City'].head(), end='\n\n')

# Accessing using Dot notation
print(data.City.head(), end='\n\n')

# Accessing using index name
print('FIRST ROW')
print(data.loc[0].head(), end='\n\n')

# Verifying Series Type
print('TYPE: ', type(data['City']), end='\n\n')

# Creating new Series in the DataFrame
data['Location'] = data.City + ', ' + data.State
print(data.head(), end='\n\n')

# Reading only selected DataFrame columns' from URL
data = pd.read_csv(url, usecols=['City', 'State'])
print(data.head())
print(data.shape, end='\n\n')

# Reading all and only selected DataFrame columns' from URL
data = pd.read_csv(url, nrows=100)
datafilter = data[['State', 'City']]
print(datafilter.head())
print(datafilter.shape, end='\n\n')

# Reading only the first 100 DataFrame rows' from URL
data = pd.read_csv(url, usecols=[0, 3], nrows=100)
print(data.head())
print(data.shape, end='\n\n')
