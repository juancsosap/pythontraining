import pandas as pd


url = 'http://bit.ly/uforeports'

BASEDIR = 'C:\\Users\\juanc\\OneDrive\\Documentos\\GitHub\\pythontraining\\training\\examples\\pandas\\'
FILE_OUTPUT = BASEDIR + 'uforeports.csv'


data = pd.read_csv(url, nrows=5, skiprows=0, header=0)
print(data)
data = pd.read_csv(url, nrows=5, skiprows=6, header=None)
print(data)
data = pd.read_csv(url, nrows=5, skiprows=11, header=None)
print(data)

'''
for count in range(0, 18500, 500):
    data = pd.read_csv(url, nrows=500, skiprows=count)
    data.to_csv(FILE_OUTPUT, index=None, mode='a')
    print('#', end='')
'''
