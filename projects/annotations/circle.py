from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) not in [int, float]:
            raise TypeError('The Circle radius must be a real number.')
        if value < 0:
            raise ValueError('The Circle radius cannot be negative.')
        self.__radius = value

    def getArea(self):
        return pi * (self.radius ** 2)


if __name__ == '__main__':
    values = [2, 0, -3, 2 + 5j, True, 'radius']
    for value in values:
        try:
            area = Circle(value).getArea()
        except Exception as e:
            print(e)
        finally:
            print(f'Radius:\t{type(value)}   \t{value}')
            print(f'Area:\t{area}\n')
