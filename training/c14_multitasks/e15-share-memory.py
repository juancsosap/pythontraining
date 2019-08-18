import multiprocessing as mp
import time


def power(numbers, exp, results):
    for index, number in enumerate(numbers):
        time.sleep(0.5)
        results[index] = number ** exp.value
        print('power ({exp}): {result}'.format(result=results[index], exp=exp.value))
        exp.value += 1
    print('Final Results from New Process: {results}'.format(results=results[:]))


if __name__ == '__main__':
    numbers = [1.1, 1.2, 1.3, 1.4, 1.5]
    results = mp.Array('d', 5)
    exp = mp.Value('i', 4)
    p1 = mp.Process(target=power, args=(numbers, exp, results))

    p1.start()
    p1.join()

    print('Final Results from Main Process: {results}'.format(results=results[:]))
    print('Final EXP Value from Main Process: {exp}'.format(exp=exp.value))
    print('Done!!')
