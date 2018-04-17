import numpy as np
import matplotlib


array1 = np.array([1, 2, 3, 4])
print(array1)
print(array1 + 5)
print(array1 - 5)
print(array1 * 5)
print(array1 / 5)
print(array1 % 5)
print(array1 ** 5)

print()

array2 = np.ones(4)  # otrafuncióngeneradorade arreglos
print(array2)
array2 += 1
print(array2)
array2 -= array1
print(array2)

print()

array3 = np.array([1, 2, 3, 4])
print(array3)
array4 = np.array([4, 2, 2, 4])
print(array4)
print(array3 == array4)
print(array3 > array4)

print()

array5 = np.array([1, 1, 0, 0], dtype=bool)
array6 = np.array([1, 0, 1, 0], dtype=bool)
print(array5 | array6)
print(array5 & array6)
print(array5 ^ array6)
print(np.logical_not(array5))

>> > array([False, False, True, True], dtype=bool)
