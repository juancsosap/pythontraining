import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = '../data/uforeports.csv'   #'http://bit.ly/uforeports'
data = pd.read_csv(url)

condition = (data['Shape Reported'] == 'SPHERE')
filtered_data = data[condition]

sortered_data = filtered_data.sort_values('Time', ascending=False)

result_data = sortered_data.drop('Shape Reported', axis=1)

result_data.rename(columns={'Colors Reported': 'Color'}, inplace=True)

print(result_data.head())
