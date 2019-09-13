import numpy as np
# pip install numpy


arreglo1 = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print('Numpy Array 1:\n{}'.format(arreglo1))

arreglo2 = np.arange(3, 0, -1, dtype=np.int32).reshape((3, ))
print('Numpy Array 2:\n{}'.format(arreglo2))

arreglo3 = np.arange(10, 40, 10, dtype=np.int32).reshape((3, 1))
print('Numpy Array 3:\n{}'.format(arreglo3))

print()

# Binary Operations
print('Numpy Addition (a1 + a2)')
print(arreglo1 + arreglo2, end='\n\n')
print('Numpy Addition (a1 + a3)')
print(arreglo1 + arreglo3, end='\n\n')
print('Numpy Addition (a1 + 5)')
print(arreglo1 + 5, end='\n\n')
