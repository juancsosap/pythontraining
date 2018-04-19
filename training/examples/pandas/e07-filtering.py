import pandas as pd


url = 'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

print(data.shape, '\n')

condition = data.duration >= 200
sorted_data = data[condition]
print(sorted_data.title.head(), '\n')

condition = (data.duration >= 200) & (data.genre == 'Drama')
sorted_data = data[condition]
print(sorted_data.title.head(), '\n')

condition = (data.duration >= 200) & ((data.genre == 'Drama') | (data.genre == 'Action'))
sorted_data = data[condition]
print(sorted_data.title.head(), '\n')

condition = (data.duration >= 200) & data.genre.isin(['Drama', 'Action', 'Crime'])
sorted_data = data[condition]
print(sorted_data.title.head(), '\n')
