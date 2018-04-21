import multiprocessing as mp
import time


def square(numbers, conn):
    results = []
    for number in numbers:
        time.sleep(0.5)
        result = number ** 2
        print('Square: {result}'.format(result=result))
        results.append(result)
    conn.send(results)
    conn.close()


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    conn1, conn2 = mp.Pipe()
    p1 = mp.Process(target=square, args=(numbers, conn2))

    p1.start()
    print('Final Results from Main Process: {results}'.format(results=conn1.recv()))
    p1.join()

    print('Done!!')
