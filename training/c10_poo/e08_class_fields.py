class Person:
    __count = 0

    def __init__(self, name, age):
        Person.__count += 1
        self.id = Person.__count
        self.name = name
        self.age = age
    
    def __str__(self):
        return '({}) {} [{} years]'.format(self.id, self.name, self.age)

if __name__ == "__main__":
    p1 = Person('Juan', 10)
    print('P1:', p1)

    p2 = Person('Carlos', 20)
    print('P2:', p2)

    p3 = Person('Ana', 30)
    print('P3:', p3)
    
    p4 = Person('María', 40)
    print('P4:', p4)
    