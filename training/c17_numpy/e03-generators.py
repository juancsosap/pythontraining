import numpy as np
# pip install numpy


arreglo = np.zeros(6)
print('Numpy Array\n{}'.format(arreglo))

print()

# Default dtype float64
arreglo = np.zeros((2, 3), dtype=np.int32)
print('Numpy Array\n{}'.format(arreglo))

print()

# Default dtype float64
arreglo = np.ones((2, 3), dtype=np.str)
print('Numpy Array\n{}'.format(arreglo))

print()

# Default dtype float64
arreglo = np.empty((2, 3), dtype=np.str)
print('Numpy Array\n{}'.format(arreglo))

print()

lista = range(10)
print('Python List\n{}'.format(lista))
arreglo = np.arange(10, dtype=np.float64)
print('Numpy Array\n{}'.format(arreglo))
print()

# default dtype int64
lista = range(1, 10)
print('Python List\n{}'.format(lista))
arreglo = np.arange(1, 10)
print('Numpy Array\n{}'.format(arreglo))
print(arreglo.dtype)

print()

lista = range(2, 10, 2)
print('Python List\n{}'.format(lista))
arreglo = np.arange(2, 10, 2)
print('Numpy Array\n{}'.format(arreglo))

print()

arreglo = np.full((2, 5), 5)
print('Numpy Array\n{}'.format(arreglo))

print()

arreglo = np.linspace(0, 5, 21)
print('Numpy Array\n{}'.format(arreglo))

print()

# Default dtype float64
arreglo = np.linspace(1, 5, 10, dtype=np.int8)
print('Numpy Array\n{}'.format(arreglo))

print()

arreglo = np.random.random((2, 3))*100
print('Numpy Array\n{}'.format(arreglo))

print()

arreglo = np.random.randint(1, 10, (2, 10))
print('Numpy Array\n{}'.format(arreglo))

print()

# Identity Matrix
arreglo = np.identity(4)
print('Numpy Array\n{}'.format(arreglo))


print()

# Identity Matrix
arreglo = np.eye(4,5)
print('Numpy Array\n{}'.format(arreglo))
