import pandas as pd
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
FILE_OUTPUT = os.path.join(BASEDIR, 'uforeports.csv')


url = 'http://bit.ly/uforeports'
data = pd.read_csv(url, usecols=['State'])
max = data.shape[0]
print(max)

data = pd.read_csv(url, nrows=500)
data.to_csv(FILE_OUTPUT, sep=",", index=False, mode='w')
for c in range(501, max, 500):
    data = pd.read_csv(url, nrows=500, skiprows=c, header=None)
    data.to_csv(FILE_OUTPUT, sep=",", index=False, header=False, mode='a')
    print("#", end='')
