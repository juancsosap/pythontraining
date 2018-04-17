# -*- coding:utf-8 -*-
#!python


def logger(func):
    def inner(*args, **kwargs):
        print(f'{func.__name__}() was called')
        return func(*args, **kwargs)
    return inner


class PropertyError(Exception):
    def __init__(self, property, type, value):
        msg = f'The property {property} must be {type}. The value {value} is not valid.'
        Exception.__init__(self, msg)


class Shape:
    # Atributo de Clase
    __count = 0

    def __init__(self, name='figure'):
        # Atributo de Instancia
        Shape._Shape__count += 1
        self.__name = name

    def __del__(self):
        Shape._Shape__count -= 1

    # getter
    @property
    def name(self):
        return self.__name

    # setter
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise PropertyError('name', 'String', value)

    def __str__(self):
        return f'{id(self)}:{self.__name}'
        # return str(id(self)) + ':' + self.name

    def __repr__(self):
        return f'Shape(\'{self.__name}\')'
        # return 'Shape(\'' + self.name + '\')'

    def __len__(self):
        return len(self.__name)

    @logger
    def __add__(self, other):
        return Shape(self.__name + other.__name)

    @logger
    def __eq__(self, other):
        return self.__name == other.__name

    def getName(self):
        return self.__name

    @logger
    def getCount():
        return Shape._Shape__count


class Square(Shape):
	pass


class Person:

	def __init__(self, **kwargs):
		self.name = kwargs['name'] if 'name' in kwargs else '' 
		self.surname = kwargs['surname'] if 'surname' in kwargs else '' 
		self.age = kwargs['age'] if 'age' in kwargs else 0 
		


if __name__ == '__main__':
    s1 = Shape()
    try:
        s1.name = 2
    except Exception as e:
        print(e)
    s2 = Shape('figure2')
    print(Shape.getCount())

    print(s1)
    print(s1.name)

    print(s2)
    del s2
    print(Shape.getCount())
    s3 = Shape('figure3')
    print(s3)
    print(repr(s1))
    print(len(s1))
    s4 = s1 + s3
    print(s4)
    s5 = Shape('figure1')
    print(s5)
    print(s1 == s5)

    p1 = Person(name='juan', age=35, nationality='venezolano', chiste='jajaja')
    print(p1.name)
    print(p1.surname)
    print(p1.age)
    print(dir(p1))
