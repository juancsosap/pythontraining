import numpy as np
# pip install numpy


arreglo = np.arange(1, 10, dtype=np.int32).reshape((3, 3))
print('Numpy Array:\n{}'.format(arreglo))

print()

print('Numpy EXP')
print(np.exp(arreglo), end='\n\n')

print('Numpy SQRT')
print(np.sqrt(arreglo), end='\n\n')

print('Numpy SIN')
print(np.sin(arreglo), end='\n\n')

print('Numpy COS')
print(np.cos(arreglo), end='\n\n')

print('Numpy FLOOR')
print(np.floor(arreglo / 2), end='\n\n')

print('Numpy Covariance')
print(np.cov(arreglo), end='\n\n')

print('Numpy Arithmetic Mean')
print(np.mean(arreglo), end='\n\n')

print('Numpy Standard Deviation')
print(np.std(arreglo), end='\n\n')

print('Numpy Variance')
print(np.var(arreglo), end='\n\n')

print('Numpy SUM')
print(arreglo.sum(), end='\n')
print('Numpy SUM Colunms')
print(arreglo.sum(axis=0), end='\n')
print('Numpy SUM Rows')
print(arreglo.sum(axis=1), end='\n\n')

print('Numpy MIN')
print(arreglo.min(), end='\n')
print('Numpy MIN Colunms')
print(arreglo.min(axis=0), end='\n')
print('Numpy MIN Rows')
print(arreglo.min(axis=1), end='\n\n')

print('Numpy MAX')
print(arreglo.max(), end='\n')
print('Numpy MAX Colunms')
print(arreglo.max(axis=0), end='\n')
print('Numpy MAX Rows')
print(arreglo.max(axis=1), end='\n\n')

print('Numpy Cumulative Sum')
print(arreglo.cumsum(), end='\n')
print('Numpy Cumulative Sum Colunms')
print(arreglo.cumsum(axis=0), end='\n')
print('Numpy Cumulative Sum Rows')
print(arreglo.cumsum(axis=1), end='\n\n')
