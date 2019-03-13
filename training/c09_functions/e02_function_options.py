def sumar(a, b):
    return a + b


def multiplicar(a, b, c=1, d=1):
    return a * b * c * d


def sumar_muchos(*args):
    result = 0
    for val in args:
        result += val
    return result


def printdata(**kwargs):
    for key, val in kwargs.items():
        print('{}: {}'.format(key.capitalize(), val))


def multiplicar_muchos(a, b, *args):
    result = 1
    for val in args:
        result *= val
    return result


if __name__ == '__main__':
    print(sumar(1, 2))
    print(multiplicar(2, 3, 4))
    print(sumar_muchos(1, 2, 3, 4, 5, 6, 7))
    printdata(nombre="Juan", apellido="Sosa", edad=35)
    print(sumar_muchos())
