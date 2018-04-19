import pandas as pd
import numpy as np


# Reading DataFrame from URL
url = 'http://bit.ly/imdbratings'
data = pd.read_csv(url)
print(data.head(10), end='\n\n')
print(data.tail(10), end='\n\n')

# Describing only the numeric Series of the DataFrame
print(data.describe(), end='\n\n')

# Obtaining the DataFrame shape's
print(data.shape, end='\n\n')

# Obtaining the DataFrame Data Types
print(data.dtypes, end='\n\n')

# Describing obly the object (String), and float64 Data Type of the DataFrame
print(data.describe(include=['object', 'float64']), end='\n\n')

# Describing all the Series of the DataFrame
print(data.describe(include='all'), end='\n\n')

# Accessing only the numeric Data Type Series from the DataFrame
print(data.select_dtypes(include=[np.number]).head(), end='\n\n')

# Obtaining the DataFrame Columns Header names
print(data.columns, end='\n\n')
