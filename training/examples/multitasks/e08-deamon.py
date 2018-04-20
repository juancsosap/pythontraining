import threading as th
import time


def saludo():
    thread_name = th.currentThread().getName()
    print('Hola {name}'.format(name=thread_name))
    time.sleep(1)
    print('Hola nuevamente {name}'.format(name=thread_name))


t = th.Thread(target=saludo, name='Juan')
t.setDaemon(True)
t.start()
