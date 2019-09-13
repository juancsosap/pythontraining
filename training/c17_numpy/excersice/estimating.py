import numpy as np

np.set_printoptions(threshold=10)

size = 10_000

ids = np.arange(size).reshape((size, 1))
ages = np.random.randint(0, 150, size).reshape((size, 1))
risk = (np.random.random(size) * 100).reshape((size, 1))
loads = np.random.randint(0, 20, size).reshape((size, 1))

clients = np.hstack((ids, ages, risk, loads))
print(clients)

print()

minval = np.array([18, 75, 0])
maxval = np.array([40, 100, 5])

results = (clients[:, 1:] >= minval) & (clients[:, 1:] <= maxval)

print(results)

print()

status = results[:, 0] & results[:, 1] & results[:, 2]

print(status)

print()

good = clients[status]

print(good)
print(len(good))
