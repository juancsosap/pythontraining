# -*- coding: utf-8 -*-

stack = [5, 2, 8]
print(stack)

stack.append(1)
print(stack)

stack.append(2)
print(stack)

stack.pop()  # retorna 2, tamaño de la lista=4
print(stack)

stack.pop()  # retorna 1, tamaño de la lista=3
print(stack)

stack.pop()  # retorna 1, tamaño de la lista=2
print(stack)
