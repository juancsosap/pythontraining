from model.patente import Patente


class Vehiculo:

    @property
    def patente(self):
        return self.__patente.patente

    @patente.setter
    def patente(self, valor):
        if isinstance(valor, Patente):
            self.__patente = valor
        else:
            raise ValueError('The value must be a Patente instance')

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        if isinstance(valor, str):
            self.__marca = str(valor)
        else:
            raise ValueError('The value must be a String')

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        if isinstance(valor, str):
            self.__modelo = valor
        else:
            raise ValueError('The value must be a String')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        if isinstance(valor, str):
            self.__color = valor
        else:
            raise ValueError('The value must be a String')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if isinstance(valor, int):
            self.__id = valor
        else:
            raise ValueError('The value must be an Integer')

    def __init__(self, patente=None, modelo='', color='', marca='', id=0):
        self.patente = patente
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.id = id


module_name = 'Vehiculo'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
