import numpy as np


arregloA = np.array([True, True, False, False])
print('Numpy Array A:\n{}'.format(arregloA))

arregloB = np.array([True, False, True, False])
print('Numpy Array B:\n{}'.format(arregloB))

print()

# Logical Operations
print('Numpy AND')
print(np.logical_and(arregloA, arregloB), end='\n\n')
print('Numpy OR')
print(np.logical_or(arregloA, arregloB), end='\n\n')
print('Numpy XOR')
print(np.logical_xor(arregloA, arregloB), end='\n\n')
print('Numpy NOT')
print(np.logical_not(arregloA), end='\n\n')

print('Numpy AND with Value')
print(np.logical_and(arregloA, True), end='\n\n')
print('Numpy OR with Value')
print(np.logical_or(arregloA, True), end='\n\n')
print('Numpy XOR with Value')
print(np.logical_xor(arregloA, True), end='\n\n')
