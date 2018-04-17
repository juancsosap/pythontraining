# -*- coding: utf-8 -*-
from datetime import date, datetime

if __name__ == '__main__':
    nombre = input('Escribe tu Nombre: ')
    apellido = input('Escribe tu Apellido: ')
    edad = int(input('Escribe tu Edad: '))
    altura = float(input('Escribe tu Altura: '))
    nacimiento = input('Escribe tu fecha de Nacimiento: ')
    fecha = datetime.strptime(nacimiento, '%d-%m-%Y').date()
    edadreal = (date.today() - fecha).days // 365
    print(f'{nombre} {apellido.upper()}')
    print(f'Tienes {edad} años')
    print(f'Mides {altura:.2f} mtrs')
    print('Naciste el {0:%d} de {0:%m} de {0:%Y} ' +
          'y tienes {1} años'.format(fecha, edadreal))
    if edad >= 18:
        print('Eres Mayor de edad')
    elif edad < 8:
        print('Eres un niño')
    else:
        print('Eres Menor de edad')
    mensaje = 'Puedes pasar' if edad >= 18 else 'No puedes entrar'
    print(mensaje)
