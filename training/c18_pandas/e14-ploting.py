import pandas as pd
import matplotlib.pyplot as plt
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'data/drinksbycountry.csv'  #'http://bit.ly/drinksbycountry'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

countries = ['Chile', 'Colombia', 'Peru', 'Argentina']
datafilter = data.country.isin(countries)
dataclean = data[datafilter]
print(dataclean)
graph = dataclean.plot(kind='barh')
print(type(graph), '\n')

plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.subplots_adjust(bottom=0.25)

data.groupby('continent').mean().plot.bar()

plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.subplots_adjust(bottom=0.25)

plt.show()
