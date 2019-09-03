# () -> ANY   ->    Supplier
def text():
    return 'hello'

mensaje = text()
print(mensaje)

# () -> ()    ->    Action
def show():
    print('hello')

show()

# ANY -> ()   ->    Consumer
def sayhello(name):
    print('hello', name)

sayhello('Juan')

# ANY -> ANY  ->    Function
def greet(name):
    return 'hello ' + name

saludo = greet('Carlos')
print(saludo)

# ANY -> Bool ->    Predicate
def validate(passwd):
    return 'MyPassword' == passwd

clave = "123456"
valido = validate(clave)
print(valido)

print()

def sumar(n1, n2): return n1 + n2
def restar(n1, n2): return n1 - n2
def multiplicar(n1, n2): return n1 * n2
def dividir(n1, n2): return n1 / n2

operaciones = [sumar, restar, multiplicar, dividir]

for oper in operaciones:
    print(oper(5, 5))

oper = sumar
oper(1,2)

def printoper(n1, n2, oper):
    result = oper(n1, n2)
    print(result)

printoper(5, 7, sumar)

add = lambda n1, n2 : n1 + n2
sub = lambda n1, n2 : n1 - n2
mul = lambda n1, n2 : n1 * n2
div = lambda n1, n2 : n1 / n2

print(add(1,5))

printoper(5, 2, lambda n1, n2 : n1 ** n2)

textos = ['hola', 'saludos', 'yo', 'espermatozoide', 'luis']

for n in map(lambda t : len(t), textos):
    print(n)

def longitud(texto):
    return len(texto)
for n in map(longitud, textos):
    print(n)