class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return '{} [{} years]'.format(self.__name, self.__age)
    
    # getter
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    # setter
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError('name must be string')

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            raise ValueError('age must be integer')

if __name__ == "__main__":
    p1 = Person('Juan', 10)
    print('P1:', p1)
    p1.name = 'Juan Carlos'
    print(p1.name)
    print('P1:', p1)

    print()

    p2 = Person('Luis', 20)
    print('P2:', p2)
    p2.age = 30
    print('P2:', p2)
