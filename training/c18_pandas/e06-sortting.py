import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'data/imdbratings.csv'  #'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

serie = data.title.sort_values()
print(serie.head(), end='\n\n')

serie = data['title'].sort_values(ascending=False)
print(serie.head(), end='\n\n')

print(data.title.head(), end='\n\n')

sorted_data = data.sort_values('duration', ascending=False)
print(sorted_data.head(), end='\n\n')

sorted_data = data.sort_values(['star_rating', 'duration'], ascending=False)
print(sorted_data.head(10), end='\n\n')

print(data.head(), end='\n\n')
