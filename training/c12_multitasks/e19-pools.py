import multiprocessing as mp
import time


def square_add(number):
    result = 0
    for num in range(number):
        result += num ** 2
    return result


if __name__ == '__main__':
    numbers = range(1, 10000)

    start = time.time()
    pool = mp.Pool(processes=20)
    results = pool.map(square_add, numbers)
    pool.close()
    pool.join()
    end = time.time()

    delta = end - start

    print('Final Results from Main Process: {results}'.format(results=results))
    print('The calculation duration was {time} seconds'.format(time=delta))

    start = time.time()
    results = []
    for number in numbers:
        results.append(square_add(number))
    end = time.time()

    delta = end - start

    print('Final Results from Main Process: {results}'.format(results=results))
    print('The calculation duration was {time} seconds'.format(time=delta))

    print('Done!!')
