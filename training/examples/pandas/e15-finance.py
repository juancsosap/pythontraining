import pandas as pd
import pandas_datareader.data as pddr
# pip install pandas-datareader

import datetime as dt
from datetime import datetime


start = datetime(2016, 1, 1)
stop = datetime(2018, 4, 20)

data = pddr.DataReader('AAPL', 'iex', start, stop)

print(data.head())
