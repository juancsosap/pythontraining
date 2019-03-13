import pandas as pd
import matplotlib.pyplot as plt


url = 'http://bit.ly/drinksbycountry'
data = pd.read_csv(url)
print(data.head(), end='\n\n')

countries = ['Chile', 'Colombia', 'Peru', 'Argentina']
graph = data[data.country.isin(countries)].plot(kind='barh')

print(type(graph), '\n')

data.groupby('continent').mean().plot.bar()

plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.25)

plt.show()
