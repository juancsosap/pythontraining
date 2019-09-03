import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'data/drinksbycountry.csv'  #'http://bit.ly/drinksbycountry'
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

print('\nMEAN Total: ', data.beer_servings.mean(), '\n')

print('MEAN Europe: ', data[data.continent == 'Europe'].beer_servings.mean(), '\n')

print('MEAN:\n', data.groupby('continent').beer_servings.mean(), '\n')
print('MAX:\n', data.groupby('continent').beer_servings.max(), '\n')
print('MIN:\n', data.groupby('continent').beer_servings.min(), '\n')
print('COUNT:\n', data.groupby('continent').beer_servings.count(), '\n')

print('AGG:\n', data.groupby('continent').beer_servings.agg(['count', 'max', 'min', 'mean']), '\n')

print('MEAN:\n', data.groupby('continent').beer_servings.describe(), '\n')

print('MEAN:\n', data.groupby('continent').mean(), '\n')
