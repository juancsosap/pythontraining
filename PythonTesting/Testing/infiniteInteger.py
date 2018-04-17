class InfiniteInteger:

    def __init__(self, value):
        self.number = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value if value.isdigit() else'0'

    def __add__(self, other):
        size1 = len(self.number)
        size2 = len(other.number)
        size = size1 if size1 > size2 else size2

        num1 = InfiniteInteger.addZeros(self.number, size)
        num2 = InfiniteInteger.addZeros(other.number, size)

        result, drest = '', 0
        for i in range(size):
            dval1 = int(num1[-i - 1])
            dval2 = int(num2[-i - 1])
            dresult = dval1 + dval2 + drest

            drest = dresult // 10
            dresult = dresult % 10

            result = str(dresult) + result

        result = ('1' if drest > 0 else '') + result

        return InfiniteInteger(result)

    @staticmethod
    def addZeros(num, size):
        numSize = len(num)
        zeros = size - numSize
        return ('0' * zeros) + num

    def __str__(self):
        return self.number


if __name__ == '__main__':
    a = InfiniteInteger('123')
    print(a)
    b = InfiniteInteger('1234567890')
    print(b)
    c = a + b
    print(c)
