import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib

# MAGIC COMMAND FOR JUPYTER NOTEBOOK
# %matplotlib inline


x = np.linspace(-1, 1, 100)

y1 = x ** 2
plt.plot(x, y1, color='red', alpha=0.8, linewidth=5) # string color

y2 = x ** 4
plt.plot(x, y2, color='g') # one letter color

y3 = x ** 6
plt.plot(x, y3, color='#1188FF') # RGB HEX color

# axis -> x, y, both (default)
# linestyle -> '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.grid(True, axis='y', color='black', alpha=0.3, linestyle='dashed', linewidth=2)

plt.show()
