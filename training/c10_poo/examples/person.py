class Person:
    cantidad = 0

    def __init__(self):
        Person.cantidad += 1

    @classmethod
    def contar(cls):
        return cls.cantidad 
    
    def nombrar(self, name):
        self.nombre = name

    def hablar(self, texto):
        print(self.nombre, texto)

print(Person.contar())

pepe = Person()
pepe.nombrar('Pepe')
pepe.hablar('hola')

print(Person.contar())

jose = Person()
jose.nombrar('Jose')
jose.hablar('hola')

print(Person.contar())

pepe.hablar('chao')
jose.hablar('chao')
