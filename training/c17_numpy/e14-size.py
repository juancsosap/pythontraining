import numpy as np
# pip install numpy

import sys


size = 2_000_000

lista = [x for x in range(size)]
space = sys.getsizeof(size) * len(lista)
print('{:,d}'.format(space))

array = np.arange(size)
space = array.size * array.itemsize
print('{:,d}'.format(space))
