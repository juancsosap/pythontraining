import numpy as np


# Creaciónde arreglosunidimensionales:
lista = [1, 2, 3, 4, 5]
print(lista)
print(type(lista))

array = np.array(lista)
print(array)
print(type(array))

print(array.dtype)

# Definirtipode datodel arreglo
array_complejo = np.array(lista, dtype=complex)
print(array_complejo)

matrix = np.array([[0, 1, 2], [3, 4, 5]])  # arreglo 2 x 3
print(matrix)

print(matrix.ndim)  # dimensiones soportadas por el arreglo
print(matrix.shape)  # proporciones de la matrix
