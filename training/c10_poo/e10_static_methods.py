class Person:
    __count = 0

    def __init__(self, name, age):
        Person.__count += 1
        self.name = name
        self.age = age
    
    def __del__(self):
        Person.__count -= 1

    def __str__(self):
        return '{} [{} years]'.format(self.name, self.age)

    @classmethod
    def count(cls):
        return cls._Person__count
    
    @staticmethod
    def print(person):
        print('Name :', person.name)
        print('Age  :', person.age)
        

if __name__ == "__main__":
    p1 = Person('Juan', 10)
    print('----> P1: Creating')
    Person.print(p1)
    print('Quantity:', Person.count(), '\n')
    
    p2 = Person('Carlos', 20)
    print('----> P2: Creating')
    Person.print(p2)
    print('Quantity:', Person.count(), '\n')
    
    print('----> P2: Deleting')
    del p2
    print('Quantity:', Person.count(), '\n')
    
    p3 = Person('Ana', 30)
    print('----> P3: Creating')
    Person.print(p3)
    print('Quantity:', Person.count(), '\n')
    
    p4 = Person('María', 40)
    print('----> P4: Creating')
    Person.print(p4)
    print('Quantity:', Person.count(), '\n')
    