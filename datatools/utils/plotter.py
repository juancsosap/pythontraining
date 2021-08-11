import random
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.ticker import PercentFormatter
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from datatools.utils import FileUtils, DataUtils

class PlotUtils:
    dirpath = 'datatools/utils/configs'
    
    # plot a group of pandas series with its mean
    @staticmethod
    def plotdata(xaxis, series, ylabel, title):
        plt.figure(figsize=(12, 5))
        for label, serie in series.items():
            mean = [serie.mean() for x in range(serie.shape[0])]
            plt.plot(xaxis, serie, label=label)
            plt.plot(xaxis, mean)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.xlim(xaxis.min(), xaxis.max())
        plt.title(title)
        plt.grid()
        plt.legend(loc='upper right')
        plt.show()
    
    @staticmethod
    def randomcolor():
        digits = [random.choice('0123456789ABCDEF') for j in range(6)]
        return "#"+''.join(digits)

    # scatter categorical data with colors according to it
    @staticmethod
    def histdata(serie, ylabel, title, percentages=True, stdev=100):
        plt.figure(figsize=(12, 3))
        
        if serie.dtype != 'O':
            mean = serie.mean()
            stdv = serie.std()
            dffilter = (serie > mean - stdv*stdev) & (serie < mean + stdv*stdev)
            serie = serie[dffilter]
        
        if percentages:
            plt.hist(serie, rwidth=0.8, weights=np.ones(len(serie)) / len(serie))
            plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        else:
            plt.hist(serie) 
            
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

    # scatter categorical data with colors according to it
    @staticmethod
    def scatterdata(xaxis, ylabel, title, parsedata):
        info, values = parsedata
        serie = pd.Categorical(info['data'], categories=values, ordered=True)

        plt.figure(figsize=(12, 5))
        
        plt.scatter(xaxis, serie, c=info['color'], alpha=1)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.xlim(xaxis.min(), xaxis.max())
        plt.grid()
        plt.show()

    # plot coordinates in a map
    @staticmethod
    def plotmap(location, longitudes, latitudes, title, parsedata):
        info, values = parsedata
        
        fig, ax = plt.subplots(figsize = (12,10))
        maps = FileUtils.readjson(f'datatools/utils/configs/maps.json')[location]
        
        bg = plt.imread(maps['path'])
        box = (DataUtils.tocoo(*maps['longitude']['min']), DataUtils.tocoo(*maps['longitude']['max']), 
               DataUtils.tocoo(*maps['latitude']['min']), DataUtils.tocoo(*maps['latitude']['max']))

        ax.scatter(longitudes, latitudes, zorder=1, s=20, c=info['color'])
        
        ax.set_xlim(DataUtils.tocoo(*maps['longitude']['min']), DataUtils.tocoo(*maps['longitude']['max']))
        ax.set_ylim(DataUtils.tocoo(*maps['latitude']['min']), DataUtils.tocoo(*maps['latitude']['max']))
        ax.tick_params(labelrotation=45)
        ax.set_title(title)
        ax.set_xlabel('Longitud')
        ax.set_ylabel('Latitud')

        if 'nodes' in maps:
            nodes = FileUtils.readjson(f'datatools/utils/configs/nodes.json')[maps['nodes']]
            for node in nodes:
                latitude, longitude = DataUtils.tocoo(*node['latitude']), DataUtils.tocoo(*node['longitude'])
                ax.scatter(longitude, latitude, zorder=1, s=200, c='black', marker='o')
                ax.scatter(longitude, latitude, zorder=1, s=50, c='red', marker='v')
        
        ax.imshow(bg, zorder=0, extent=box, aspect='equal')

        plt.show()

    @staticmethod
    def dataclassifier(df, field, config_item=None, filter=None, alpha=0.2):
        serie = df[field]
        values = list(serie.unique())
        if config_item != None:
            config = FileUtils.readjson(f'{PlotUtils.dirpath}/plots.json')
            if filter == None: filter = [dfilter['name'] for dfilter in config[config_item]]
            data, colors = [], []
            for row  in serie:
                for dfilter in config[config_item]:
                    within = True
                    if 'min' in dfilter:
                        within = within and (row > dfilter['min'])
                    if 'max' in dfilter:
                        within = within and (row <= dfilter['max'])
                    if 'value' in dfilter:
                        within = within and (dfilter['value'] in row)
                    if within:
                        r, g, b = to_rgb(dfilter['color'])
                        alpha = dfilter['alpha'] if dfilter['name'] in filter else 0
                        colors.append((r, g, b, alpha))
                        data.append(dfilter['name'])
                        break
            values = [dfilter['name'] for dfilter in config[config_item]]
        else:
            dcolors = []
            for _ in range(len(values)):
                r, g, b = to_rgb(randomcolor())
                dcolors.append((r, g, b, 0.2))
            colors = serie.map(dict(zip(values, dcolors)))
            data = serie
        return pd.DataFrame({'data':data, 'color':colors}), values
