# -*- coding: utf-8 -*-
from time import time
from math import sqrt


def factorial(num):
    if num in (0, 1):
        return 1
    result = num
    for i in range(2, num):
        result *= i
    return result


def primes(num):
    result = [2]
    if num == 1:
        return []
    elif num == 2:
        return [2]
    else:
        for n in range(3, num + 1, 2):
            isprime = True
            for i in result:
                if i > sqrt(n):
                    break
                if n % i == 0:
                    isprime = False
                    break
            if isprime:
                result.append(n)
        return result

    return []


def even(num):
    result = []
    for i in range(0, num, 2):
        result.append(i)
    return result


def evengenerator(num):
    for i in range(0, num, 2):
        yield i


def evennot5(num):
    result = []
    for i in range(0, num, 2):
        if i % 5 != 0:
            result.append(i)
    return result


def creatematrix(rows, columns):
    result = []
    for i in range(rows):
        result.append([])
        for j in range(columns):
            result[i].append(i * columns + j + 1)
    return result


def generatematrix(rows, columns):
    for i in range(rows):
        result = []
        for j in range(columns):
            result.append(i * columns + j + 1)
        yield result


if __name__ == '__main__':
    # Factorial
    t0 = time()
    for i in range(1, 10):
        print(f'{i}:{factorial(i)}')
    t1 = time()
    print(t1 - t0)

    # Primes
    t0 = time()
    pri = primes(1000000)
    t1 = time()
    for p in pri:
        print(p, end=' ')
    print()
    print(len(pri))
    print(t1 - t0)

    # Even
    # Evens with loops
    t0 = time()
    e = even(1000000)
    t1 = time()
    for even in e:
        print(even, end=' ')
    print(t1 - t0)
    # Evens with generators
    t0 = time()
    eg = evengenerator(10000)
    t1 = time()
    for even in eg:
        print(even, end=' ')
    print(t1 - t0)
    # Evens with List Comprenhation
    t0 = time()
    mx = 1000000
    elc = [n for n in range(0, mx, 2)]
    t1 = time()
    elcn5 = [n for n in range(0, mx, 2) if n % 5 != 0]
    print(elc)
    print(elcn5)
    print(len(elcn5))
    print(t1 - t0)

    # Matrix
    # Matrix Creation with Loops
    m = creatematrix(5, 5)
    for r in m:
        for c in r:
            print(c, end='\t')
        print()
    print()
    # Matrix Creation with List Comprenhation
    columns = 5
    rows = 5
    mlc = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    print(mlc)
    # Matrix Cration with Generators
    mg = generatematrix(5, 5)
    print(next(mg))
    print(next(mg))
    print(next(mg))
    print(next(mg))
    print(next(mg))

else:
    print('Bucles library imported')
    print(__name__)
