import numpy as np
# pip install numpy


arreglo1 = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print('Numpy Array 1:\n{}'.format(arreglo1))

arreglo2 = np.arange(9, 0, -1, dtype=np.int32).reshape((3, 3))
print('Numpy Array 2:\n{}'.format(arreglo2))

print()

# Arithetic Operations
print('Numpy Addition')
print(arreglo1 + arreglo2, end='\n\n')
print('Numpy Substraction')
print(arreglo1 - arreglo2, end='\n\n')
print('Numpy Multiplication')
print(arreglo1 * arreglo2, end='\n\n')
print('Numpy Division')
print(arreglo1 / arreglo2, end='\n\n')
print('Numpy Module')
print(arreglo1 % arreglo2, end='\n\n')
print('Numpy Power')
print(arreglo1 ** arreglo2, end='\n\n')

# Arithetic Operations
print('Numpy Addition with number')
print(arreglo1 + 5, end='\n\n')
print('Numpy Substraction with number')
print(arreglo1 - 5, end='\n\n')
print('Numpy Multiplication with number')
print(arreglo1 * 5, end='\n\n')
print('Numpy Division with number')
print(arreglo1 / 5, end='\n\n')
print('Numpy Module with number')
print(arreglo1 % 5, end='\n\n')
print('Numpy Power with number')
print(arreglo1 ** 5, end='\n\n')
