class Person:
    def __init__(self, rut, name, age):
        self.rut = rut
        self.name = name
        self.age = age
    
    def __str__(self):
        return '{rut:>15} : {name:15} {age:5}'.format(**self.__dict__)
