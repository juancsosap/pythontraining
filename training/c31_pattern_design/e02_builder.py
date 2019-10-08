class Person:
    def __init__(self, firstname='', lastname='', age=0, nationality=''):
        self.__firstname = firstname
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
    
    def __str__(self):
        return '{} {} [{}] ({})'.format(self.__firstname, self.lastname, self.age, self.nationality)

    @staticmethod
    def builder():
        return Builder()
    
    class Builder:
        def __init__(self):
            self.__instance = Person()
        
        def firstname(self, value):
            self.__instance.__firstname = value
            return self

        def lastname(self, value):
            self.__instance.lastname = value
            return self

        def age(self, value):
            self.__instance.age = value
            return self
        
        def nationality(self, value):
            self.__instance.nationality = value
            return self
        
        def build(self):
            return self.__instance

if __name__ == "__main__":
    p1 = Person(firstname='Juan', lastname='Sosa', age=35, nationality='Chileno')
    print(p1)

    p2 = Person()
    p2._Person__firstname = 'Luis'
    p2.lastname = 'Perez'
    p2.age = 50
    p2.nationality = 'Colombiano'
    print(p2)

    p3 = Person.builder().firstname('Carlos') \
                         .lastname('Peña') \
                         .age(45) \
                         .nationality('Venezolano') \
                         .build()
    print(p3)
    