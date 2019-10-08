import numpy as np
# pip install numpy

# Data generation
arreglo1 = np.random.randint(1, 10, (5, 1))
arreglo2 = np.arange(15, 0, -1).reshape((5, 3))
arreglo3 = np.hstack([arreglo1, arreglo2])
print('Numpy Array:\n{}'.format(arreglo3))

print()

# Sort by one column
sorter = arreglo3[:,0].argsort()
print('Numpy Sorter:\n{}'.format(sorter))

arreglo4 = arreglo3[sorter]
print('Numpy Sorted:\n{}'.format(arreglo4))

print()

# Sort by many columns
multi_sorter = np.lexsort((arreglo3[:, 2], arreglo3[:, 0]))
print('Numpy Sorter:\n{}'.format(multi_sorter))

arreglo5 = arreglo3[multi_sorter]
print('Numpy Sorted:\n{}'.format(arreglo5))

print()

# Permute data
unorder = np.random.permutation(np.arange(len(arreglo3)))
print('Numpy Unorder:\n{}'.format(unorder))

arreglo6 = arreglo3[unorder]
print('Numpy Unorded:\n{}'.format(arreglo6))
