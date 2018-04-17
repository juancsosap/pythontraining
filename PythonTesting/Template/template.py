# -*- coding: utf-8 -*-
#!python

import os
import io
import argparse

from string import Template
from datetime import datetime


class MainProgram:

    @classmethod
    def argumentParser(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument('templatePath', type=str,
                            help='Ruta del archivo plantilla utilizada para crear el resultado.')
        parser.add_argument('outputFolder', type=str,
                            help='Directorio donde se almacenaran los resultados.')
        parser.add_argument('-s', '--storelog',
                            help='Guarda en el archivo especificado un log de las acciones ejecutadas.')

        group = parser.add_mutually_exclusive_group()
        group.add_argument('-v', '--verbose', action='store_true',
                           help='Muestra en pantalla el log de las acciones ejecutadas.')
        group.add_argument('-q', '--quiet', action='store_true',
                           help='No muestra en pantalla el log de las acciones ejecutadas.')
        cls.args = parser.parse_args()

    @classmethod
    def loadTemplate(cls):
        tempText = ''
        with io.open(cls.args.templatePath, 'r', encoding='utf-8') as tempFile:
            tempText = tempFile.read()
            if cls.args.verbose:
                print(f'Archivo Plantilla Cargado : {cls.args.templatePath}')
            if cls.args.storelog:
                with io.open(cls.args.storelog, 'a', encoding='utf-8') as outlogFile:
                    outlogFile.write(f'Archivo Plantilla Cargado : {cls.args.templatePath}\n')
        return Template(tempText)

    @classmethod
    def loadData(cls):
        advisor1 = Advisor(Person('Antonio', 'Perez', 'antonio.perez@netec.cl'), 'Chile')
        advisor2 = Advisor(Person('Tiago', 'Mendez', 'tiago.mendez@netec.ar'), 'Argentina')

        description1 = 'Programación Básica en Python'
        event1 = Event(advisor1, 'Introducción a Python', description1, datetime(2018, 1, 29, 9))
        description2 = 'Programación Básica en Java'
        event2 = Event(advisor2, 'Introducción a Java', description2, datetime(2018, 1, 28, 9))

        users = [(User(Person('Juan', 'Sosa', 'juan.sosa@gmail.com'), 'Falabella'), event1),
                 (User(Person('Ana', 'Prada', 'ana.prada@gmail.com'), 'Copec'), event1),
                 (User(Person('Luis', 'Peña', 'luis.pena@gmail.com'), 'ARSAT'), event2),
                 (User(Person('Tomas', 'Lopez', 'tomas.lopez@gmail.com'), 'McDonals'), event2),
                 (User(Person('Carlos', 'Pinto', 'carlos.pinto@gmail.com'), 'BCI'), event1)]

        if cls.args.verbose:
            print('Datos de Prueba Cargada Satisfactoriamente')
        if cls.args.storelog:
            with io.open(cls.args.storelog, 'a', encoding='utf-8') as outlogFile:
                outlogFile.write('Datos de Prueba Cargada Satisfactoriamente\n')

        return users

    @classmethod
    def main(cls):
        cls.argumentParser()
        template = cls.loadTemplate()
        users = cls.loadData()

        count = 0
        for user, event in users:
            data = {'user': user.fullname, 'advisor': event.advisor.fullname, 'email': event.advisor.email,
                    'session': event.name, 'description': event.description,
                    'date': event.datetime.strftime('%d de %m de %Y'),
                    'time': event.datetime.strftime('%Hh%M')}
            result = template.safe_substitute(data)

            outputFileName = f'{os.path.basename(cls.args.templatePath).split(".")[0]}-{user.email}.txt'
            outputPath = os.path.join(cls.args.outputFolder, outputFileName)
            with io.open(outputPath, 'w', encoding='utf-8') as outFile:
                outFile.write(result)
                count += 1
                if cls.args.verbose:
                    print(f'Archivo Resultado Generado : {outputPath}')
                if cls.args.storelog:
                    with io.open(cls.args.storelog, 'a', encoding='utf-8') as outlogFile:
                        outlogFile.write(f'Archivo Resultado Generado : {outputPath}\n')
        if not cls.args.quiet:
            print(f'{count} Archivos Generados Satisfactoriamente.')


class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def fullname(self):
        return f'{self.surname.upper()}, {self.name}'


class User(Person):
    def __init__(self, person, company):
        Person.__init__(self, person.name, person.surname, person.email)
        self.company = company


class Advisor(Person):
    def __init__(self, person, country):
        Person.__init__(self, person.name, person.surname, person.email)
        self.country = country


class Event:
    def __init__(self, advisor, name, description, datetime):
        self.name = name
        self.description = description
        self.datetime = datetime
        self.advisor = advisor
        self.attendees = []


if __name__ == '__main__':
    MainProgram.main()
