# -*- coding: utf-8 -*-


class Person:

    count = 0

    def __init__(self, surname, name=''):
        self.name = name
        self.surname = surname
        Person.count += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError('The name property must be a String value.')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str):
            self.__surname = value
        else:
            raise ValueError('The surname property must be a String value.')


class Employee(Person):

    def __init__(self, person, job=''):
        super().__init__(name=person.name, surname=person.surname)
        self.job = job

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if isinstance(value, str):
            if len(value) > 2:
                self.__job = value
            else:
                msg = 'job property must have more than 2 printable characters or more.'
                raise ValueError(msg)
        else:
            msg = 'job property must be a string value.'
            raise ValueError(msg)


if __name__ == '__main__':
    juan = Person(surname='Sosa')
    juan.age = 35
    juan.name = 'Carlos'
    juan._Person_name = 5
    print(juan.name)
    print(dir(juan))
    print(Person.count)

    juan.count = 5
    Person.count = 7
