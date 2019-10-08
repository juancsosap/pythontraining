import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib

import matplotlib.ticker as ticker

ages = np.random.randint(0, 120, 50)
ranges = np.arange(0, 121, 10)

figure, plot = plt.subplots(1, 1)

plot.hist(ages, ranges, histtype='bar', rwidth=0.8)
plot.yaxis.set_major_formatter(ticker.PercentFormatter(50))

plot.set_xlabel('Ages')
plot.set_ylabel('Quantity')
plot.set_title('Ages Distribution Graph')

plt.show()
