import numpy as np
# pip install numpy


arreglo1 = np.arange(1, 7, dtype=np.int32).reshape((3, 2))
print('Numpy Array 1:\n{}{}\n'.format(arreglo1, arreglo1.shape))

arreglo2 = np.arange(1, 9, dtype=np.int32).reshape((2, 4))
print('Numpy Array 2:\n{}{}\n'.format(arreglo2, arreglo2.shape))

print()

# Dot Product
print('Numpy Matrix Dot Product (a1 . a2)')
# arreglo4 = arreglo1.dot(arreglo2)
arreglo4 = np.dot(arreglo1, arreglo2) 
print('{}{}\n'.format(arreglo4, arreglo4.shape))

print()

arreglo3 = np.random.randint(1, 10, 9, dtype=np.int32).reshape((3, 3))
print('Numpy Array 3:\n{}{}\n'.format(arreglo3, arreglo3.shape))

# Transpose
print('Numpy Matrix Transpose (a3T)')
# arreglo5 = arreglo3.transpose() 
# arreglo5 = arreglo3.T
arreglo5 = np.transpose(arreglo3)
print('{}{}\n'.format(arreglo5, arreglo5.shape))

# Determinant
print('Numpy Matrix Determinant (det(a3))')
det1 = np.linalg.det(arreglo3)
print('{}\n'.format(det1))

# Invert Matrix
print('Numpy Matrix Invert (inv(a3))')
arreglo7 = np.linalg.inv(arreglo3)
print('{}{}\n'.format(arreglo7, arreglo7.shape))

# Cross Product
print('Numpy Matrix Cross Product (a3 x a3)')
arreglo6 = arreglo3 @ arreglo3
print('{}{}\n'.format(arreglo6, arreglo6.shape))
