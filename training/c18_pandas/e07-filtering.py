import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)
os.chdir('..')

url = 'data/imdbratings.csv'  #'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

print(data.shape, '\n')

condition = data.duration >= 200
filtered_data = data[condition]
# data = data[data.duration >= 200]
print(filtered_data.head(), '\n')

condition = (data.duration >= 200) & (data.genre == 'Drama')
filtered_data = data[condition]
print(filtered_data.head(), '\n')

condition = (data.duration >= 200) & ((data.genre == 'Drama') | (data.genre == 'Action'))
filtered_data = data[condition]
print(filtered_data.head(), '\n')

condition = (data.duration >= 200) & data['genre'].isin(['Drama', 'Action', 'Crime'])
filtered_data = data[condition]
print(filtered_data.head(), '\n')

condition = data['content_rating'].isnull()
filtered_data = data[~condition]
print(filtered_data.head(), '\n')
