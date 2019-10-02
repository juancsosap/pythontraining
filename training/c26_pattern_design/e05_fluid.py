class StrList:
    def __init__(self, values):
        self.__list = [value for value in values if(isinstance(value, str))]
    
    def upper(self):
        self.__list = [value.upper() for value in self.__list]
        return self

    def lower(self):
        self.__list = [value.lower() for value in self.__list]
        return self

    def filter(self, selector):
        self.__list = [value for value in self.__list if selector(value)]
        return self

    def limit(self, quantity):
        self.__list = self.__list[:quantity] if len(self.__list) > quantity else self.__list
        return self

    def foreach(self, action):
        for item in self.__list: 
            action(item)

    def print(self):
        print(self.__list)

def sw(t):
    return not t.startswith('A')

if __name__ == "__main__":
    l = []
    sl = StrList(['Juan', 'Carlos', 'Luis', 'Andres', 'Pepe', 'Antonio', 'Jose', 'Ana', 'Maria', 'Sofia'])
    sl.upper().filter(sw) \
              .filter(lambda t : not t.endswith('A')) \
              .filter(lambda t : len(t) > 4) \
              .foreach(lambda t : l.append(t.lower()))
    
    print(l)