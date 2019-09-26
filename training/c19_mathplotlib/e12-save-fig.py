import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib

import matplotlib.ticker as ticker

import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

class HistPlot:
    def __init__(self, data, ranges, label, title, ylabel='Percentage', color='red'):
        self.data = data
        self.ranges = ranges
        self.label = label
        self.title = title
        self.color = color
        self.ylabel = ylabel

    def prepare(self):
        figure, plot = plt.subplots(1, 1)

        plot.hist(self.data, self.ranges, histtype='bar', rwidth=0.8, color=self.color)
        plot.yaxis.set_major_formatter(ticker.PercentFormatter(len(self.data)))

        plot.set_xlabel(self.label)
        plot.set_ylabel(self.ylabel)
        plot.set_title(self.title)

    def show(self):
        self.prepare()
        plt.show()
    
    def save(self, path):
        self.prepare()
        plt.savefig(path)


ages = np.random.randint(0, 120, 500)
ranges = np.arange(0, 121, 10)

HistPlot(ages, ranges, 'Ages', 'Ages Distribution Graph').show()

clients = np.random.randint(0, 50, 5000)
ranges = np.arange(0, 51, 5)

HistPlot(clients, ranges, 'Clients', 'Clients Distribution Graph', color='green').save('myclientsstat.pdf')
