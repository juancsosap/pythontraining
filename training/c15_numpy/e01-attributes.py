import numpy as np
# pip install numpy

#   STACK   |   HEAP
#           |
#   list1   |   1234         ABA1     ABA2     ABA3
#   ------  |  ------        -----    -----    -----
#  | 1234 | | | ABA1 | 0    |  1  |  |  2  |  |  3  |
#   ------  |  ------        -----    -----    -----
#           | | ABA2 | 1
#           |  ------
#           | | ABA3 | 2
#           |  ------
#           |
#   array1  |   5678
#   ------  |  -----
#  | 5678 | | |  1  | 0
#   ------  |  -----
#           | |  2  | 1
#           |  -----
#           | |  3  | 2
#           |  -----
#           |

# Array 1D
list1 = [1, 2, 3]
array1 = np.array(list1)
print('1D Python List\n{}'.format(list1))
print('1D Numpy Array\n{}'.format(array1))
print('Dimensions: {} axis'.format(array1.ndim))
print('Shape: {}'.format(array1.shape))
print('Size: {} elements'.format(array1.size))
print('Item Size: {} bytes'.format(array1.itemsize))
print('Item Type: {}'.format(array1.dtype))

print()

# Array 2D
list2 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
array2 = np.array(list2)
print('2D Python List\n{}'.format(list2))
print('2D Numpy Array\n{}'.format(array2))
print('Dimensions: {} axis'.format(array2.ndim))
print('Shape: {}'.format(array2.shape))
print('Size: {} elements'.format(array2.size))
print('Item Size: {} bytes'.format(array2.itemsize))
print('Item Type: {}'.format(array2.dtype))
