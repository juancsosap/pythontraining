import numpy as np
# pip install numpy
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
FILE_INPUT = os.path.join(BASEDIR, 'data_input.csv')
FILE_OUTPUT = os.path.join(BASEDIR, 'data_input.csv')

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
