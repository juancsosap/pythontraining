import threading as th


def printer():
    thread_name = th.currentThread().getName()
    print('Hello World from {name}'.format(name=thread_name))


t = th.Thread(target=printer, name='PRINTER')
t.start()
