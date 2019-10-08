import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib

import matplotlib.ticker as ticker

class HistPlot:
    def __init__(self, data, ranges, label, title, ylabel='Percentage', color='red'):
        self.data = data
        self.ranges = ranges
        self.label = label
        self.title = title
        self.color = color
        self.ylabel = ylabel

    def show(self):
        figure, plot = plt.subplots(1, 1)

        plot.hist(self.data, self.ranges, histtype='bar', rwidth=0.8, color=self.color)
        plot.yaxis.set_major_formatter(ticker.PercentFormatter(len(self.data)))

        plot.set_xlabel(self.label)
        plot.set_ylabel(self.ylabel)
        plot.set_title(self.title)

        plt.show()


ages = np.random.randint(0, 120, 500)
ranges = np.arange(0, 121, 10)

HistPlot(ages, ranges, 'Ages', 'Ages Distribution Graph').show()

clients = np.random.randint(0, 50, 5000)
ranges = np.arange(0, 51, 5)

HistPlot(clients, ranges, 'Clients', 'Clients Distribution Graph', color='green').show()
