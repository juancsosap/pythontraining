import numpy as np
# pip install numpy


arreglo = np.arange(25, dtype=np.int32).reshape((5, 5))
print('Numpy Array:\n{}'.format(arreglo))


print()

print('Numpy a[1]')
print(arreglo[1], end='\n\n')

print('Numpy a[1, 2]')
print(arreglo[1, 2], end='\n\n')

print('Numpy a[1:4]')
print(arreglo[1:4], end='\n\n')

print('Numpy a[1:4, 2]')
print(arreglo[1:4, 2], end='\n\n')

print('Numpy a[1:4, np.newaxis, 2]')
print(arreglo[1:4, np.newaxis, 2], end='\n\n')

print('Numpy a[1:4, 1:4]')
print(arreglo[1:4, 1:4], end='\n\n')

print('Numpy a[::2]')
print(arreglo[::2], end='\n\n')

print('Numpy a[::2, ::-1]')
print(arreglo[::2, ::-1], end='\n\n')

print('Numpy a[::-1, ::-1]')
print(arreglo[::-1, ::-1], end='\n\n')

print('Numpy a[a > 5]')
print(arreglo[arreglo > 5], end='\n\n')

print('Numpy a[a > 5] - 5')
arreglo[arreglo > 5] -= 5
print(arreglo, end='\n\n')
