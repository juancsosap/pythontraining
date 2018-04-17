from collections import deque


cola = deque([1, 2, 3])
print(cola)

cola.append(7)  # llega 7 en turno No 4
print(cola)

cola.popleft()  # se retorna el elemento de la posición 0 = 1
print(cola)

cola.popleft()  # se retorna el elemento de la posición 0 = 2
