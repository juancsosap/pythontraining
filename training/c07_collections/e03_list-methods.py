# -*- coding: utf-8 -*-

dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

dias.append('domingo')  # agrega un elemento
print(dias)

dias.append('otro día')  # añade un día al final
print(dias)

dias.insert(2, 'segundo miércoles')  # añade un día en el indice indicado
print(dias)

dias.remove('otro día')  # remueve del final un día
print(dias)

dias.pop()  # remueve el último elemento, puede recibir la posición a remover -retorna el elemento
print(dias)

print('index: {}'.format(dias.index('lunes')))

dias.sort()  # ordena la lista según los tipos de elementos -e.i. A-Z
print(dias)

dias.append('lunes')  # agrega un elemento
print(dias)

# retorna la cantidad de elementos de un tipo en la lista
print('count: {}'.format(dias.count('lunes')))

dias.reverse()  # reorganiza la lista en orden inverso al original
print(dias)

newdias = dias.copy()  # retorna una copia de la lista

dias.clear()  # borra los elementos de la lista, igual que del(dias[:])
print(dias)

dias.extend(newdias[1:3])
dias.extend(newdias) # agrega los elementos de una lista al final de otra lista
print(dias)
print(newdias)

texto = "Juan"
letras = []
letras.extend(texto)
print(letras)
