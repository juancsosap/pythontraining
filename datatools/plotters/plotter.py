from datatools.utils import *

class Plotter:
    dirpath = 'datatools/plotters/configs'
    
    def __init__(self, srcpath, config_item, session=None):
        self.configs = FileUtils.readjson(f'{Plotter.dirpath}/{config_item}.json')
        self.dfs, self.dfsf = dict(), dict()
        session = '' if session is None else f'-{session}'
        for source in self.configs['sources']:
            filename = f'{self.configs["source"]}/{source}{session}.csv'
            self.dfs[source] = DataUtils.loadcsv([filename])
        self.parse = {}          
    
    def prepare(self, filterlist=[]):
        try:
            for source in self.configs['sources']:
                self.dfsf[source] = DataUtils.filterdf(self.dfs[source], DataUtils.importfilters(filterlist))
                DataUtils.printdf(self.dfsf[source], source.upper())
        except:
            print('Invalid Filters')
    
    def loadconfig(self, plotdesc):
        items = plotdesc.split('|') + [None]
        plotname, params = items[0], items[1:]
        
        plotconfig = self.configs['plots'][plotname]
        sources = plotconfig['source']
        if len(sources) > 1:
            df = DataUtils.mergedf([self.dfsf[source] for source in sources], plotconfig['link'])
        else:
            df = self.dfsf[sources[0]]
        
        config = {}
        if 'field' in plotconfig: config['field'] = plotconfig['field'].format(*items[1:])
        if 'title' in plotconfig: config['title'] = plotconfig['title'].format(*items[1:])
        if 'xlabel' in plotconfig: config['xlabel'] = plotconfig['xlabel'].format(*items[1:])
        if 'ylabel' in plotconfig: config['ylabel'] = plotconfig['ylabel'].format(*items[1:])
        
        dffilter = self.loadfilter(df, plotname, params)

        if 'xmap' in plotconfig: config['xmap'] = df[plotconfig['xmap']][dffilter]
        if 'ymap' in plotconfig: config['ymap'] = df[plotconfig['ymap']][dffilter]
        
        if 'xdata' in plotconfig: config['xdata'] = df[plotconfig['xdata']][dffilter]
        if 'ydata' in plotconfig: 
            config['ydata'] = {}
            for field in plotconfig['ydata']:
                config['ydata'][field['label']] = df[field['field'].format(*items[1:])][dffilter]
                    
        return config
    
    def describe(self, source, groups, filtered=True):
        df = self.dfsf[source] if filtered else self.dfs[source]
        return df.describe(include=groups)

    def unique(self, source, field, filtered=True):
        df = self.dfsf[source] if filtered else self.dfs[source]
        return list(df[field].unique())
    
    def plotdata(self, plotname, filter=None):
        config = self.loadconfig(plotname)
        if config['xdata'].shape[0] == 0:
            print('No data Available')
        else:
            if filter != None:
                config['ydata'] = {filter: config['ydata'][filter]}
            PlotUtils.plotdata(config['xdata'], config['ydata'], config['ylabel'], config['title'])
    
    def scatterdata(self, plotname):
        config = self.loadconfig(plotname)
        if config['xdata'].shape[0] == 0:
            print('No data Available')
        else:
            values = list(self.parse[plotname][0]['data'].unique())
            if len(values) > 1:
                PlotUtils.scatterdata(config['xdata'], config['ylabel'], config['title'], self.parse[plotname])
            else:
                print(f'All values are {values[0]}')
    
    def histdata(self, plotname, field=None, percentages=True, stdev=100):
        config = self.loadconfig(plotname)
        field = config['field'] if field is None else field
        serie = config['ydata'][field]
        
        if serie.shape[0] == 0:
            print('No data Available')
        else:
            PlotUtils.histdata(serie, config['ylabel'], config['title'], percentages=percentages, stdev=stdev)
    
    def plotmap(self, mapname, plotname):
        config = self.loadconfig(plotname)
        if config['xmap'].shape[0] == 0:
            print('No data Available')
        else:
            PlotUtils.plotmap(mapname, config['xmap'], config['ymap'], config['title'], self.parse[plotname])
    
    def prepareplot(self, plotdesc, field=None, filters=None):
        items = plotdesc.split('|') + [None]
        plotname, params = items[0], items[1:]
        
        config = self.loadconfig(plotdesc)
        
        field = config['field'] if field is None else field
        serie = config['ydata'][field]
        
        df = pd.DataFrame({field:serie})
        
        self.parse[plotdesc] = PlotUtils.dataclassifier(df, field, plotname, filters)
        
        if serie.shape[0] == 0:
            print('No data Available')
        else:
            return DataUtils.describedata(self.parse[plotdesc][0], 'data', 'color')
        
    def loadfilter(self, df, plotname, params):
        plotconfig = self.configs['plots'][plotname]
        dffilter = pd.Series(np.ones(df.shape[0]), dtype=bool)

        if 'filter' in plotconfig:
            for dfilter in plotconfig['filter']:
                dffilter = dffilter & (df[dfilter] == plotconfig['filter'][dfilter].format(*params))
        return dffilter
    