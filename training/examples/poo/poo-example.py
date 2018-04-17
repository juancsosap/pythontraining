class Persona:
    # attpúblico
    edad = 10
    peso = 75
    nombre = 'Pablo'


class Cliente(Persona):
    def get_nombre(self):
        return self.nombre


class Animal:
    orden = 'Carnivora'
    # attprotegido
    _clase = 'Mamalia'
    especie = 'C. lupus'


class Terrestre(Animal):
    def get_clase(self):
        return self._clase


class Zoologico:
    def get_animal_clase(self):
        return Animal()._clase


class Cuenta:
    # attrprivado
    __interes = 0.07
    idUsuario = '00001'
    saldo = 1000000000000


if __name__ == '__main__':
    print(Cliente().get_nombre())
    print(Terrestre().get_clase())
    print(Animal()._clase)
