from functools import reduce


class SizeMismatchError(Exception):
    pass


class Matrix:
    def __init__(self, rows=3, columns=3, default=0):
        self.__rows = rows if rows > 0 else 3
        self.__columns = columns if columns > 0 else 3
        self.__matrix = [[default for i in range(
            self.__columns)] for j in range(self.__rows)]

    def load(self, matrix):
        if len(matrix) == self.getSize()[0]:
            if len(matrix[0]) == self.getSize()[1]:
                self.__matrix = matrix
            else:
                raise SizeMismatchError()
        else:
            raise SizeMismatchError()

    def copy(self):
        matrix = Matrix(rows=self.getSize()[0], columns=self.getSize()[1])
        matrix.load(self.__matrix)
        return matrix

    def toList(self):
        return self.__matrix

    def __str__(self):
        text = ''
        for row in self.__matrix:
            for cell in row:
                text += f'{cell}\t'
            text += '\n'
        return text

    def __add__(self, other):
        if self.getSize() == other.getSize():
            n = self.__matrix
            m = other.toList()
            r = [[n[r][c] + m[r][c]
                  for c in range(len(n[0]))] for r in range(len(n))]
            matrix = Matrix(rows=self.getSize()[0], columns=self.getSize()[1])
            matrix.load(r)
            return matrix
        else:
            raise SizeMismatchError()

    def __neg__(self):
        return [[-cell for cell in row] for row in self.__matrix]

    def __sub__(self, other):
        return self + (-other)

    def getSize(self):
        return (len(self.__matrix), len(self.__matrix[0]))


if __name__ == '__main__':
    m1 = Matrix(3, 4, 10)
    print(f'M1:{id(m1)}')
    print(m1)

    m2 = Matrix(3, 4)
    print(f'M2:{id(m2)}')
    print(m2)
    d2 = [[3 * j + i + 1 for i in range(4)] for j in range(3)]
    m2.load(d2)
    print(f'M2:{id(m2)}')
    print(m2)

    m3 = m2.copy()
    print(f'M3:{id(m3)}')
    print(m3)

    m4 = m1 + m2
    print(f'M4:{id(m4)}')
    print(m4)
