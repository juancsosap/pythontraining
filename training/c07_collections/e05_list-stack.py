stack = [5, 2, 8]
print(stack)

# Agrega un elemento a la pila
stack.append(1)
print(stack)

# Agrega un elemento a la pila
stack.append(2)
print(stack)

# Extrae un elemento a la pila
stack.pop()  # retorna 2, tamaño de la lista=4
print(stack)

# Extrae un elemento a la pila
stack.pop()  # retorna 1, tamaño de la lista=3
print(stack)

# Extrae un elemento a la pila
stack.pop()  # retorna 1, tamaño de la lista=2
print(stack)

# Leer el actual elemento en el tope de la pila
print(stack[-1])
