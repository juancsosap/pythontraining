import pandas as pd


url = 'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

print(data.shape, '\n')

condition = data.duration >= 200
filtered_data = data[condition]
print(filtered_data.title.head(), '\n')

condition = (data.duration >= 200) & (data.genre == 'Drama')
filtered_data = data[condition]
print(filtered_data.title.head(), '\n')

condition = (data.duration >= 200) & ((data.genre == 'Drama') | (data.genre == 'Action'))
filtered_data = data[condition]
print(filtered_data.title.head(), '\n')

condition = (data.duration >= 200) & data.genre.isin(['Drama', 'Action', 'Crime'])
filtered_data = data[condition]
print(filtered_data.title.head(), '\n')

condition = data.isnull();
filtered_data = data[condition]
print(filtered_data.title.head(), '\n')
