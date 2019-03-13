import threading as th
import time


def printer():
    thread_name = th.currentThread().getName()
    for i in range(10):
        print('{index:02d} - Hello World from {name}'.format(index=i, name=thread_name))
        time.sleep(1)


for i in range(100):
    thread_name = 'PRINTER{index:02d}'.format(index=i)
    t = th.Thread(target=printer, name=thread_name)
    t.start()
