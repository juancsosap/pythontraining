import pandas as pd
import numpy as np


# Creating Serie from Python List
days = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
days_serie = pd.Series(days)
print(days_serie, end='\n\n')
print(type(days))
print(type(days_serie))
print()

# Creating Serie from Numpy Array
drivers = np.random.randint(0, 100, 7)
drivers_serie = pd.Series(drivers)
print(drivers_serie, end='\n\n')
print(type(drivers))
print(type(drivers_serie))
print()

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
               [10, 12, 14, 20, 15, 8, 18],
               [8, 10, 10, 15, 12, 6, 15]]
guests_dataframe = pd.DataFrame(guests_rows)
print(guests_dataframe, end='\n\n')

# Creating DataFrame from Python List
#guests_columns = [['Dom', 10, 8],
#                  ['Lun', 12, 10],
#                  ['Mar', 14, 10],
#                  ['Mie', 20, 15],
#                  ['Jue', 15, 12],
#                  ['Vie', 8, 6],
#                  ['Sab', 18, 15]]
guests_columns = list(zip(*guests_rows))
guests_dataframe = pd.DataFrame(guests_columns)
print(guests_dataframe, end='\n\n')

# Defining Rows Index
guests_dataframe = pd.DataFrame(guests_rows, index=['Days', 'Guests', 'Remained'])
print(guests_dataframe, end='\n\n')

# Defining Column Names
guests_dataframe = pd.DataFrame(guests_columns, columns=['Days', 'Guests', 'Remained'])
print(guests_dataframe, end='\n\n')

# Creating DataFrame from Python Dictionary
guests_dict = {'Days': guests_rows[0], 'Guests': guests_rows[1], 'Remained': guests_rows[2]}
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
print(df1, end='\n\n')
df2 = pd.DataFrame(np.random.randn(4, 2), index=['b', 'c', 'd', 'e'], columns=['c3', 'c4'])
print(df2, end='\n\n')
dfj = df1.join(df2)
print(dfj, end='\n\n')
dfj = df1.join(df2, how='outer')
print(dfj, end='\n\n')
dfj = df1.join(df2, how='inner')
print(dfj, end='\n\n')

# Creating DataFrame merging DataFrames
personas = {'nombre': ['Juan', 'Luis', 'Pepe', 'Maria'],
            'apellido': ['Sosa', 'Perez', 'Lopez', 'Silva'],
            'edad': [10, 20, 30, 40]}
usuarios = {'nombre': ['Juan', 'Luis', 'Pepe'],
            'apellido': ['Sosa', 'Perez', 'Lopez'],
            'password': ['S0s@', 'P3r3$', 'L0P3Z']}

df_personas = pd.DataFrame(personas)
print(df_personas, end='\n\n')
df_usuarios = pd.DataFrame(usuarios)
print(df_usuarios, end='\n\n')
df_full = df_personas.merge(df_usuarios, on=['nombre', 'apellido'], how='outer')
print(df_full, end='\n\n')

# Creating DataFrame merging DataFrames
personas = {'nombre': ['Juan', 'Luis', 'Pepe', 'Maria'],
            'apellido': ['Sosa', 'Perez', 'Lopez', 'Silva'],
            'edad': [10, 20, 30, 40]}
usuarios = {'name': ['Juan', 'Luis', 'Pepe'],
            'surname': ['Sosa', 'Perez', 'Lopez'],
            'password': ['S0s@', 'P3r3$', 'L0P3Z']}

df_personas = pd.DataFrame(personas)
df_usuarios = pd.DataFrame(usuarios)
df_full = df_personas.merge(df_usuarios, how='left', 
                                         left_on=['nombre', 'apellido'], 
                                         right_on=['name', 'surname'])

df_full.drop(['name', 'surname'], axis=1, inplace=True)
print(df_full, end='\n\n')
