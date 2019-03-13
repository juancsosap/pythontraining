from collections import deque

dias = deque(['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'])
print(dir(deque))

dias.append('domingo')  # agrega un elemento al final
print(dias)

dias.appendleft('otro día')  # agrega un elemento al principio
print(dias)

dias.insert(3, 'segundo miércoles')  # añade un elemento en el indice indicado
print(dias)

dias.remove('otro día')  # remueve el elemento indicado
print(dias)

dias.pop()  # remueve y retorna el último elemento
print(dias)

dias.popleft()  # remueve y retorna el primer elemento
print(dias)

print('index: {}'.format(dias.index('jueves')))

dias.rotate()  # ordena la lista colocando el último elemento en la primera posición
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

dias.extend(['lunes', 'sábado']) # agrega los elementos de una lista al final de otra lista
print(dias)
dias.extendleft(newdias) # agrega los elementos de una lista al principio de otra lista
print(dias)

# Get the first Element
print(newdias[0])
# Get the last Element
print(newdias[-1])
# print(newdias[1:3]) # Slice is not supported

print(newdias)

print(dias.maxlen) # No limit (None)

# Verify if a value is in a Collection
print('lunes' in dias)
