import pandas as pd


url = 'http://bit.ly/chiporders'
data = pd.read_table(url)
print(data.head(), end='\n\n')

# STR UPPER Method
serie = data.item_name.str.upper()
print(serie.head(), end='\n\n')

# STR CONTAINS Method
serie = data.item_name.str.contains('Chicken')
print(serie.head(), end='\n\n')
print(data[serie].head(), end='\n\n')

# STR cascade Methods
serie = data.choice_description.str.replace('[', '')\
                               .str.replace(']', '')
print(serie.head(), end='\n\n')
