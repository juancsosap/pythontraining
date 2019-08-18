import threading as th
import time


def saludo():
    thread_name = th.currentThread().getName()
    print('Hola {name}'.format(name=thread_name))
    time.sleep(1)
    print('Hola nuevamente {name}'.format(name=thread_name))


def despedida():
    thread_name = th.currentThread().getName()
    print('Chao {name}'.format(name=thread_name))
    time.sleep(1)
    print('Chao nuevamente {name}'.format(name=thread_name))


ts = []

ts.append(th.Thread(target=saludo, name='Juan'))
ts.append(th.Thread(target=saludo, name='Luis'))
ts.append(th.Thread(target=saludo, name='Pepe'))
ts.append(th.Thread(target=saludo, name='Maria'))

ts.append(th.Thread(target=despedida, name='Juan'))
ts.append(th.Thread(target=despedida, name='Luis'))
ts.append(th.Thread(target=despedida, name='Pepe'))
ts.append(th.Thread(target=despedida, name='Maria'))

for t in ts:
    t.start()
