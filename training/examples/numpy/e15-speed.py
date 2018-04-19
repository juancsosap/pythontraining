import numpy as np
# pip install numpy

import time


size = 10_000_000

lista1 = range(size)
lista2 = range(size)

array1 = np.arange(size)
array2 = np.arange(size)


# Python List
begin = time.time()
result = [(x + y) for x, y in zip(lista1, lista2)]
end = time.time()
print("Python list took:", (end - begin) * 1000)

# Numpy Array
begin = time.time()
result = array1 + array2
end = time.time()
print("Numpy array took:", (end - begin) * 1000)
