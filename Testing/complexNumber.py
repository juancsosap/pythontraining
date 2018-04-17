import math


class ComplexNumber:
    def __init__(self, real, imag=0):
        self.__real = real
        self.__imag = imag

    def __add__(self, other):
        real = self.__real + other.getReal()
        imag = self.__imag + other.getImag()
        return ComplexNumber(real, imag)

    def __neg__(self):
        real = -self.__real
        imag = -self.__imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        real = self.__real * other.getReal() - self.__imag * other.getImag()
        imag = self.__real * other.getImag() + self.__imag * other.getReal()
        return ComplexNumber(real, imag)

    def __pow__(self, power):
        result = self
        for i in range(power - 1):
            result *= self
        return result

    def __abs__(self):
        return math.sqrt(self.__real ** 2 + self.__imag ** 2)

    def __invert__(self):
        real = self.__real / (abs(self) ** 2)
        imag = - self.__imag / (abs(self) ** 2)
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        real = (self * other).getReal() / (abs(other) ** 2)
        imag = (self * other).getImag() / (abs(other) ** 2)
        return ComplexNumber(real, imag)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __ne__(self, other):
        return abs(self) != abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __str__(self):
        oper = '+' if self.__imag >= 0 else ''
        return f'{self.__real}{oper}{self.__imag}i'

    def getReal(self):
        return self.__real

    def getImag(self):
        return self.__imag


if __name__ == '__main__':
    n1 = ComplexNumber(1, 1)
    n2 = ComplexNumber(math.sqrt(2), 0)

    nr = n1 + n2
    print(f'Suma:{nr}')
    nr = n1 - n2
    print(f'Resta:{nr}')
    nr = n1 * n2
    print(f'Multiplicacion:{nr}')
    nr = -n1
    print(f'Negacion:{nr}')
    nr = n1 ** 3
    print(f'Potenciacion:{nr}')
    nr = abs(n1)
    print(f'Absoluto N1:{nr}')
    nr = abs(n2)
    print(f'Absoluto N2:{nr}')
    nr = ~n1
    print(f'Inverso:{nr}')
    nr = n1 / n2
    print(f'Division:{nr}')
    nr = n1 / ComplexNumber(2)
    print(f'Division:{nr}')
    nr = n1 >= n2
    print(f'Comparacion:{nr}')
