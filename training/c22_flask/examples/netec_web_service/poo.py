
class Person:
    __id = 0

    def __init__(self, name='', age=0):
        self.id = Person.nextid()
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def isadult(self):
        return self.age > 18

    @classmethod
    def nextid(cls):
        cls.__id += 1
        return cls.__id

    @staticmethod
    def printer(person):
        print('{} : {}, {}'.format(person.id, person.name, person.age))

    def print(self):
        print('{} : {}, {}'.format(self.id, self.name, self.age))

    def __str__(self):
        return '{} : {}, {}'.format(self.id, self.name, self.age)


def main():
    juan = Person('Juan', 15)
    pepe = Person('Pepe', 15)

    print(juan.id)
    print(pepe.id)
    print(Person._Person__id)
    print(juan.isadult())
    juan.print()

    juan.name = 'carlos'
    juan.print()

    juan.surname = 'Sosa'
    print(dir(pepe))

    print(juan)

    print(Person._Person__id)

    luis = Person('luis', 15)
    Person.printer(luis)


if __name__ == '__main__':
    main()
