import numpy as np
# pip install numpy


lista = [1, 2, 3]
arreglo = np.array([1, 2, 3])
print('Python List\n{}'.format(lista))
print('Numpy Array\n{}'.format(arreglo))

print()

lista = [1, 2.0, 3, True]
arreglo = np.array(lista)
print('Python List\n{}'.format(lista))
print('Numpy Array\n{}'.format(arreglo))

print()

lista = [1, 2.6, '3', True]
arreglo = np.array(lista, dtype=np.int32)
print('Python List\n{}'.format(lista))
print('Numpy Array\n{}'.format(arreglo))

print()

# Array 2D
lista = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
arreglo = np.array(lista)
print('Python List\n{}'.format(lista))
print('Numpy Array\n{}'.format(arreglo))
