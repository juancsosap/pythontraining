from point import Point
from equation import Equation


def test1():
    print(test2())


def test2():
    return 'hola'


if __name__ == '__main__':
    p1 = Point(5, 5)
    p2 = Point(5, 6)
    print(p1)
    print(p2)
    print(p1 == p2)
    s1 = '(5, 5)'
    print(p1 == s1)
    e1 = Equation(5, 5)
    print(e1 == p1)
    print(p1 + p2)
    test1()

    del p1
