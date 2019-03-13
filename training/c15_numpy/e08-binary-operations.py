import numpy as np
# pip install numpy


arreglo1 = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print('Numpy Array 1:\n{}'.format(arreglo1))

arreglo2 = np.arange(9, 0, -1, dtype=np.int32).reshape((3, 3))
print('Numpy Array 2:\n{}'.format(arreglo2))

print()

# Binary Operations
print('Numpy & (Binary AND)')
print(arreglo1 & arreglo2, end='\n\n')
print('Numpy | (Binary OR)')
print(arreglo1 | arreglo2, end='\n\n')
print('Numpy ^ (Binary XOR)')
print(arreglo1 ^ arreglo2, end='\n\n')

print('Numpy & (Binary AND) with Number')
print(arreglo1 & 5, end='\n\n')
print('Numpy | (Binary OR) with Number')
print(arreglo1 | 5, end='\n\n')
print('Numpy ^ (Binary XOR) with Number')
print(arreglo1 ^ 5, end='\n\n')
