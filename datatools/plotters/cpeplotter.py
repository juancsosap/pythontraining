from datatools.plotters.plotter import *

class CPEPlotter(Plotter):
    def __init__(self, session=None):
        try:
            super().__init__(f'outputs/CPE', 'cpe', session)
            for source in self.configs['sources']:
                self.dfs[source]['time'] = self.dfs[source]['time'].apply(TimeUtils.todatetime)
        except:
            print('Collected File not available')
    
    def prepare(self, filterlist=[]):
        super().prepare(filterlist)
    
    def cpemigrated(self):
        return '|'.join(pd.read_csv('datatools/repository/migrated.csv')['hostname'].unique())