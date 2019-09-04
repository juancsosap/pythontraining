'''
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.setedad(edad)
    
    def setedad(self, valor):
        if valor >= 0 and valor < 150:
            self.__edad = valor
        else:
            self.__edad = 0

    def getedad(self):
        return '{} años'.format(self.__edad)

    def getemail(self, dominio):
        nick = '{}.{}'.format(self.nombre.lower(), self.apellido.lower())
        return '{}@{}'.format(nick, dominio)

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, compañia):
        super().__init__(nombre, apellido, edad)
        self.compañia = compañia
    
    def getemail(self):
        dominio = '{}.cl'.format(self.compañia.lower())
        return super().getemail(dominio)
        
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, cargo):
        super().__init__(nombre, apellido, edad)
        self.cargo = cargo

def getemail(obj, dominio):
    nick = '{}.{}'.format(obj.nombre.lower(), obj.apellido.lower())
    return '{}@{}'.format(nick, dominio)




pepe = Persona("Pepe", "Perez", 35)
juan = Persona("Juan", "Lopez", 75)
print(juan.getedad())

juan.edad = -100

print(juan.getedad())

print()

print(pepe.nombre, pepe.apellido, pepe.getedad())
print(pepe.getemail('itau.cl'))
print(juan.getemail('itau.cl'))

print(getemail(pepe, 'itau.cl'))
print(getemail(juan, 'itau.cl'))

print()

luis = Cliente("Luis", "Gomez", 50, "Fallabela")
print(luis.getemail())

ana = Empleado("Ana", "Gutierrez", 70, "Contadora")
print(ana.getemail('anayasociados.cl'))
'''

class TextAnalizer:
    '''
    Class with tools to make simple analitic over text
    '''
    def __init__(self, text):
        '''
        TextAnalizer(text)
        Create the object model with the text provided
        where text must be a string value
        '''
        if(isinstance(text, str)):
            self.__text = text
        else:
            raise ValueError
    
    def char_quantity(self, space=True):
        '''
        char_quantity([space])
        Return the amound of characters present in the text
        space - flag the indicate if the space characters must be considered
              - optional value  with the default value True
        '''
        if space:
            return len(self.__text)
        else:
            clean_text = self.__text.replace(' ', '').replace('\t', '').replace('\n', '')
            return len(clean_text)
    
    def char_list(self, space=True):
        '''
        char_list([space])
        Return a set with the characters present in the text
        space - flag the indicate if the space characters must be considered
              - optional value  with the default value True
        '''
        if space:
            return set(self.__text)
        else:
            clean_text = self.__text.replace(' ', '').replace('\t', '').replace('\n', '')
            return set(clean_text)
    
    def word_quantity(self):
        '''
        word_quantity()
        Return a the quantity of words present in the text
        '''
        clean_text = self.__text.replace('.', ' ').replace(',', ' ').replace('\n', ' ') \
                                .replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
        return len(clean_text.split(' '))

    def word_list(self):
        '''
        word_quantity()
        Return the set of words present in the text
        '''
        clean_text = self.__text.replace('.', ' ').replace(',', ' ').replace('\n', ' ') \
                                .replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
        return set(clean_text.split(' '))


ta = TextAnalizer("hola    mundo")
print(ta.word_quantity())

class Person:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

pepe = Person('Juan', 'Sosa', 30)
print(pepe.nombre, pepe.apellido, pepe.edad)
print(pepe)

juan = pepe
print(juan)

juan.nombre = 'Luis'

print(pepe.nombre, pepe.apellido, pepe.edad)

def cambiarnombre(persona):
    persona.nombre = 'Maria'

cambiarnombre(juan)

print(pepe.nombre, pepe.apellido, pepe.edad)

class Number:
    def __init__(self, value):
        self.value = value

import random

def getnumber(num):
    num.value = random.randint(0, 100)

mynum = Number(6)
getnumber(mynum)
print(mynum.value)
