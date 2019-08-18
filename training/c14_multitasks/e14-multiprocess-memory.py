from multiprocessing import Process
import time


def square(numbers, results):
    for number in numbers:
        time.sleep(0.5)
        result = number ** 2
        print('Square: {result}'.format(result=result))
        results.append(result)
    print('Final Results from New Process: {results}'.format(results=results))


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    results = []
    p1 = Process(target=square, args=(numbers, results))

    p1.start()
    p1.join()

    print('Final Results from Main Process: {results}'.format(results=results))
    print('Done!!')
