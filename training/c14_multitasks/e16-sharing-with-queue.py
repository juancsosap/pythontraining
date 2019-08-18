import multiprocessing as mp
import time


def square(numbers, queue):
    for number in numbers:
        time.sleep(0.5)
        result = number ** 2
        print('Square: {result}'.format(result=result))
        queue.put(result)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    queue = mp.Queue()
    p1 = mp.Process(target=square, args=(numbers, queue))

    p1.start()
    p1.join()

    print('Final Results from Main Process: [', end='')
    while not queue.empty():
        print('{result},'.format(result=queue.get()), end='')
    print(']')
    print('Done!!')
