from threading import Thread
import time


def square(numbers, results):
    for number in numbers:
        time.sleep(0.5)
        result = number ** 2
        print('Square: {result}'.format(result=result))
        results.append(result)
    print('Final Results from New Thread: {results}'.format(results=results))


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    results = []
    t1 = Thread(target=square, args=(numbers, results))

    t1.start()
    t1.join()

    print('Final Results from Main Thread: {results}'.format(results=results))
    print('Done!!')
