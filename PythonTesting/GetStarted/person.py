import sys
from datetime import date
from datetime import datetime
import re


def trim(text):
    return re.sub(' +', ' ', text)


class InvalidTimeError(Exception):
    pass


class ValueAlreadyExistError(Exception):
    pass


class ValueDoNotExistError(Exception):
    pass


class Person:
    __count = 0

    def __init__(self, name='', surname='', height=1,
                 birthday=date.today(), isalive=True):
        self.name = name
        self.surname = surname
        self.height = height
        self.birthday = birthday
        self.isalive = isalive

        Person._Person__count += 1

    def __del__(self):
        Person._Person__count -= 1

    @classmethod
    def clone(cls, person):
        return cls(person.name, person.surname, person.height, person.birthday, person.isalive)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str:
            value = trim(value).strip()
            if len(value) > 2:
                self.__name = value
            else:
                msg = 'name property must have almost 2 printable characters or more.'
                raise ValueError(msg)
        else:
            msg = 'name property must be a string value.'
            raise ValueError(msg)

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if type(value) == str:
            value = trim(value).strip()
            if len(value) > 2:
                self.__surname = value
            else:
                msg = 'surname property must have almost 2 printable characters or more.'
                raise ValueError(msg)
        else:
            msg = 'surname property must be a string value.'
            raise ValueError(msg)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) in [int, float]:
            if value > 0 and value < 3:
                self.__height = value
            else:
                msg = 'height property must be between 0 and 3 meters.'
                raise ValueError(msg)
        else:
            msg = 'height property must be a numeric value.'
            raise ValueError(msg)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if type(value) == str:
            datevalue = self.__formatBirthday(value)
        elif type(value) == date:
            datevalue = value
        else:
            msg = 'birthday property must be a string or date value.'
            raise ValueError(msg)
        self.__birthday = datevalue

    @staticmethod
    def __formatBirthday(date):
        try:
            if '-' in date:
                return datetime.strptime(date, '%d-%m-%Y').date()
            elif '/' in date:
                return datetime.strptime(date, '%d/%m/%Y').date()
            else:
                msg = 'birthday property must be a valid date value'
                raise InvalidTimeError(msg)
        except Exception:
            msg = 'birthday property must be a valid date value'
            raise InvalidTimeError(msg)

    @property
    def isalive(self):
        return self.__isalive

    @isalive.setter
    def isalive(self, value):
        if type(value) == bool:
            self.__isalive = value
        else:
            msg = 'isalive property must be a boolean value.'
            raise ValueError(msg)

    @property
    def age(self):
        age = (date.today() - self.birthday).days // 365
        return age

    def __str__(self):
        return f'Name:\t\t{self.getFullName()}\n' + \
               f'Age:\t\t{self.age}\n' + \
               f'Height:\t\t{self.height}\n' + \
               f'Birthday:\t{self.birthday:%A}, {self.birthday:%B %d %Y}\n'

    def __repr__(self):
        return f'Person("{self.name}","{self.surname}",{self.height},' + \
            f'"{self.birthday:%d-%m-%Y}",{self.isalive})\n'

    def getFullName(self):
        return f'{self.name} {self.surname.upper()}'

    @classmethod
    def getQuantity(cls):
        return cls.__count


class Employee(Person):

    def __init__(self, person, job=''):
        super().__init__(person.name, person.surname, person.height,
                         person.birthday, person.isalive)
        self.job = job

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if isinstance(value, str):
            value = trim(value).strip()
            if len(value) > 2:
                self.__job = value
            else:
                msg = 'job property must have more than 2 printable characters or more.'
                raise ValueError(msg)
        else:
            msg = 'job property must be a string value.'
            raise ValueError(msg)

    def __str__(self):
        return str(super()) + f'Job:\t{self.job}\n'

    def getDescription(self):
        return f'{self.job} - {super().getFullName()}\n'


class Manager(Employee):

    def __init__(self, employee, employees=[]):
        super().__init__(employee, employee.job)
        self.employees = employees

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        self.__employees = []
        if type(employees) == list:
            for employee in employees:
                if isinstance(employee, Employee):
                    self.__employees.append(employee)
                else:
                    msg = 'employees property must contain a list of Employee objects.'
                    raise ValueError(msg)
        else:
            msg = 'employees property must contain a list of Employee objects.'
            raise ValueError(msg)

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            if employee not in self.employees:
                self.__employees.append(employee)
            else:
                msg = 'given employee already included in the list.'
                raise ValueAlreadyExistError(msg)
        else:
            msg = 'employees property must contain only Employee objects.'
            raise ValueError(msg)

    def del_employee(self, employee):
        if isinstance(employee, Employee):
            if employee in self.employees:
                self.__employees.remove(employee)
            else:
                msg = 'given employee is not included in the list.'
                raise ValueDoNotExistError(msg)
        else:
            msg = 'employees property contain only a list of Employee objects.'
            raise ValueError(msg)

    def getEmployees(self):
        text = ''
        for employee in self.employees:
            text += f'--> {employee.getFullName()}\n'
        return text

    def __str__(self):
        return str(super()) + '-' * 20 + self.getEmployees()


if __name__ == '__main__':
    if len(sys.argv) > 1:  # First Argument is the script Path
        if sys.argv[1] == '--vervose':
            name = input('Please, Type your name: ')
            surname = input('Please, Type your surname: ')
            birthday = Person.formatBirthday(
                input('Please, Type your birthday: '))
            height = float(input('Please, Type your height: '))
            user = Person(name, surname, height, birthday)
        else:
            user = Person(sys.argv[0], sys.argv[1], float(
                sys.argv[2]), Person.formatBirthday(sys.argv[3]))
        print(f'Thanks for the info {user.getFullName()}')
        print(f'Then, you are {user.age} years old.')
        print(f'and you are {user.height:3.2f} mtrs tall')

    print()

    family = []
    family.append(Person('Jadash', 'Sosa', birthday=date(2013, 12, 18)))
    family.append(Person('Juan', 'Sosa', 1.72, date(1982, 3, 26)))
    family.append(Person('Sarah', 'Sosa', height=1.20,
                         birthday=date(2012, 1, 28)))
    family.append(Person('Ana', 'Prada', birthday=date(1982, 10, 22)))

    family.sort(key=lambda p: p.name)

    for person in family:
        print(person)

    print(Person.getQuantity())

    print(repr(family[0]))
    del family[0]

    print(Person.getQuantity())
    print(len(family))

    ana = Person("Ana", "Prada", 1, "22-10-1982", True)
    otherana = Person.clone(ana)

    print(id(ana))
    print(ana)

    print(id(otherana))
    print(otherana)
