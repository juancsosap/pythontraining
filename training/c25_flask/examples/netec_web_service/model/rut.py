import re


class Rut:

    __serie = (2, 3, 4, 5, 6, 7)

    def __init__(self, rut):
        self.rut = rut

    @property
    def rut(self):
        size = len(self.__rut)
        r1 = self.__rut[size - 3:]
        r2 = self.__rut[size - 6:size - 3]
        r3 = self.__rut[:size - 6]
        dv = Rut.getVerificador(self.__rut)
        return '{}.{}.{}-{}'.format(r3, r2, r1, dv)

    @rut.setter
    def rut(self, valor):
        if(Rut.isValid(valor)):
            rutWP = valor.replace(".", "", 2)
            self.__rut = rutWP[:len(rutWP) - 2]
        else:
            raise ValueError('The value must have RUT structure')

    @classmethod
    def getVerificador(cls, valor):
        if isinstance(valor, str):
            result = 0
            for i in range(-1, -len(valor), -1):
                digit = int(valor[i])
                index = (len(valor) - 1 - i) % 6
                result += digit * cls.__serie[index]
            result = 11 - (result % 11)
            if(result == 11):
                return "0"
            elif(result == 10):
                return "k"
            else:
                return str(result)
        else:
            raise ValueError('The value must be a String')

    @classmethod
    def isValid(cls, rut):
        if isinstance(rut, str):
            regex = "[1-9][0-9]?([.]?[0-9]{3}){2}[-][0-9k]"
            return re.match(regex, rut)
        else:
            raise ValueError('The value must be a String')

    @classmethod
    def is_rut(cls, valor):
        if isinstance(valor, str):
            if(cls.isValid(valor)):
                return valor.endswith(cls.getVerificador(Rut(valor).rut))
            return False
        else:
            raise ValueError('The value must be a String')


module_name = 'Rut'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
