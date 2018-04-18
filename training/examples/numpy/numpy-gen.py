import numpy as np


array1 = np.zeros(shape=(3, 4))
print(array1)

array2 = np.ones(shape=(3, 4))
print(array2)

array3 = np.arange(2, 10, 2)
print(array3)

array4 = np.linspace(0, 10, 20)
print(array4)

array5 = array4.reshape(5, 4)
print(array5)

array6 = array5.ravel()
print(array6)

print(array6.min())
print(array6.max())
print(array6.sum())
print(array5.sum(axis=0))
print(array5.sum(axis=1))
print(np.sqrt(array6))
print(np.std(array6))
