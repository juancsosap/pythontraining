import pandas as pd
import matplotlib.pyplot as plt
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)
os.chdir('..')

# Reading data
url = 'data/uforeports.csv'
columns = ['city', 'color', 'shape', 'state', 'time']
data = pd.read_csv(url, header=0, names=columns)
print(data.head(), end='\n\n')

print(data.dtypes, end='\n\n')
print(data.describe(), end='\n\n')

data['color'].fillna('UNDEFINED',inplace = True)
data['shape'].fillna('OTHER',inplace = True)
print(data.head(), end='\n\n')

colors = data['color'].unique()
print(colors, end='\n\n')

data['r_color'] = data['color'].str.contains('RED')
data['g_color'] = data['color'].str.contains('GREEN')
data['b_color'] = data['color'].str.contains('BLUE')
data['o_color'] = data['color'].str.contains('ORANGE')
data['y_color'] = data['color'].str.contains('YELLOW')
data.drop('color', axis=1, inplace=True)
print(data.head(), end='\n\n')

shape_cat = pd.Categorical(data['shape'])
print(shape_cat.categories, end='\n\n')

data['shape'] = pd.Categorical(data['shape']).codes
print(data.head(), end='\n\n')
