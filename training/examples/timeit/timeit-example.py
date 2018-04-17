import timeit


def testlc(max):
    lista = [x**3 for x in range(max)]
    print(len(lista))


def testfl(max):
    lista = []
    for x in range(max):
        lista.append(x**3)
    print(len(lista))


if __name__ == '__main__':
    max = 30_000_000
    time = timeit.timeit("testlc({})".format(max), setup="from __main__ import testlc", number=1)
    print("Duración: {} en seg".format(time))
    time = timeit.timeit("testfl({})".format(max), setup="from __main__ import testfl", number=1)
    print("Duración: {} en seg".format(time))
