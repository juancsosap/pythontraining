tupla1 = 1, 3, 4, 6  # herencia de Python 2.X
print(tupla1)

tupla2 = (1, 3, 4, 6)  # herencia de Python 2.X
print(tupla2)

tupla3 = 1, (4, 5, (6, 7))
print(tupla3)

tupla4 = 1, (4, 5, (6, [1, 2]))
tupla4[1][2][1].append(444)
print(tupla4[1][2][1])  # >>> [1, 2, 444]
