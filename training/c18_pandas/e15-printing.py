import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)
os.chdir('..')

url = 'data/drinksbycountry.csv'
headers = ['COUNTRY', 'BEER', 'SPIRIT', 'WINE', 'ALCOHOL', 'CONTINENT']
data = pd.read_csv(url, header=0, names=headers)
print(data, end='\n\n')

pd.options.display.max_rows = 4
pd.options.display.max_columns = 5
pd.options.display.float_format = '{:,.2f}'.format
pd.options.display.max_colwidth = 10

print(data, end='\n\n')
