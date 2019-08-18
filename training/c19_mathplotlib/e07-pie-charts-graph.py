import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


days = ['DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB']

activity = np.array([10, 7, 8, 12, 11, 5, 6])

plt.pie(activity, labels=days, startangle=90, shadow=False,
        explode=(0, 0, 0, 0.1, 0, 0, 0), autopct='%1.2f%%')

plt.title('Days Activity Distribution Graph')

plt.show()
