from multiprocessing import Process
import time


def square(numbers):
    for number in numbers:
        time.sleep(5)
        print('Square: {result}'.format(result=number**2))


def cube(numbers):
    for number in numbers:
        time.sleep(5)
        print('Cube: {result}'.format(result=number**3))


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    p1 = Process(target=square, args=(numbers,))
    p2 = Process(target=cube, args=(numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done!!')
