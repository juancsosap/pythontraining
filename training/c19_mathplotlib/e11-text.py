import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


ages = np.random.randint(0, 120, 500)
ranges = np.arange(0, 120, 20)

plt.hist(ages, label=ranges, histtype='bar', rwidth=0.8, align='left')

plt.xlabel('Ages')
plt.ylabel('Quantity')
plt.title('Ages Distribution Graph')

plt.xticks(ranges)

plt.text(60, 20, 'Ages', horizontalalignment='center', color='red', size=50)

plt.show()
