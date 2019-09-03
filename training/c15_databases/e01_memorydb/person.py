class Person:
    def __init__(self, rut, name, age):
        self.rut = rut
        self.name = name
        self.age = age
    
    def __str__(self):
        return '{:>15} : {:15} {:5}'.format(self.rut, self.name, self.age)
