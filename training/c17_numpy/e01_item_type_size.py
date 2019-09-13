import numpy as np

# Valid values
l = [1, 2, 3]
a = np.array(l)
print(a, a.dtype)

# Different type values
l = [1, 2, 3]
a = np.array(l, dtype=np.int32)
print(l, l[0].bit_length())
print(a, a.dtype)

# wrong type for the vale
n = 500
l = [n, n, n]
a = np.array(l, dtype=np.uint8)
print(l, l[0].bit_length())
print(a, a.dtype)

# rigth type for the value
n = 500
l = [n, n, n]
a = np.array(l, dtype=np.uint16)
print(l, l[0].bit_length())
print(a, a.dtype)

'''
'int0', 'int8', 'int16', 'int32', 'int64'
'uint0', 'uint8', 'uint16', 'uint32', 'uint64'
'float16', 'float32', 'float64', 'float128'
'complex64', 'complex128', 'complex256'
'bool8'

int16 -> 2^16 = 2^10 * 2^6 = 64 * 10^3 -> -32*10^3 <-> +32*10^3
'''