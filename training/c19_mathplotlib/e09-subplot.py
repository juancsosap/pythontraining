import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


days = ['DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB']

activity_current = np.array([10, 7, 8, 12, 11, 5, 6])
activity_last = np.array([15, 3, 10, 5, 7, 9, 13])

figure, plots = plt.subplots(1, 2, figsize=(9,6))
figure.suptitle('Days Activity')

plots[0].pie(activity_current, labels=days, startangle=90, shadow=False,
        explode=(0, 0, 0, 0.1, 0, 0, 0), autopct='%1.2f%%')

plots[0].set_title('Current Week')

plots[1].pie(activity_last, labels=days, startangle=90, shadow=False,
        explode=(0.1, 0, 0, 0, 0, 0, 0), autopct='%1.2f%%')

plots[1].set_title('Last Week')

plt.tight_layout(pad=1)
plt.show()

