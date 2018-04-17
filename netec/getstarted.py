import math
from math import pi


def verifyage(age):
    if(age < 3):
        print('Bebe')
    elif(age < 12):
        print('Niño')
    elif(age < 18):
        print('Adolecente')
    else:
        print('Adulto')


def printer(**kwargs):
    for k, v in kwargs.items():
        print('{}: {}'.format(k, v))


def add(*args):
    r = 0
    for val in args:
        r += val
    return r


def contact(name='', surname='', age=0):
    print('Name: {}'.format(name))
    print('Surname: {}'.format(surname))
    print('Age: {}'.format(age))


def printline(l):
    for i in range(l):
        print('-', end='')
    print()


def main():
    print(add(5, 5, 5, 5, 5, 5))
    printer(nombre='juan', edad=35, cargo='profesor')
    contact(surname='sosa', age=35)
    print(math.sqrt(2))
    print(pi)
    verifyage(15)
    printline(10)


if __name__ == '__main__':
    main()
