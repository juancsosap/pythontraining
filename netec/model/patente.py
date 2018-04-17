import re


class Patente:

    def __init__(self, patente):
        self.patente = patente

    @property
    def patente(self):
        return self.__patente

    @patente.setter
    def patente(self, valor):
        if(Patente.isPatente(valor)):
            self.__patente = valor
        else:
            raise ValueError('The value must have Patente structure')

    @classmethod
    def isPatente(cls, patente):
        if isinstance(patente, str):
            regexOld = "^[0-9]{4}[A-Z]{2}$"
            regexNew = "^[BCDFGHJKLMNPQRSTVWXYZ]{4}[0-9]{2}$"
            return re.match(regexOld, patente) or re.match(regexNew, patente)
        else:
            raise ValueError('The value must be a String')


module_name = 'Patente'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
