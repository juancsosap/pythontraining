import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


x = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
y1 = [10, 70, 80, 90, 95, 45, 15]
y2 = [15, 30, 50, 25, 70, 15, 10]

plt.bar(x, y1, label='Computers', color='#0080FF')
plt.bar(x, y2, label='Printers', color='red')

plt.xlabel('Week Days')
plt.ylabel('Porcentage')
plt.title('Utilization Graph')
plt.legend()

plt.show()
