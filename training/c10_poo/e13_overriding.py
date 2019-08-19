class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Name    : {}\n'.format(self.name)
    
    def print(self):
        print('Person:')
        print(self)
    
    def show(self):
        print('--> Show <--')
        self.print()

class Employee(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def __str__(self):
        return super().__str__() + 'Role    : {}\n'.format(self.role)

    def print(self):
        print('Employee:')
        print(self)

class Client(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def __str__(self):
        return super().__str__() + 'Company : {}\n'.format(self.company)

    def print(self):
        print('Client:')
        print(self)

if __name__ == "__main__":
    print('-'*50)
    p1 = Person('Luis')
    print(p1)
    p1.print()
    p1.show()
    
    print('-'*50)
    p2 = Employee('Juan', 'Seller')
    print(p2)
    p2.print()
    p2.show()
    
    print('-'*50)
    p3 = Client('Carlos', 'CocaCola')
    print(p3)
    p3.print()
    p3.show()
    
    print('-'*50)
    