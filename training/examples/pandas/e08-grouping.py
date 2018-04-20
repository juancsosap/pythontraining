import pandas as pd


url = 'http://bit.ly/drinksbycountry'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

print(data.shape, '\n')

print('Groups:')
for group in data.groupby('continent').groups:
    print(group)

print()

for group_name, group_df in data.groupby('continent'):
    print(group_name)
    print(group_df['country'].head())

print()

print('AFRICA GROUP:\n', data.groupby('continent').get_group('Africa').country.head())

print('MEAN Total: ', data.beer_servings.mean(), '\n')

print('MEAN Europe: ', data[data.continent == 'Europe'].beer_servings.mean(), '\n')

print('MEAN:\n', data.groupby('continent').beer_servings.mean(), '\n')
print('MAX:\n', data.groupby('continent').beer_servings.max(), '\n')
print('MIN:\n', data.groupby('continent').beer_servings.min(), '\n')
print('COUNT:\n', data.groupby('continent').beer_servings.count(), '\n')

print('AGG:\n', data.groupby('continent').beer_servings.agg(['count', 'max', 'min', 'mean']), '\n')

print('MEAN:\n', data.groupby('continent').mean(), '\n')
