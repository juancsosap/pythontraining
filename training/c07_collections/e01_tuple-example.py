# Creating Tuple
tupla = 1, 3, 4, 6  # herencia de Python 2.X
tupla = (1, 3, 4, 6)
print(tupla)
print(type(tuple))
print(dir(tuple))

# Tuple Length
size = len(tupla)
print(size)

# Could Store different data types
tupla = (1, 1.0, 1+1j, True, 'YES', (1,2,3))
print(tupla)

# Multi-dimentional Tuple
tupla = (1, (4, 5, (6, 7)))
print(tupla)

# Could not be modified the content of the tuple
# tuple[0] = 10 # Not supported

print("---------------------------")

# Getting items from Tuple
tupla = (1, 2, 3, 4, 1, 1, 3, 3, 3, 3)
print(tupla[2])
print(tupla[-2])
print(tupla[2:4])
print(tupla[::2])

print("---------------------------")

# Methods
# Number of times the value is present in the tuple
print(tupla.count(1))
# Index of the first element with the specified value
print(tupla.index(3))
print(tupla.index(3, 3)) # Index from the specified index
print(tupla.index(3, 3, 7)) # Index between the specified indexes
# print(tupla.index(3, 3, 6)) # If not value is found a ValueError is throw

print("---------------------------")

# Use Tuple to initialize multiple variables
tupla = (1, 2, 3)
(a, b, c) = tupla
# a, b, c = 1, 2, 3
print(tupla)
print(a, b, c)

# Verify if a value is in a Collection
print(1 in tupla)
