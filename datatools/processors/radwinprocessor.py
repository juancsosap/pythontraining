from datatools.processors.processor import *

class RadwinProcessor(Processor):
    def __init__(self, session=None, categories='all', dates=None):
        dates = [] if dates is None else dates
        super().__init__('radwin', categories, dates)
        self.session = session
        self.path = 'outputs/RADWIN'
    
    def process(self, filters={}):
        self.dfs = dict()
        for category in self.categories:
            print('Loading ...              ', end='')
            filelist = []
            for date in self.dates:
                filelist += FileUtils.listfiles(f'{self.path}/{date}/', [category])
            self.dfs[category] = DataUtils.loadcsv(filelist)
            DataUtils.printdf(self.dfs[category], category.upper())
        
        if 'data' in self.categories:
            print('Fixing ...               ', end='')
            totime = lambda t: TimeUtils.todatetime(t, '%Y-%m-%d %H:%M:%S.%f' if '.' in t else '%Y-%m-%d %H:%M:%S').replace(microsecond=0)
            self.dfs['data']['time'] = self.dfs['data']['datetime'].apply(totime)
            self.dfs['data'] = DataUtils.fillna(self.dfs['data'], 'hbstxrxrate', '0.0/0.0')
            self.dfs['data'] = DataUtils.fillna(self.dfs['data'], 'hsutxrxrate', '0.0/0.0')
            self.dfs['data']['hsutxrate'] = self.dfs['data']['hsutxrxrate'].apply(lambda r: r.split('/')[0])
            self.dfs['data']['hsurxrate'] = self.dfs['data']['hsutxrxrate'].apply(lambda r: r.split('/')[1])
            self.dfs['data']['hbstxrate'] = self.dfs['data']['hbstxrxrate'].apply(lambda r: r.split('/')[0])
            self.dfs['data']['hbsrxrate'] = self.dfs['data']['hbstxrxrate'].apply(lambda r: r.split('/')[1])
            DataUtils.printdf(self.dfs['data'], 'DATA')
        
        if 'events' in self.categories:
            print('Fixing ...               ', end='')
            totime = lambda t: TimeUtils.todatetime(t, '%m/%d/%Y %H:%M:%S')
            self.dfs['events']['time'] = self.dfs['events']['time'].apply(totime)
            DataUtils.printdf(self.dfs['data'], 'EVENTS')
        
        for category in self.categories:
            print('Processing ...           ', end='')
            self.dfs[category] = DataUtils.dropna(self.dfs[category])
            self.dfs[category] = self.setdtypes(self.dfs[category], category)
            self.dfs[category]['hostname'] = self.dfs[category]['site_name']
            self.dfs[category] = self.dfs[category].sort_values(['hostname', 'time']).reset_index(drop=True)
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
            
