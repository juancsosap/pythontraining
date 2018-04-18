from persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, edad, dinero):
        super().__init__(nombre, edad)
        self.__set_dinero(dinero)

    def __set_dinero(self, dinero):
        if(isinstance(dinero, float) or isinstance(dinero, int)):
            if(dinero >= 0):
                self.__money = dinero
            else:
                print("El dinero debe tener al menos 0 pesos")
        else:
            print("El dinero debe ser un valor numerico")

    def gastar(self, cantidad):
        if(isinstance(cantidad, float) or isinstance(cantidad, int)):
            if(cantidad > 0):
                if(cantidad <= self.__money):
                    self.__money -= cantidad
                else:
                    print("No tienes dinero suficiente")
            else:
                print("La cantidad a gastar debe ser mayor que 0 pesos")
        else:
            print("La cantidad debe ser un valor numerico")

    def ganar(self, cantidad):
        if(isinstance(cantidad, float) or isinstance(cantidad, int)):
            if(cantidad > 0):
                self.__money += cantidad
            else:
                print("La cantidad a ganar debe ser mayor que 0 pesos")
        else:
            print("La cantidad debe ser un valor numerico")

    def get_dinero(self):
        return '{} pesos'.format(self.__money)

    def comprar(self, item, costo):
        self.gastar(costo)
        print('{} esta comprando un {}'.format(self.get_nombre(), item))


if __name__ == '__main__':
    print('Loading Cliente')
else:
    print('Importing Cliente')
