from math import sqrt
from time import time
from threading import Thread


def isprimev1(num):
    prime = True

    if num == 1:
        prime = False
    else:
        for val in range(2, num):
            if num % val == 0:
                prime = False
                break

    if prime:
        # print(f'{num} ', end='')
        Results.success += 1


def isprimev2(num):
    prime = True

    if num == 1:
        prime = False
    else:
        for val in range(2, int(sqrt(num)) + 1):
            if num % val == 0:
                prime = False
                break

    if prime:
        # print(f'{num} ', end='')
        Results.success += 1


def isprimev3(num):
    prime = True

    if num == 1:
        prime = False
    else:
        if num % 2 == 0:
            prime = True if num == 2 else False
        else:
            for val in range(3, int(sqrt(num)) + 1, 2):
                if num % val == 0:
                    prime = False
                    break

    if prime:
        # print(f'{num} ', end='')
        Results.success += 1


def isprimev4(num):
    prime = True

    if num == 1:
        prime = False
    else:
        primes = [2, 3, 5, 7]
        if num in primes:
            prime = True
        else:
            for p in primes:
                if num % p == 0:
                    prime = False
                    break
            if prime:
                for val in range(11, int(sqrt(num)) + 1, 6):
                    if num % val == 0:
                        prime = False
                        break
                if prime:
                    for val in range(13, int(sqrt(num)) + 1, 6):
                        if num % val == 0:
                            prime = False
                            break

    if prime:
        # print(f'{num} ', end='')
        Results.success += 1


def primeAll(max):
    tb = time()
    primes = [2, 3, 5, 7]

    nums = (6 * n + m for n in range(1, max // 6 + 1) for m in (-1, 1))
    for num in nums:
        prime = True
        for pri in primes:
            if num % pri == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    print(f'Total with primeAll:\t{len(primes)}')
    te = time()
    print(f'Required Time with primeAll: {te - tb}\n')


class Results:
    success = 0

    @classmethod
    def reset(cls):
        cls.success = 0


if __name__ == '__main__':
    funcs = []
    # funcs.append(isprimev1)
    # funcs.append(isprimev2)
    funcs.append(isprimev3)
    funcs.append(isprimev4)
    MAXNUMBER = 100000
    for func in funcs:
        Results.reset()
        tb = time()
        i = 0
        pr = []
        t = []
        for n in range(MAXNUMBER + 1):
            func(n + 1)
        # print()
        print(f'Total with {func.__name__}:\t{Results.success}')
        te = time()
        print(f'Required Time with {func.__name__}: {te - tb}\n')

    primeAll(MAXNUMBER)
