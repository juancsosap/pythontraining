import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'data/drinksbycountry.csv'  #'http://bit.ly/drinksbycountry'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

# Droping Column
sub_data = data.drop('continent', axis=1)
print(sub_data.head(), end='\n\n')

# Droping Row
sub_data = data.drop(2, axis=0)
print(sub_data.head(), end='\n\n')

# Calculate the Mean per Column (default)
print(data.mean(axis=0), '\n')
print(data.mean(axis='index'), '\n')

# Calculate the Mean per Row
print(data.mean(axis=1).head(), '\n')
print(data.mean(axis='columns').head(), '\n')
