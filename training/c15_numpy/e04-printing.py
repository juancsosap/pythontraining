import numpy as np
# pip install numpy


# 1D Numpy Array
arreglo = np.arange(6)
print(arreglo)

print()

# 2D Numpy Array
arreglo = np.arange(12).reshape(4, 3)
print(arreglo)

print()

# 3D Numpy Array
arreglo = np.arange(24).reshape(2, 3, 4)
print(arreglo)

print()

# Large 1D Numpy Array
arreglo = np.arange(10_000)
print(arreglo)

print()

# Large 2D Numpy Array
arreglo = np.arange(10_000).reshape(100, 100)
print(arreglo)

print()

arreglo = np.arange(100)
print(arreglo)
np.set_printoptions(threshold=50)
print(arreglo)
