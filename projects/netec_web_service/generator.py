def geneven(num):
    for i in range(0, num + 1, 2):
        yield i


def genid():
    i = 0
    while True:
        i += 1
        yield i


class generator:
    n = 0

    @classmethod
    def genid2(cls):
        cls.n += 1
        return cls.n


def listeven(num):
    r = []
    for i in range(0, num + 1, 2):
        r.append(i)
    return r


# [[x+3*r for x in range(3)] for r in range(3)]

def genmatrix():
    result = []
    for r in range(3):
        result.append([])
        for x in range(1, 4):
            result[r].append(x + 3 * r)
    return result


if __name__ == '__main__':
    #    for num in listeven(100000000):
    #        if num < 100:
    #            print(num)
    #        else:
    #            break
    print(genmatrix())

    gen = genid()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
    print(generator.genid2())
