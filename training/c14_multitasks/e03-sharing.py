import threading as th


def printer():
    thread_name = th.currentThread().getName()
    for i in range(100):
        print('{index:02d} - Hello World from {name}'.format(index=i, name=thread_name))


for i in range(4):
    thread_name = 'PRINTER{index:02d}'.format(index=i)
    t = th.Thread(target=printer, name=thread_name)
    t.start()
