cubos = []
for x in range(10):
    cubos.append(x**3)  # elevado al cubo
print(cubos)  # >>> [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# List Comprehention
cuboslc = [x**3 for x in range(10)]
print(cuboslc)

lista = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            lista.append((x, y))
print(lista)

# Multidimensional List Comprehention
listalc = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# >>> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(listalc)
