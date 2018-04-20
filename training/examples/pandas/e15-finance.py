import pandas as pd
import pandas_datareader.data as pddr
# pip install pandas-datareader

import datetime as dt
from datetime import datetime


start = datetime(2016, 1, 1)
stop = datetime(2018, 4, 20)

data = pddr.DataReader('GOOG', 'iex', start, stop)

print(type(data), '\n')

print(data.head(), '\n')

print(data.tail(), '\n')
