class Bit:
    def __init__(self, value = 0):
        self.set(value)

    def get(self):
        return (self.__value + 0)

    def set(self, value):
        if isinstance(value, Bit):
            self.__value = value.bool()
        elif isinstance(value, bool):
            self.__value = value
        else:
            self.__value = (value != 0)

    def bool(self):
        return self.__value

    def __str__(self):
        return str(self.get())

    def __invert__(self):
        return Bit(not self.bool())

    def __or__(self, other):
        return Bit(self.bool() or other.bool())

    def __and__(self, other):
        return Bit(self.bool() and other.bool())

    def __xor__(self, other):
        return ~self & other | self & ~other

class Byte:
    def __init__(self, value = [Bit() for i in range(8)]):
        self.set(value)

    def get(self):
        return [Bit(bit) for bit in self.__value]

    def set(self, value):
        if isinstance(value, Byte):
            self.__value = [Bit(bit) for bit in value.get()]
        elif isinstance(value, list):
            if len(value) == 8:
                valid = True
                for bit in value:
                    if not isinstance(bit, Bit):
                        valid = False
                        break
                if valid:
                    self.__value = value
        elif isinstance(value, str):
            if len(value) == 8:
                valid = True
                for bit in value:
                    if not (bit in ['0', '1']):
                        valid = False
                        break
                if valid:
                    self.__value = [Bit(int(bit)) for bit in value]
                    self.__value.reverse()
        else:
            self.__value = [Bit() for i in range(8)]

    def bool(self):
        return [bit.bool() for bit in self.__value]

    def __getitem__(self, index):
        return Bit(self.__value[index])

    def __setitem__(self, index, value):
        self.__value[index] = Bit(value)

    def __str__(self):
        output = ''
        for item in self.get():
            output = str(item) + output
        return output
