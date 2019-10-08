class IntBox:
    def __init__(self, value):
        self.__setdata(value)
    
    @property
    def value(self):
        return self.__data
    
    def __setdata(self, value):
        if(isinstance(value, int)):
            self.__data = value
        else:
            raise ValueError

if __name__ == "__main__":
    b1 = IntBox(5)
    print(b1.value)

    #b1.value = 7               # Not allowed, not available setter

    b1._IntBox__data = 9
    print(b1.value)

    b1._IntBox__setdata(8)
    print(b1.value)

    #b1._IntBox__setdata('hola') # raise a ValueError

    b1._IntBox__data = 'hola'    # no validation is made
    print(b1.value)

    #b2 = IntBox('hola')          # raise a ValueError
