import pandas as pd


BASEDIR = 'C:\\Users\\juanc\\OneDrive\\Documentos\\GitHub\\pythontraining\\training\\examples\\pandas\\'
FILE_OUTPUT = BASEDIR + 'uforeports.csv'

url = 'http://bit.ly/uforeports'
data = pd.read_csv(url, usecols=['State'])
max = data.shape[0]
print(max)

for c in range(1, max, 500):
    data = pd.read_csv(url, nrows=500, skiprows=c, header=None)
    data.to_csv(FILE_OUTPUT, sep=",", index=False, header=False, mode='a')
    print("#", end='')
