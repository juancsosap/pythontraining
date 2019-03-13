from persona import Persona
from cliente import Cliente


class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.set_cargo(cargo)

    def set_cargo(self, cargo):
        if(isinstance(cargo, str)):
            if(len(cargo) >= 3):
                self.__role = cargo
            else:
                print("El cargo debe tener al menos 3 caracteres")
        else:
            print("El cargo debe ser un valor String")

    def get_cargo(self):
        return self.__role

    def atender(self, cliente):
        if(isinstance(cliente, Cliente)):
            print('{} esta atendiendo al cliente {}'.format(
                self.get_nombre(), cliente.get_nombre()))
        else:
            print("Solo podemos atender a clientes")


if __name__ == '__main__':
    print('Loading Empleado')
else:
    print('Importing Empleado')
