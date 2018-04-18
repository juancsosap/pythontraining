from persona import Persona
from cliente import Cliente


personas = [Persona("Juan", 30),
            Persona("Luis", 50),
            Persona("Pepe")]

for persona in personas:
    print(persona)

juan = Cliente("Juan", 40, 1_000_000)
juan.hablar("Hola")
print("Es Persona: {}".format(isinstance(juan, Persona)))
print("Es Cliente: {}".format(isinstance(juan, Cliente)))
juan.comprar("telefono", 1_000_000)
print(juan.get_dinero())
