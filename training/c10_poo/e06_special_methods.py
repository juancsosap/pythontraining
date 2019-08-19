'''
__str__   -> str()     str      -> String conversion
__repr__  -> repr()    str      -> String representation
__len__   -> len()     int      -> Length of objects, often used to count elements
'''

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    # is used when str() method is called over the object
    def __str__(self):
        return 'Name: {}\nAge:  {}'.format(self.name, self.age)

    # is used when repr() method is called over the object
    def __repr__(self):
        return '{} [{}]'.format(self.name, self.age)

if __name__ == "__main__":
    p1 = Person('Juan', 20)
    print(str(p1))

    print()
    
    p2 = Person('Carlos', 10)
    print(p2)

    print()
    
    p3 = Person('ana', 30)
    print(repr(p2))