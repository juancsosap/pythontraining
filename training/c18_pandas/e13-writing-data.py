import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

outfile = 'data/uforeports-clean.csv'

url = 'data/uforeports.csv'   #'http://bit.ly/uforeports'
data = pd.read_csv(url, usecols=['State'])
max = data.shape[0]
print(max)

data = pd.read_csv(url, nrows=500)
data.to_csv(outfile, sep=",", index=False, mode='w')
for c in range(501, max, 500):
    data = pd.read_csv(url, nrows=500, skiprows=c, header=None)
    data.to_csv(outfile, sep=",", index=False, header=False, mode='a')
    print("#", end='')

print()

# read_csv   -> to_csv
# read_json  -> to_json
# read_sql   -> to_sql
# read_excel -> to_excel
# read_table -> to_table
