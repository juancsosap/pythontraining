import numpy as np
import matplotlib.pyplot as plt

# Generating random data
x = np.random.randint(-10, 11, 100).reshape((10, 10))

# Plot the data as colored table
plt.imshow(x, cmap=plt.cm.Blues)
plt.title('Table Graph')
plt.colorbar()

# Write text
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        color = 'white' if x[i, j] > x.max() * 2/3 else 'black'
        plt.text(j, i, x[i, j], horizontalalignment='center', verticalalignment='center', color=color)

plt.show()
