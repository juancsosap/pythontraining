import numpy as np
# pip install numpy


arreglo1 = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print('Numpy Array 1:\n{}'.format(arreglo1))

arreglo2 = np.arange(9, 0, -1, dtype=np.int32).reshape((3, 3))
print('Numpy Array 1:\n{}'.format(arreglo2))

print()

# Matrix Operations
print('Numpy Matrix Product (a1 x a2)')
print(arreglo1.dot(arreglo2), end='\n\n')
print('Numpy Matrix Product (a1 x a2)')
print(np.dot(arreglo1, arreglo2), end='\n\n')

print('Numpy Matrix Transpose (a1T)')
print(arreglo1.transpose(), end='\n\n')
print('Numpy Matrix Transpose (a1T)')
print(np.transpose(arreglo1), end='\n\n')
