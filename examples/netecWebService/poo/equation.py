class Equation:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if(isinstance(other, Equation)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == '__main__':
    print(Equation(1, 2) == Equation(3, 4))
else:
    print('Importing {}...'.format(__name__))
