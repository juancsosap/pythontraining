import math


class Shape:
    def __init__(self):
        self.__type = 'Not Defined'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def getArea(self):
        return 0

    def __str__(self):
        return f'{self.__class__}:{id(self)}'


class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, value):
        self.__radio = value if value > 0 else 1

    def getArea(self):
        return math.pi * (self.radio ** 2)

    def getType(self):
        return "Shape.Circle"

    def __lt__(self, other):
        return self.radio < other.radio

    def __le__(self, other):
        return self.radio <= other.radio

    def __eq__(self, other):
        return self.radio == other.radio

    def __ne__(self, other):
        return self.radio != other.radio

    def __gt__(self, other):
        return self.radio > other.radio

    def __ge__(self, other):
        return self.radio >= other.radio


class Rectangle(Shape):

    @property
    @staticmethod
    def VERTICES():
        return 4

    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        self.__base = value if value > 0 else 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value if value > 0 else 1

    def getArea(self):
        return self.base * self.height

    def getType(self):
        return "Shape.Rectangle"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def getType(self):
        return "Shape.Square"


if __name__ == '__main__':
    figure = Shape()
    print(figure.type)

    c1 = Circle(1)
    print(f'{str(c1)} : {c1.getType()} : {c1.getArea()}')

    c2 = Circle(2)
    print(f'{str(c2)} : {c2.getType()} : {c2.getArea()}')

    r1 = Rectangle(2, 5)
    print(f'{str(r1)} : {r1.getType()} : {r1.getArea()}')

    if isinstance(c1, Circle) and isinstance(c2, Circle):
        if c1 > c2:
            print("C1 is Bigger")
        elif c1 < c2:
            print("C2 is Bigger")
        else:
            print("C1 and C2 are Equals")

    s1 = Square(2)
    print(f'{str(s1)} : {s1.getType()} : {s1.getArea()}')
