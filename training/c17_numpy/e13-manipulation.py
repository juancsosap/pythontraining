import numpy as np
# pip install numpy


arreglo1 = np.arange(20, dtype=np.int32).reshape((5, 4))
print('Numpy Array:\n{}'.format(arreglo1))

arreglo2 = np.arange(20, 0, -1, dtype=np.int32).reshape((5, 4))
print('Numpy Array:\n{}'.format(arreglo2))

print()

print('Numpy Flat')
print(arreglo1.ravel(), end='\n\n')

print('Numpy Re-Shape')
print(arreglo1.reshape((2, 10)), end='\n\n')

print('Numpy Re-Shape')
print(arreglo1.reshape((2, -1)), end='\n\n')

print('Numpy Vertical Stack')
print(np.vstack((arreglo1, arreglo2)), end='\n\n')

print('Numpy Horizontal Stack')
print(np.hstack((arreglo1, arreglo2)), end='\n\n')

print('Numpy Horizontal Split')
print(np.hsplit(arreglo1, 2), end='\n\n')
print(np.hsplit(arreglo1, 2)[0], end='\n\n')
print(np.hsplit(arreglo1, 2)[1], end='\n\n')
