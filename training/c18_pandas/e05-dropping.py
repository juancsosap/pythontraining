import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'data/uforeports.csv'   #'http://bit.ly/uforeports'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

data.drop('Colors Reported', axis=1, inplace=True)

print(data.head(), end='\n\n')

data.drop(['City', 'State'], axis=1, inplace=True)

print(data.head(), end='\n\n')

data.drop([0, 1], axis=0, inplace=True)

print(data.head(), end='\n\n')

# data.dropna -> drop loss data
# data.replace
# np.nan -> Not a number
