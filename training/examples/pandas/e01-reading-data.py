import pandas as pd


# Reading tabular data from URL (Good Default Formated)
url = 'http://bit.ly/chiporders'
data = pd.read_table(url)
print(data.head(), end='\n\n')

# Reading tabular data from URL (Bad Default Formated)
url = 'http://bit.ly/movieusers'
data = pd.read_table(url)
print(data.head(), end='\n\n')

# Reading tabular data from URL setting separator symbol
data = pd.read_table(url, sep='|')
print(data.head(), end='\n\n')

# Reading tabular data from URL without header
data = pd.read_table(url, sep='|', header=None)
print(data.head(), end='\n\n')

# Reading tabular data from URL defining header
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
data = pd.read_table(url, sep='|', header=None, names=user_cols)
print(data.head(), end='\n\n')

# Reading CSV file from URL using read_table and separator
url = 'http://bit.ly/uforeports'
data = pd.read_table(url, sep=',')
print(data.head(), end='\n\n')

# Reading CSV file from URL using read_csv
data = pd.read_csv(url)
print(data.head(), end='\n\n')
