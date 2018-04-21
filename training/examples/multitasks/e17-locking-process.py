import multiprocessing as mp
import time


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    balance = mp.Value('i', 200)

    lock = mp.Lock()

    pd = mp.Process(target=deposit, args=(balance, lock))
    pw = mp.Process(target=withdraw, args=(balance, lock))

    pd.start()
    pw.start()

    pd.join()
    pw.join()

    print(balance.value)
