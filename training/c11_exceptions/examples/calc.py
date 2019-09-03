def division(a, b):
    if(a >= -200 and b >= -200):
        return a / b
    else:
        raise ValueError("Solo se aceptan numeros positivos")


def test1():
    a = input("Num1:")
    b = input("Num2:")
    try:
        ai = int(a)
        bi = int(b)
        result = division(ai, bi)
        print(result)
    except ZeroDivisionError as e:
        print("El divisor no puede ser cero")
    except ValueError as e:
        print("Solo se aceptan numeros mayores que -200")
    except Exception as e:
        print(e)
    finally:
        print("Otro mensaje")


def test2():
    a = input("Num1:")
    b = input("Num2:")
    if(a.isnumeric() and b.isnumeric()):
        ai = int(a)
        bi = int(b)
        result = suma(ai, bi)
        print(result)
    else:
        print("Solo se aceptan numeros")
    print("Otro mensaje")


if __name__ == '__main__':
    test1()
    test2()
