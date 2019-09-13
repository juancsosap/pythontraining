import numpy as np
# pip install numpy

import time


size = 10_000_000

# Fill Python List
begin = time.time()
lista1 = [i for i in range(size)]
lista2 = [i for i in range(size)]
end = time.time()
print("Fill Python list took:", (end - begin) * 1000)

# Add Python List
begin = time.time()
result = [(x + y) for x, y in zip(lista1, lista2)]
end = time.time()
print("Add Python list took:", (end - begin) * 1000)

print()

# Fill Numpy Array
begin = time.time()
array1 = np.arange(size)
array2 = np.arange(size)
end = time.time()
print("Fill Numpy array took:", (end - begin) * 1000)

# Add Numpy Array
begin = time.time()
result = array1 + array2
end = time.time()
print("Add Numpy array took:", (end - begin) * 1000)
