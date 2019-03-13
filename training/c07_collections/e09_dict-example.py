empleados = {1: "Pedro", 2: "Pablo", 3: "Juan"}  # crea diccionario empleados
print(empleados)

empleados.update({1: "Pedro Pablo", 4: "Ricardo"})  # agrega un elemento y actualiza otro
print(empleados)  # >>>{1: 'Pedro Pablo', 2: 'Pablo', 3: 'Juan', 4: 'Ricardo'}

print(sorted(empleados.keys()))  # >>>[1, 2, 3, 4]  # lista de llaves ordenada

print(3 in empleados)  # >>>true
print("Ricardo" in empleados)  # >>> false

print(empleados[1])  # >>>Pedro Pablo
print(empleados.pop(2))  # >>> Pablo
print(empleados)  # >>>{1: 'Pedro Pablo', 3: 'Juan', 4: 'Ricardo'}

print()

animales = dict([('perros', 4139), ('gatos', 4127), ('loros', 4098)])  # creación mediante secuencia
print(animales)  # >>> {'perros': 4139, 'gatos': 4127, 'loros': 4098}
print(animales['perros'])
animales['perros'] = 1234
print(animales['perros'])

print(animales.items(), end='\n\n')

for key in animales:
    print(str(key) + ":" + str(animales[key]))

print()

for (key, val) in animales.items():
    print(str(key) + ":" + str(val))

print()

for i, v in enumerate(sorted(animales.keys())):
    print("id: {0} nombre: {1} quantity: {2}".format(i, v, animales[v]))

print()

dicty = {x: x ** 2 for x in range(5)}
print(dicty)
