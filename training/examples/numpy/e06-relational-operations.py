import numpy as np


arreglo1 = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print('Numpy Array 1:\n{}'.format(arreglo1))

arreglo2 = np.arange(9, 0, -1, dtype=np.int32).reshape((3, 3))
print('Numpy Array 2:\n{}'.format(arreglo2))

print()

# Relational Operations
print('Numpy <')
print(arreglo1 < arreglo2, end='\n\n')
print('Numpy <=')
print(arreglo1 <= arreglo2, end='\n\n')
print('Numpy >')
print(arreglo1 > arreglo2, end='\n\n')
print('Numpy >=')
print(arreglo1 >= arreglo2, end='\n\n')
print('Numpy ==')
print(arreglo1 == arreglo2, end='\n\n')
print('Numpy !=')
print(arreglo1 != arreglo2, end='\n\n')

print('Numpy < with Number')
print(arreglo1 < 5, end='\n\n')
print('Numpy <= with Number')
print(arreglo1 <= 5, end='\n\n')
print('Numpy > with Number')
print(arreglo1 > 5, end='\n\n')
print('Numpy >= with Number')
print(arreglo1 >= 5, end='\n\n')
print('Numpy == with Number')
print(arreglo1 == 5, end='\n\n')
print('Numpy != with Number')
print(arreglo1 != 5, end='\n\n')
