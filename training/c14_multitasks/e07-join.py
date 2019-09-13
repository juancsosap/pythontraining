import threading as th
import time


def saludo():
    thread_name = th.currentThread().getName()
    print('Hola {name}'.format(name=thread_name))
    time.sleep(1)
    print('Hola nuevamente {name}'.format(name=thread_name))


def despedida(nombre):
    print('Chao {name}'.format(name=nombre))


ts = []

ts.append(th.Thread(target=saludo, name='Juan'))
ts.append(th.Thread(target=saludo, name='Luis'))
ts.append(th.Thread(target=saludo, name='Pepe'))
ts.append(th.Thread(target=saludo, name='Maria'))

for t in ts:
    t.start()

for t in ts:
    t.join(timeout=1)

despedida('Juan')
despedida('Luis')
despedida('Pepe')
despedida('Maria')
