class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        with open('point.txt', 'a') as file:
            file.write(str(self) + '\n')

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y
        except Exception as e:
            return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __del__(self):
        print('Deleting Point {}'.format(self))

    def __enter__(self):
        pass

    def __exit__(self):
        pass


if __name__ == '__main__':
    print(Point(1, 2) + Point(3, 4))
else:
    print('Importing {}...'.format(__name__))
