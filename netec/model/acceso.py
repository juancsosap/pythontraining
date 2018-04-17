from model.persona import Persona
from model.vehiculo import Vehiculo
from model.horario import Horario


class Acceso:

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, valor):
        if isinstance(valor, Vehiculo):
            self.__vehiculo = valor
        else:
            raise ValueError('The value must be a Vehiculo instance')

    @property
    def persona(self):
        return self.__persona

    @persona.setter
    def persona(self, valor):
        if isinstance(valor, Persona):
            self.__persona = valor
        else:
            raise ValueError('The value must be a Persona instance')

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, valor):
        if isinstance(valor, str):
            self.__departamento = valor
        else:
            raise ValueError('The value must be a String')

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, valor):
        if isinstance(valor, Horario):
            self.__horario = valor
        else:
            raise ValueError('The value must be a Horario instance')

    @property
    def visitante(self):
        return self.__visitante

    @visitante.setter
    def visitante(self, valor):
        if isinstance(valor, bool):
            self.__visitante = valor
        else:
            raise ValueError('The value must be a Bool')

    def __init__(self, vehiculo=None, persona=None, departamento='',
                 horario=None, visitante=False):
        self.vehiculo = vehiculo
        self.persona = persona
        self.dpto = departamento
        self.horario = horario
        self.visitante = visitante


module_name = 'Acceso'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
