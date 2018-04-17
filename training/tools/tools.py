import inspect


def describe(obj):
    print('---- {} Methods and Fields ----'.format(obj.capitalize()))
    for item in dir(eval(obj)):
        if not item.startswith('__'):
            print(item, end='')
            element = eval('{}.{}'.format(obj, item))
            if '__call__' in dir(element):
                print('()')
            else:
                print(':{}'.format(type(element)))


if __name__ == '__main__':
    class Test:
        def __init__(self, value):
            self.value = value

        def increment(self):
            self.value += 1

    val = Test(1)
    describe('val')

    describe('Test')
else:
    print('Loading Tools Module')
