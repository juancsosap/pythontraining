import pandas as pd


# Reading DataFrame from URL
url = 'http://bit.ly/uforeports'
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
print(data.ix[0].head(), end='\n\n')

# Accessing using index id
print(data.iloc[0].head(), end='\n\n')
print(data.ix[0].head(), end='\n\n')

# Verifying Series Type
print('TYPE: ', type(data['City']), end='\n\n')

# Creating new Series in the DataFrame
data['Location'] = data.City + ', ' + data.State
print(data.Location.head(), end='\n\n')

# Reading only selected DataFrame columns' from URL
data = pd.read_csv(url, usecols=['City', 'State'])
print(data.head())
print(data.shape, end='\n\n')

# Reading only the first 100 DataFrame rows' from URL
data = pd.read_csv(url, usecols=[0, 3], nrows=100)
print(data.head())
print(data.shape, end='\n\n')
