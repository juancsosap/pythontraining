import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


days = ['DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB']

activity_current = np.array([10, 7, 8, 12, 11, 5, 6])
activity_last = np.array([15, 3, 10, 5, 7, 9, 13])

figure, plots = plt.subplots(1, 2, figsize=(9,5))
figure.suptitle('Days Activity')

plots[0].pie(activity_current, labels=days, explode=(0, 0, 0, 0.1, 0, 0, 0), autopct='%d%%')

plots[0].set_title('Current Week')

plots[1].pie(activity_last, labels=days, explode=(0.1, 0, 0, 0, 0, 0, 0), autopct='%d%%')

plots[1].set_title('Last Week')

plt.tight_layout(pad=2)
plt.show()

figure, plots = plt.subplots(3, 3, figsize=(8,5))
    
x = np.linspace(-1, 1, 100)
for n in range(1, 10):
    r, c = (n-1) // 3, (n-1) % 3
    y = x ** n
    plots[r][c].plot(x, y, label=f'x^{n}')

    if r == 2:
        plots[2][c].set_xlabel('Value')
    else:
        plots[r][c].set_xticklabels([])
    
    if c == 0:
        plots[r][0].set_ylabel('Result Value')
    else:
        plots[r][c].set_yticklabels([])
    
    plots[r][c].grid(True)
    plots[r][c].legend()

plt.tight_layout(pad=1)
plt.show()

