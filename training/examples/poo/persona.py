class Persona:
    def __init__(self, nombre, edad=0):
        self.__set_nombre(nombre)
        self.__set_edad(edad)

    def __set_nombre(self, nombre):
        if(isinstance(nombre, str)):
            if(len(nombre) >= 3):
                self.__name = nombre
            else:
                print("El nombre debe tener al menos 3 caracteres")
        else:
            print("El nombre debe ser un valor String")

    def get_nombre(self):
        return self.__name

    def __set_edad(self, edad):
        if(isinstance(edad, int)):
            if(edad >= 0 and edad <= 150):
                self.__age = edad
            else:
                print("La edad debe estar entre 0 y 150")
        else:
            print("La edad debe ser un valor Entero")

    def get_edad(self):
        return '{} años'.format(self.__age)

    def hablar(self, msg):
        print('{} dice: {}'.format(self.__name, msg))

    def crecer(self):
        self.__age += 1

    def clone(self):
        return Persona(self.__name, self.__age)

    def __str__(self):
        return 'Nombre: {}\nEdad: {}'.format(self.__name, self.__age)


if __name__ == '__main__':
    print('Loading Persona')
else:
    print('Importing Persona')
