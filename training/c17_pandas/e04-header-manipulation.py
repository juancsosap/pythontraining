import pandas as pd


url = 'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

print(data.columns, end='\n\n')

data.rename(columns={'content_rating': 'rating'}, inplace=True)
print(data.columns, end='\n\n')

data_cols = ['star_rating', 'title', 'contentrating', 'genre', 'duration', 'actors_list']
data.columns = data_cols
print(data.columns, end='\n\n')

data = pd.read_csv(url, names=data_cols, header=0)
print(data.columns, end='\n\n')

data.columns = data.columns.str.replace('_', '')
print(data.columns, end='\n\n')