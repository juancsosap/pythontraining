import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


x = np.linspace(-1, 1, 100)
for n in range(1, 10):
    y = x ** n
    plt.plot(x, y, label='x^{}'.format(n))

plt.xlabel('Value')
plt.ylabel('Result Value')
plt.title('Values Graph')
plt.grid(True)
plt.legend()

plt.show()
