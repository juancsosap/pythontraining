import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


object_size = np.arange(0, 10)
quantity = object_size ** 2 + np.random.randint(-10, 10, 10)

#plt.plot(object_size, quantity, color='red')
plt.scatter(object_size, quantity, label='Object Size', marker='*', s=100)

plt.grid(True)
plt.xlabel('Sizes')
plt.ylabel('Quantity')
plt.title('Size Distribution Graph')
plt.legend()

plt.show()
