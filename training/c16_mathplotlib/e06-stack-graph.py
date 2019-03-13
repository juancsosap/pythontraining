import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


days = ['DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB']

sleeping = np.array([7, 6, 7, 6, 5, 8, 7])
eating = np.array([3, 2, 1, 3, 2, 3, 4])
working = np.array([2, 7, 8, 7, 8, 8, 0])
studing = np.array([3, 4, 2, 3, 4, 5, 5])
playing = np.ones((7,)) * 24 - sleeping - eating - working - studing

plt.plot([], [], color='r', label='Sleeping', linewidth=5)
plt.plot([], [], color='g', label='Eating', linewidth=5)
plt.plot([], [], color='b', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Studing', linewidth=5)
plt.plot([], [], color='c', label='Playing', linewidth=5)

plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.15)

plt.stackplot(days, sleeping, eating, working, studing, playing, colors=['r', 'g', 'b', 'k', 'c'])

plt.xlabel('Days')
plt.ylabel('Activities')
plt.title('Days Activity Distribution Graph')
plt.legend()

plt.show()
