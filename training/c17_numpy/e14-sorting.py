import numpy as np
# pip install numpy

arreglo1 = np.random.randint(1, 10, (5, 1))
arreglo2 = np.arange(15, 0, -1).reshape((5, 3))
arreglo3 = np.hstack([arreglo1, arreglo2])
print('Numpy Array:\n{}'.format(arreglo3))

sorter = arreglo3[:,0].argsort()
print('Numpy Sorter:\n{}'.format(sorter))

arreglo4 = arreglo3[sorter]
print('Numpy Sorted:\n{}'.format(arreglo4))

print()

multi_sorter = np.lexsort((arreglo3[:, 2], arreglo3[:, 0]))
print('Numpy Sorter:\n{}'.format(multi_sorter))

arreglo5 = arreglo3[multi_sorter]
print('Numpy Sorted:\n{}'.format(arreglo5))

