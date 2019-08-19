import math

class Vector:
    __count = 0

    def __init__(self, x=0, y=0, z=0, obj=None):
        self.__x, self.__y, self.__z = 0, 0, 0
        if(type(x) is int):
            self.__x = x
        if(type(y) is int):
            self.__y = y
        if(type(z) is int):
            self.__z = z
        Vector._Vector__count += 1
    
    def __del__(self):
        print("chao, me mori")
        Vector._Vector__count -= 1

    def __add__(self, other):
        return Vector(self.__x + other._Vector__x, self.__y + other._Vector__y, self.__z + other._Vector__z)

    def __sub__(self, other):
        return Vector(self.__x - other._Vector__x, self.__y - other._Vector__y, self.__z - other._Vector__z)

    def __abs__(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def __repr__(self):
        return str(dir(self))

    def __str__(self):
        return '({x}, {y}, {z})'.format(x=str(self.__x), y=str(self.__y), z=str(self.__z))

    def print(self, name=None):
        if(name is not None):
            print(str(name), self)
        else:
            print(self)

    @classmethod
    def count(cls):
        return cls.__count

    @staticmethod
    def merge(v1, v2):
        return v1 + v2

def main():
    v1 = Vector(x=1, z=7)   
    print(v1)
    v1.__x = 'hola'
    print(v1)
    print(repr(v1))
    
    print(Vector.count())
    
    v2 = Vector(7, 9, 9)
    print(v2)
    print(repr(v2))
    
    print(Vector.count())
    
    v3 = v1 + v2
    print(v3)

    Vector.merge(v1, v3).print()

    print(Vector.count())
    
    v4 = v1 - v2
    print(v4)

    print(Vector.count())
    
    print(abs(v4))

    del v4

    print(Vector.count())
    
    print("el programa aun vive")

    v3.print()
    v3.print(v2)


if __name__ == "__main__":
    main()
