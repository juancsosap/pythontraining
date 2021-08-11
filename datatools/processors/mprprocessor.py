from datatools.processors.processor import *

class MPRProcessor(Processor):
    def __init__(self, session=None, categories='all', dates=None):
        dates = [] if dates is None else dates
        super().__init__('mpr', categories, dates)
        self.session = session
        self.path = 'outputs/MPR'
    
    def process(self, filters={}):
        self.dfs = dict()
        for category in self.categories:
            print('Loading ...              ', end='')
            self.dfs[category] = DataUtils.loadcsv(FileUtils.listfiles(f'{self.path}/{category}', [category] + self.dates))
            DataUtils.printdf(self.dfs[category], category.upper())
        
        if 'basic' in self.categories:
            print('Fixing ...               ', end='')
            self.dfs['basic'] = self.dfs['basic'][self.dfs['basic']['time'].notna()]
            self.dfs['basic']['time'] = self.dfs['basic']['date'] + ' ' + self.dfs['basic']['time']
            self.dfs['basic']['time'] = self.dfs['basic']['time'].apply(TimeUtils.todatetime)
            DataUtils.printdf(self.dfs['basic'], 'BASIC')
        
        for category in self.categories:
            print('Processing ...           ', end='')
            self.dfs[category] = DataUtils.dropna(self.dfs[category])
            self.dfs[category] = self.setdtypes(self.dfs[category], category)
            self.dfs[category] = self.dfs[category].sort_values(['time']).reset_index(drop=True)
            self.dfs[category]['date'] = self.dfs[category]['time'].apply(lambda t: t.strftime('%Y/%m/%d'))
            self.dfs[category]['week'] = self.dfs[category]['time'].apply(lambda t: t.isocalendar()[1])
            DataUtils.printdf(self.dfs[category], category.upper())

        print('Applying Filters ...     ')
        for category in self.categories:
            self.dfs[category] = DataUtils.filterdf(self.dfs[category], filters)
        
        for category, columns in self.configs['outputs'].items():
            if category in self.categories:
                print('Storing Data ...         ', end='')
                session = '' if self.session is None else f'-{self.session}'
                filename = f'{self.path}/processed/{category}{session}.csv'
                self.dfs[category][columns].drop_duplicates().to_csv(filename, index=False)
                DataUtils.printdf(self.dfs[category], category.upper())
            
