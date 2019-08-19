class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return str([item for item in dir(self) if not item.startswith('__')])

class Employee(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

class Client(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

if __name__ == "__main__":
    print('-'*50)
    
    print('--> Person:')
    p1 = Person('Luis')
    print(repr(p1), p1.name)
    print('P:', isinstance(p1, Person), ', E:', isinstance(p1, Employee), ', C:', isinstance(p1, Client))

    print('-'*50)
    
    print('--> Employee:')
    p2 = Employee('Juan', 'Seller')
    print(repr(p2), p2.name, p2.role)
    print('P:', isinstance(p2, Person), ', E:', isinstance(p2, Employee), ', C:', isinstance(p2, Client))

    print('-'*50)
    
    print('--> Client:')
    p3 = Client('Carlos', 'CocaCola')
    print(repr(p3), p3.name, p3.company)
    print('P:', isinstance(p3, Person), ', E:', isinstance(p3, Employee), ', C:', isinstance(p3, Client))

    print('-'*50)
    