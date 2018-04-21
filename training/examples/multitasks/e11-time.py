import threading as th
import time


lock = th.Lock()


def isprimo(num, primes):
    time.sleep(0.1)
    if(num < 2):
        return False
    else:
        for n in range(2, num):
            if(num % n == 0):
                return False
    lock.acquire()
    primes.append(num)
    lock.release()
    return True


max = 10

primes = []
start = time.time()
for n in range(1, max):
    isprimo(n, primes)
end = time.time()
delta = (end - start) * 1000
print('Duration: {time}'.format(time=delta))
print(primes)

primes = []
start = time.time()
for n in range(1, max):
    t = th.Thread(target=isprimo, args=(n, primes))
    t.start()
for n in range(1, max):
    t.join()
end = time.time()
delta = (end - start) * 1000
print('Duration: {time}'.format(time=delta))
print(primes)
