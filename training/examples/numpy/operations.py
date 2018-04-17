import numpy as np
# pip install numpy


array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print('ADDITION ARRAY1:', array1[0] + array1[1] + array1[2])
print('ADDITION ARRAY2:', array2[0] + array2[1] + array2[2])

print("Addition:", array1 + array2)
print("Substraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Divition:", array1 / array2)

array3 = np.array([[1, 2], [3, 4], [5, 6]])
print("Dimentions of ARRAY1:", array1.ndim)
print("Dimentions of ARRAY3:", array3.ndim)

print("ITEM Size ARRAY:", array3.dtype, array3.itemsize)

array4 = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
print("ITEM Size ARRAY:", array4.dtype, array4.itemsize)

array5 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print("ITEM Size ARRAY:", array5.dtype, array5.itemsize)
print(array5)
print("SHAPE:", array5.shape)
