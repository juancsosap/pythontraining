import numpy as np
# pip install numpy


BASEDIR = 'C:\\Users\\juanc\\OneDrive\\Documentos\\GitHub\\pythontraining\\training\\examples\\numpy'
FILE_INPUT = BASEDIR + '\\data_input.csv'
FILE_OUTPUT = BASEDIR + '\\data_output.csv'

arreglo = np.loadtxt(FILE_INPUT, delimiter=',')
print(arreglo)

print()

arreglo **= 2
print(arreglo)

np.savetxt(FILE_OUTPUT, arreglo, delimiter=',')

print()

x, y, z = np.loadtxt(FILE_OUTPUT, delimiter=',', unpack=True)

print(x)
print(y)
print(z)
