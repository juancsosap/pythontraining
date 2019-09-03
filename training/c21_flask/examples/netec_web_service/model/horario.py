import datetime


class Horario:

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, valor):
        if isinstance(valor, datetime.datetime):
            self.__entrada = valor
        else:
            raise ValueError('The value must be a DateTime instance')

    @property
    def salida(self):
        return self.__salida

    @salida.setter
    def salida(self, valor):
        if isinstance(valor, datetime.datetime):
            self.__salida = valor
        else:
            raise ValueError('The value must be a DateTime instance')

    def __init__(self, entrada=None, salida=None):
        self.entrada = entrada
        self.salida = salida

    @classmethod
    def porhoras(cls, entrada, horas):
        salida = entrada + datetime.timedelta(hours=horas)
        return Horario(entrada, salida)

    @classmethod
    def add_time(time, hours):
        return time + datetime.timedelta(hours=hours)


module_name = 'Horario'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
