class Operable:
    def __init__(self, value):
        self.__value = value
    
    def __str__(self):
        return str(self.__value)

class Additable(Operable):
    def __add__(self, other):
        return self.__class__(self._Operable__value + other._Operable__value)

class Subtractable(Operable):
    def __sub__(self, other):
        return self.__class__(self._Operable__value - other._Operable__value)

class Number(Additable, Subtractable):
    pass

if __name__ == "__main__":
    n1 = Number(7)
    print(' ', n1)

    n2 = Number(2)
    print(' ', n2, '+')

    print('-'*5)

    n3 = n1 + n2
    print(' ', n3)

    print()

    n1 = Number(7)
    print(' ', n1)

    n2 = Number(2)
    print(' ', n2, '-')

    print('-'*5)

    n3 = n1 - n2
    print(' ', n3)
