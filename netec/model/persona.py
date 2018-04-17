from model.rut import Rut


class Persona:

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self.__nombre = valor
        else:
            raise ValueError('The value must be a String')

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        if isinstance(valor, str):
            self.__apellido = str(valor)
        else:
            raise ValueError('The value must be a String')

    @property
    def rut(self):
        return self.__rut.rut

    @rut.setter
    def rut(self, valor):
        if isinstance(valor, Rut) or valor is None:
            self.__rut = valor
        else:
            raise ValueError('The value must be a Rut instance')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if isinstance(valor, int):
            self.__id = valor
        else:
            raise ValueError('The value must be an Integer')

    def __init__(self, nombre='', apellido='', rut=None, id=0):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.id = id


module_name = 'Persona'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
