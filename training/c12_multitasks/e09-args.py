import threading as th


lock = th.Lock()


def printer(name):
    for i in range(100):
        print('{index:02d} - Hello World from {name}'.format(index=i, name=name))


for i in range(4):
    name = 'PRINTER{index:02d}'.format(index=i)
    t = th.Thread(target=printer, args=(name,))
    t.start()
