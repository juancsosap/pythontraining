import pandas as pd
import numpy as np


# Creating Serie from Python List
days = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
days_serie = pd.Series(days)
print(days_serie, end='\n\n')

# Creating Serie from Numpy Array
drivers = np.random.randint(0, 100, 7)
drivers_serie = pd.Series(drivers)
print(drivers_serie, end='\n\n')

# Creating Serie and asigning index
drivers_serie = pd.Series(drivers, index=days)
print(drivers_serie, end='\n\n')

# Creating Serie from a Dictionary
professions = {'Juan': 'Doctor',
               'Luis': 'Escritor',
               'José': 'Cocinero',
               'Paco': 'Taxista',
               'Emma': 'Publicista',
               'Pepe': 'Ingeniero'}
prof_serie = pd.Series(professions)
print(prof_serie, end='\n\n')

# Creating Serie from a Dictionary selecting the rows to include
prof_serie = pd.Series(professions, index=['Juan', 'Paco', 'Pepe'])
print(prof_serie.head(), end='\n\n')

# Creating DataFrame from Python List
guests_rows = [['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
               [10, 12, 14, 20, 15, 8, 18]]
guests_dataframe = pd.DataFrame(guests_rows)
print(guests_dataframe, end='\n\n')

# Creating DataFrame from Python List
guests_columns = list(zip(guests_rows[0], guests_rows[1]))
guests_dataframe = pd.DataFrame(guests_columns)
print(guests_dataframe, end='\n\n')

# Defining Rows Index
guests_dataframe = pd.DataFrame(guests_rows, index=['Days', 'Guests'])
print(guests_dataframe, end='\n\n')

# Defining Column Names
guests_dataframe = pd.DataFrame(guests_columns, columns=['Days', 'Guests'])
print(guests_dataframe, end='\n\n')

# Creating DataFrame from Python Dictionary
guests_dict = {'Days': guests_rows[0], 'Guests': guests_rows[1]}
guests_dataframe = pd.DataFrame(guests_dict)
print(guests_dataframe, end='\n\n')

# Defining Rows Index
guests_dataframe = pd.DataFrame(guests_dict, index=range(1, 8))
print(guests_dataframe, end='\n\n')

# Creating DataFrame from Series
days_serie = pd.Series(guests_rows[0])
drivers_serie = pd.Series(guests_rows[1])
guests_dict = {'Days': days_serie, 'Guests': drivers_serie}
guests_dataframe = pd.DataFrame(guests_dict)
print(guests_dataframe, end='\n\n')

# Selecting Values to include in the DataFrame from Series
days_serie = pd.Series(guests_rows[0])
drivers_serie = pd.Series(guests_rows[1][1:6], index=range(1, 6))
guests_dict = {'Days': days_serie, 'Guests': drivers_serie}
guests_dataframe = pd.DataFrame(guests_dict)
print(guests_dataframe, end='\n\n')

# Creating DataFrame concatenating Series
guests_dataframe = pd.concat([days_serie, drivers_serie], axis=1)
print(guests_dataframe, end='\n\n')

# Creating DataFrame joining DataFrames
df1 = pd.DataFrame(np.random.randn(4, 2), index=['a', 'b', 'c', 'd'], columns=['c1', 'c2'])
df2 = pd.DataFrame(np.random.randn(4, 2), index=['b', 'c', 'd', 'e'], columns=['c3', 'c4'])
dfj = df1.join(df2)
print(dfj, end='\n\n')
dfj = df1.join(df2, how='outer')
print(dfj, end='\n\n')
dfj = df1.join(df2, how='inner')
print(dfj, end='\n\n')
