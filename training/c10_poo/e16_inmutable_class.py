class Person:
    def __init__(self, name, age):
        self.__setname(name)
        self.__setage(age)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    def __setname(self, value):
        if(isinstance(value, str)):
            self.__name = value
        else:
            raise ValueError
    
    def __setage(self, value):
        if(isinstance(value, int)):
            self.__age = value
        else:
            raise ValueError
    
    def __str__(self):
        return '{} {}'.format(self.__name, self.__age)

if __name__ == "__main__":
    p1 = Person('Juan', 40)
    p2 = Person('Luis', 50)

    print(p1)
    print(p2)

    print()

    print(p1.name, p1.age)
    print(p2.name, p2.age)

    # p1.name = 'Maria' # Not allowed, not public setter available
    p3 = Person(123, 123)
