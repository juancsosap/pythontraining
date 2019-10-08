import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)
os.chdir('..')

# Loading data
url = 'data/imdbratings.csv'  #'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

# Sort serie ascending
serie = data.title.sort_values()
print(serie.head(), end='\n\n')

# Sort serie descending
serie = data['title'].sort_values(ascending=False)
print(serie.head(), end='\n\n')

# Original serie data is not affected
print(data.title.head(), end='\n\n')

# Sort dataframe by one column
sorted_data = data.sort_values('duration', ascending=False)
print(sorted_data.head(), end='\n\n')

# Sort dataframe by many columns
sorted_data = data.sort_values(['star_rating', 'duration'], ascending=False)
print(sorted_data.head(10), end='\n\n')

# Original dataframe data is not affected
print(data.head(), end='\n\n')
