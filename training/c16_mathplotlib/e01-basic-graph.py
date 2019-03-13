import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib

# MAGIC COMMAND FOR JUPYTER NOTEBOOK
# %matplotlib inline


x = np.linspace(-1, 1, 100)
y = x ** 2

plt.plot(x, y)

plt.show()
