import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

# ## Data Types ##
#
# object  -> str
# int64   -> int
# float64 -> float
# bool    -> bool
# datetime64
# timedelta
# category

url = 'data/drinksbycountry.csv'  #'http://bit.ly/drinksbycountry'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

# Initial Data Types
print(data.dtypes, end='\n\n')

# Changing Data Types
data['beer_servings'] = data['beer_servings'].astype(float)
print(data.dtypes, end='\n\n')

# Changing Data Types during the reading
data = pd.read_csv(url, dtype={'beer_servings': float})
print(data.head(), end='\n\n')
print(data.dtypes, end='\n\n')

# Loading Data with wrong Data Type
url = 'data/chiporders.data'  #'http://bit.ly/chiporders'
data = pd.read_table(url)
print(data.head(), end='\n\n')
print(data.dtypes, end='\n\n')

print(data.item_price.head(), end='\n\n')

print('MEAN: ', data.item_price.str.replace('$', '').astype(float).mean())
