import numpy as np

a1 = np.arange(1, 4, dtype=np.int32)
print("ARRAY 1")
print(a1)
a2 = np.arange(4, 7, dtype=np.int32)
print("ARRAY 2")
print(a2)

print("ARRAY SUMA")
print(a1 + a2)
print("ARRAY RESTA")
print(a1 - a2)
print("ARRAY MULTIPLICACION")
print(a1 * a2)
print("ARRAY DIVISION")
print(a1 / a2)

print()

m1 = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print("MATRIX 1")
print(m1)
m2 = np.hstack((np.arange(1, 10, 2, dtype=np.int32),
                np.arange(2, 10, 2, dtype=np.int32))).reshape((3, 3))
print("MATRIX 2")
print(m2)

print("MATRIX SUMA")
print(m1 + m2)
print("MATRIX RESTA")
print(m1 - m2)
print("MATRIX MULTIPLICACION")
print(m1 * m2)
print("MATRIX DIVISION")
print(m1 / m2)
