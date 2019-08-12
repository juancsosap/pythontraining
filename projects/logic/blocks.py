from data import Bit, Byte

class Adder:
    def __init__(self, data1 = Byte(), data2 = Byte(), bias = Bit()):
        self.__build = False
        self.setinput(1, data1)
        self.setinput(2, data2)
        self.setbias(bias)
        self.__build = True
        self.operate()

    def setinput(self, id, value):
        if isinstance(value, Byte):
            if id == 1:
                self.__data1 = Byte(value)
                if self.__build: self.operate()
            if id == 2:
                self.__data2 = Byte(value)
                if self.__build: self.operate()

    def setbias(self, value):
        if isinstance(value, Bit):
            self.__bias = Bit(value)
            if self.__build: self.operate()

    one = lambda d1, d2, r : d1 ^ d2 ^ r
    bis = lambda d1, d2, r : ((d1 ^ d2) & r) | (d1 & d2)

    def operate(self):
        r = self.__bias
        output = []
        for i in range(8):
            d1 = self.__data1[i]
            d2 = self.__data2[i]
            output.insert(0, Adder.one(d1, d2, r))
            r = Adder.bis(d1, d2, r)
        self.__output = Byte(output)
        self.__rest = r

    def getoutput(self):
        return Byte(self.__output)

    def getrest(self):
        return Bit(self.__rest)
