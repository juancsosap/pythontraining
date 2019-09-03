import numpy as np
# pip install numpy

basedir = __file__[:__file__.rfind('/')+1]

infile = basedir + 'data/data_input.csv'
outfile = basedir + 'data/data_output.csv'

arreglo = np.loadtxt(infile, delimiter=',')
print(arreglo)

print()

arreglo **= 2
print(arreglo)

np.savetxt(outfile, arreglo, delimiter=',')

print()

x, y, z = np.loadtxt(outfile, delimiter=',', unpack=True)

print(x)
print(y)
print(z)
