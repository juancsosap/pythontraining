import math

class Base:
    def __init__(self, sbase):
        self.sbase = sbase

    def swap(self, dbase, values, join=False):
        if isinstance(values, int) or isinstance(values, str):
             values = [digit for digit in str(values)]
        sdigits = len(values)
        value = 0
        for i in range(sdigits):
            factor = self.sbase ** (sdigits - i - 1)
            value += int(values[i]) * factor
        result = []
        ddigits = int(math.log(value)/math.log(dbase)) + 1
        for i in range(ddigits):
            factor = dbase ** (ddigits - i - 1)
            number = value // factor
            result.append(str(number))
            value -= number * factor
        return ''.join(result) if join else result
    
    def todec(self, values):
        result = self.swap(10, values)
        return int(''.join(result))
    
    def tohex(self, values):
        digits = ['A', 'B', 'C', 'D', 'E', 'F']
        result = self.swap(16, values)
        result = [digit if int(digit) < 10 else digits[int(digit) - 10] for digit in result]
        return ''.join(result)


if __name__ == "__main__":
    base = Base(8)
    print(base.todec(['5', '2', '3', '4', '5']))
    print(base.swap(16, '52345'))
    print(base.tohex(52345))
    print(base.swap(2, '52345', True))
    