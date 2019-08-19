class StringList:
    def __init__(self):
        self.__values = []

    def add(self, value):
        if(isinstance(value, str)):
            self.__values.append(value)
        else:
            raise ValueError('Only String value are allowed')

    def remove(self, value):
        if(isinstance(value, str)):
            self.__values.remove(value)
        else:
            raise ValueError('Only String value are allowed')
    
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__values):
            return self.__values[self.__index]
        else:
            raise StopIteration


if __name__ == "__main__":
    sl = StringList()

    sl.add('Juan')
    sl.add('Carlos')
    sl.add('Luis')
    sl.add('Pedro')

    for s in sl:
        print(s)
    
    print()
    
    nsl = iter(sl)
    print(next(nsl))
    print(next(nsl))
    print(next(nsl))
    print(next(nsl))
