import pandas as pd


url = 'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

for val in data.title.head():
    print(val)

print()

for index, row in data.head().iterrows():
    print(index, row.title, row.genre, sep=' - ')