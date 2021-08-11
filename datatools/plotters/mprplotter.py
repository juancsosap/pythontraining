from datatools.plotters.plotter import *

class MPRPlotter(Plotter):
    def __init__(self, session=None, debug=False):
        try:
            super().__init__(f'outputs/MPR', 'mpr', session)
            for source in self.configs['sources']:
                self.dfs[source]['time'] = self.dfs[source]['time'].apply(TimeUtils.todatetime)
        except Exception as e:
            print('Collected File not available')
            if debug: print(e)
    
    def prepare(self, filterlist=[]):
        super().prepare(filterlist)