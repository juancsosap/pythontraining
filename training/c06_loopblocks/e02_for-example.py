# [0,1,2,3,4,5,6,7,8,9]

val = 0
lista = []
while(val < 100):
    lista.append(val)
    val += 2

print(lista)

lista2 = []
for val in range(0, 100, 2):
    lista2.append(val)

print(lista2)

gen = (val for val in range(0, 100, 2))
print(gen)
