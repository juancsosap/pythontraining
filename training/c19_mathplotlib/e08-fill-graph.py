import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


x = np.linspace(-3, 3, 100)
y1 = x ** 4 + x ** 3 + x ** 2 + x - 10
y2 = 10 * x - 10

plt.plot(x, y1, label='Poligon', color='red')
plt.plot(x, y2, label='Line', color='blue')
plt.fill_between(x, y1, y2, where=(y1 > y2), facecolor='orange', alpha=0.3)
plt.fill_between(x, y1, y2, where=(y1 < y2), facecolor='green', alpha=0.3)

plt.grid(True)
plt.xlabel('Value')
plt.ylabel('Result Value')
plt.title('Values Graph')
plt.legend()

plt.show()
