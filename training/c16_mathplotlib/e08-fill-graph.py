import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


x = np.linspace(-3, 3, 100)
y = x ** 4 + x ** 3 + x ** 2 + x - 10

plt.plot(x, y, label='Polinom')
plt.fill_between(x, y, 0, where=(y > 0), facecolor='g', alpha=0.3)
plt.fill_between(x, y, 0, where=(y < 0), facecolor='r', alpha=0.3)

plt.grid(True)
plt.xlabel('Value')
plt.ylabel('Result Value')
plt.title('Values Graph')
plt.legend()

plt.show()
