def suma(n1, n2):
    print(n1 + n2)

suma(3, 6)

print()

def suma(n1, n2, n3 = 0):
    print(n1 + n2 + n3)

suma(3, 6)
suma(3, 6, 9)

print()

def suma(nums):
    length = len(nums)
    result = 0
    for i in range(0, length):
        result = result + nums[i]
    return result

value = suma((1, 2, 3))
print(value)

print()

def suma(*nums):
    result = 0
    for num in nums:
        result = result + num
    return result

value = suma(1, 2, 3)
print(value)
datos = [1, 2, 3]
value = suma(*datos)
print(value)

print()

def suma(mul, *nums):
    result = 0
    for num in nums:
        result = result + num
    return result * mul

value = suma(10, 2, 3)
print(value)

print()

def suma(mul = 1, *nums):
    result = 0
    for num in nums:
        result = result + num
    return result * mul

value = suma(10, 2, 3)
print(value)
value = suma()
print(value)

print()

def suma(*nums, mul = 1):
    result = 0
    for num in nums:
        result = result + num
    return result * mul

value = suma(10, 2, 3, 7, 25, 45)
print(value)
value = suma(10, 2, 3, 7, 25, 45, mul=2)
print(value)

# def print(*values, sep=' ', end='\n', file=sys.stdout):

print()

def describir(nombre='', apellido='', edad=0):
    print(nombre)
    print(apellido)
    print(edad)

describir('Juan', 'Sosa', 40)

print()

def describir(*datos):
    for dato in datos:
        print(dato)

describir('Juan', 'Sosa', 40, 120.5)
datos = ['Juan', 'Sosa', 40, 120.5]
describir(*datos)

print()

def describir(nombre='', apellido='', edad=0):
    print('nombre:', nombre)
    print('apellido:', apellido)
    print('edad:', edad)

describir('Juan', 'Sosa', 40)

print()

def describir(*datos):
    for (tipo, valor) in datos:
        print('{}: {}'.format(tipo, valor))

describir(('nombre', 'Juan'), ('apellido', 'Sosa'), ('edad', 40), ('peso', 120.5), ('casado', True))

print()

def describir(datos):
    for (tipo, valor) in datos.items():
        print('{}: {}'.format(tipo, valor))

p = {'nombre':'Juan', 'apellido':'Sosa', 'edad':40, 'peso':120.5, 'casado':True}
describir(p)

print()

def describir(**datos):
    for (tipo, valor) in datos.items():
        print('{}: {}'.format(tipo, valor))

describir(nombre='Juan', apellido='Sosa', edad=40, peso=120.5, casado=True)

print()

def describir(*args, **kwargs):
    for valor in args:
        print('????:', valor)
    for (tipo, valor) in kwargs.items():
        print('{}: {}'.format(tipo, valor))

describir(nombre='Juan', apellido='Sosa', edad=40, peso=120.5, casado=True)
describir('Juan', 'Sosa', 40, 120.5, True)
describir('Juan', 'Sosa', edad=40, peso=120.5, casado=True)

print()

def tocsv(*fields, sep=','):
    for row in zip(*fields):
        print(*row, sep=sep)

names = ['Juan', 'Luis', 'Pepe', 'Maria', 'Ana']
lastnames = ['Perez', 'Rojas', 'Prada', 'Sosa', 'Peña']
ages = [30, 35, 25, 10, 15]
married = [True, False, True, True, False]
tocsv(names, lastnames, ages, married, sep=';')