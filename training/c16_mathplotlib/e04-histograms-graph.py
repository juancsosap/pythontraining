import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


ages = np.random.randint(0, 120, 100)
ranges = np.arange(0, 121, 10)

plt.hist(ages, ranges, histtype='bar', rwidth=0.8)

plt.xlabel('Ages')
plt.ylabel('Quantity')
plt.title('Ages Distribution Graph')

plt.show()
