import pandas as pd


url = 'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

serie = data.title.sort_values()
print(serie.head(), end='\n\n')

serie = data.title.sort_values(ascending=False)
print(serie.head(), end='\n\n')

print(data.title.head(), end='\n\n')

sorted_data = data.sort_values('duration', ascending=False)
print(sorted_data.title.head(), end='\n\n')

sorted_data = data.sort_values(['content_rating', 'duration'], ascending=False)
print(sorted_data.head(), end='\n\n')

print(data.head(), end='\n\n')
