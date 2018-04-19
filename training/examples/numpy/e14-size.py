import numpy as np
# pip install numpy

import sys


size = 200_000_000

lista = range(size)
print(sys.getsizeof(1) * len(lista))

array = np.arange(size)
print(array.size * array.itemsize)
