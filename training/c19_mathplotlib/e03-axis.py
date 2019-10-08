import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


x = np.linspace(-1, 1, 100)
for n in range(1, 10):
    y = x ** n
    plt.plot(x, y, label=f'x^{n}')

plt.xlabel('Value')
plt.ylabel('Result Value')
plt.title('Values Graph')
plt.grid(True)
plt.legend()

plt.xticks([-1, 0, 1])
plt.yticks([-1, -0.5, 0, 0.5, 1], ['One', 'Two', 'Three', 'Four', 'Five'], rotation=30)

plt.show()
