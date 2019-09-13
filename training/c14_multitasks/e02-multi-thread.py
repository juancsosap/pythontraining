import threading as th


def printer():
    thread_name = th.currentThread().getName()
    print('Hello World from {name}'.format(name=thread_name))


for i in range(10):
    thread_name = 'PRINTER{index}'.format(index=i)
    t = th.Thread(target=printer, name=thread_name)
    t.start()

printer()
