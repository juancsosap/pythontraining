# Creating List
lista = [1, 3, 4, 6]
print(lista)
print(type(list))
print(dir(list))

# List Length
size = len(lista)
print(size)

# Could Store different data types
lista = [1, 1.0, 1+1j, True, 'YES', (1,2,3), [1,2,3]]
print(lista)

# Combining Lists
lista1 = [1, 2, 3, 4]
lista2 = ['A', 'B', 'C']
lista = lista1 + lista2
print(lista)

# Multi-dimentional List
lista = [1, [4, 5, [6, 7]]]
print(lista)

print("---------------------------")

# Getting items from List
lista = [1, 2, 3, 4, 1, 1, 3, 3, 3, 3]
print(lista[2])
print(lista[-2])
print(lista[2:4])
print(lista[::2])

# Getting items from multidimentional List
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(lista[2])
print(lista[-2][1])
print(lista[0][::2])

# Could be modified the content
print(lista)
lista[0] = 10
print(lista)
lista[2:5] = [10, 20, 30, 40, 50]
print(lista)

# Verify if a value is in a Collection
print(50 in lista)
