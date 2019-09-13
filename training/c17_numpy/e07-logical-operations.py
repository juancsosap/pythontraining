import numpy as np
# pip install numpy


arregloA = np.array([True, True, False, False])
arregloB = np.array([True, False, True, False])

# Logical Operations
print('Numpy AND')
print(arregloA, arregloB, '-'*30, sep='\n')
#print(np.logical_and(arregloA, arregloB), end='\n\n')
print(arregloA & arregloB, end='\n\n')
print('Numpy OR')
print(arregloA, arregloB, '-'*30, sep='\n')
#print(np.logical_or(arregloA, arregloB), end='\n\n')
print(arregloA | arregloB, end='\n\n')
print('Numpy XOR')
print(arregloA, arregloB, '-'*30, sep='\n')
#print(np.logical_xor(arregloA, arregloB), end='\n\n')
print(arregloA ^ arregloB, end='\n\n')
print('Numpy NOT')
print(arregloA, arregloB, '-'*30, sep='\n')
#print(np.logical_not(arregloA), end='\n\n')
print(~arregloA, end='\n\n')
