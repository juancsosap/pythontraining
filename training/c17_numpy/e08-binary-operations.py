import numpy as np
# pip install numpy


arreglo1 = np.array([0b1111, 0b1101, 0b1011, 0b1001, 0b0111, 0b0101, 0b0011, 0b0001])
arreglo2 = np.array([0b1110, 0b1100, 0b1010, 0b1000, 0b0110, 0b0100, 0b0010, 0b0000])

# Binary Operations
print('Numpy & (Binary AND)')
print(arreglo1, arreglo2, '-'*30, sep='\n')
print(arreglo1 & arreglo2, end='\n\n')
print('Numpy | (Binary OR)')
print(arreglo1, arreglo2, '-'*30, sep='\n')
print(arreglo1 | arreglo2, end='\n\n')
print('Numpy ^ (Binary XOR)')
print(arreglo1, arreglo2, '-'*30, sep='\n')
print(arreglo1 ^ arreglo2, end='\n\n')
print('Numpy ~ (Binary NOT)')
print(arreglo1, '-'*30, sep='\n')
print(~arreglo1, end='\n\n')
