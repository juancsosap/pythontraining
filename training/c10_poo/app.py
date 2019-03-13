from persona import Persona
from cliente import Cliente
from empleado import Empleado


personas = [Persona("Juan", 30),
            Persona("Luis", 50),
            Persona("Pepe")]

for persona in personas:
    print(persona)

print()

juan = Cliente("Juan", 40, 1_000_000)
juan.hablar("Hola")
print("Es Persona: {}".format(isinstance(juan, Persona)))
print("Es Cliente: {}".format(isinstance(juan, Cliente)))
juan.comprar("telefono", 1_000_000)
print(juan.get_dinero())

print()

pepe = Empleado("Pepe", 21, "Vendedor")
pepe.atender(juan)

print(Persona.get_cantidad())
