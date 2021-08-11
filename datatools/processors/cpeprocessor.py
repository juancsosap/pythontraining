from datatools.processors.processor import *

class CPEProcessor(Processor):
    def __init__(self, session=None, categories='all', dates=None):
        dates = [] if dates is None else dates
        super().__init__('cpe', categories, dates)
        self.session = session
        self.path = 'outputs/CPE'
    
    def process(self, filters={}):
        self.dfs = dict()
        for category in self.categories:
            print('Loading ...              ', end='')
            self.dfs[category] = DataUtils.loadcsv(FileUtils.listfiles(f'{self.path}/{category}', [category] + self.dates))
            DataUtils.printdf(self.dfs[category], category.upper())
        
        print('Loading ...              ', end='')
        self.dfs['groups'] = DataUtils.loadcsv(['datatools/repository/cpes.csv'])
        DataUtils.printdf(self.dfs['groups'], 'CPE GROUPS')

        if 'node-status' in self.categories:
            print('Fixing ...               ', end='')
            self.dfs['node-status']['rsrp'] = self.dfs['node-status']['rsrp'].replace('<=', None)
            if 'fdb_macs' in self.dfs['node-status'].columns:
                self.dfs['node-status']['fdb_macs'] = self.dfs['node-status']['fdb_macs'].fillna(0)
            else: self.dfs['node-status']['fdb_macs'] = 0
            DataUtils.printdf(self.dfs['node-status'], 'NODE STATUS')
        
        if 'port-states' in self.categories:
            print('Fixing ...               ', end='')
            self.dfs['port-states'] = DataUtils.fillna(self.dfs['port-states'], 'encap', 'null')
            DataUtils.printdf(self.dfs['port-states'], 'PORT STATES')
        
        for category in self.categories:
            print('Processing ...           ', end='')
            self.dfs[category] = DataUtils.dropna(self.dfs[category])
            self.dfs[category] = self.dfs[category][~self.dfs[category]['time'].str.contains('None')]
            self.dfs[category]['time'] = self.dfs[category]['time'].apply(TimeUtils.fixdatetime)
            self.dfs[category] = self.setdtypes(self.dfs[category], category)
            self.dfs[category] = self.dfs[category].sort_values(['hostname', 'time']).reset_index(drop=True)
            self.dfs[category]['date'] = self.dfs[category]['time'].apply(lambda t: t.strftime('%Y/%m/%d'))
            self.dfs[category]['week'] = self.dfs[category]['time'].apply(lambda t: t.isocalendar()[1])
            DataUtils.printdf(self.dfs[category], category.upper())

            print('Merging ...              ', end='')
            self.dfs[category] = DataUtils.mergedf([self.dfs[category], self.dfs['groups']], ['hostname'], 'left')
            DataUtils.printdf(self.dfs[category], category.upper())
            
        if 'node-status' in self.categories:
            print('Loading ...              ', end='')
            self.dfs['cells'] = DataUtils.loadcsv(['datatools/repository/enbcells.csv'])[['cellname', 'cellid']]
            DataUtils.printdf(self.dfs['cells'], 'CELLS')
            
            print('Merging ...              ', end='')
            self.dfs['node-status'] = DataUtils.mergedf([self.dfs['node-status'], self.dfs['cells']], ['cellid'], 'left')
            DataUtils.printdf(self.dfs['node-status'], 'NODE STATUS')
            
            print('Fixing ...               ', end='')
            self.dfs['node-status']['cellname'] = self.dfs['node-status']['cellname'].fillna('UNKNOWN')
        
            self.dfs['node-status']['band'] = self.dfs['node-status']['band'].fillna(0)
            self.dfs['node-status']['band'] = 'Band ' + self.dfs['node-status']['band'].astype('int').astype('object').apply(str)
            self.dfs['node-status']['band'] = self.dfs['node-status']['band'].apply(lambda x: 'UNKNOWN' if x == 'Band 0' else x)
            DataUtils.printdf(self.dfs['node-status'], 'NODE STATUS')

        if 'port-states' in self.categories:
            print('Loading ...              ', end='')
            self.dfs['apps'] = DataUtils.loadcsv(['datatools/repository/cpe-ports.csv'])
            DataUtils.printdf(self.dfs['apps'], 'CPE APPS')
            
            print('Merging ...              ', end='')
            self.dfs['port-states'] = DataUtils.mergedf([self.dfs['port-states'], self.dfs['apps']], ['port_id', 'group'], 'left')
            DataUtils.printdf(self.dfs['port-states'], 'PORT STATES')
            
            print('Transforming ...         ', end='')
            self.dfs['port-states'] = self.dfs['port-states'].sort_values(['hostname', 'port_id', 'time']).reset_index(drop=True)
            
            toseconds = lambda val: val.total_seconds()
            self.dfs['port-states']['timediff'] = DataUtils.diffdf(self.dfs['port-states'], ['time'], apply=toseconds)
            dff = (self.dfs['port-states']['timediff'] > 100) | (self.dfs['port-states']['timediff'] < 0)
            self.dfs['port-states'].loc[dff, 'timediff'] = 0.0

            DataUtils.printdf(self.dfs['port-states'], 'PORT STATES')
            
        if 'port-stats' in self.categories:
            if 'groups' not in self.dfs:
                print('Loading ...              ', end='')
                self.dfs['apps'] = DataUtils.loadcsv(['datatools/repository/cpe-ports.csv'])
                DataUtils.printdf(self.dfs['apps'], 'CPE APPS')
            
            print('Merging ...              ', end='')
            self.dfs['port-stats'] = DataUtils.mergedf([self.dfs['port-stats'], self.dfs['apps']], ['port_id', 'group'], 'left')
            DataUtils.printdf(self.dfs['port-stats'], 'PORT STATS')
            
            print('Transforming ...         ', end='')
            self.dfs['port-stats'] = self.dfs['port-stats'].sort_values(['hostname', 'port_id', 'time']).reset_index(drop=True)
            
            toseconds = lambda val: val.total_seconds()
            self.dfs['port-stats']['timediff'] = DataUtils.diffdf(self.dfs['port-stats'], ['time'], apply=toseconds)
            dff = (self.dfs['port-stats']['timediff'] > 100) & (self.dfs['port-stats']['timediff'] < 0)
            self.dfs['port-stats'].loc[dff, 'timediff'] = 0.0

            tobandwith = lambda bytediff: bytediff / self.dfs['port-stats']['timediff'] * 8 / 1024
            onlypositive = lambda val: 0 if val < 0 else val
            self.dfs['port-stats']['ingress_bandwidth'] = DataUtils.diffdf(self.dfs['port-stats'], ['ingress_bytes'], 
                                                                      operation=tobandwith, apply=onlypositive)
            self.dfs['port-stats']['egress_bandwidth'] = DataUtils.diffdf(self.dfs['port-stats'], ['egress_bytes'], 
                                                                     operation=tobandwith, apply=onlypositive)

            divide = lambda x, y: x/y
            self.dfs['port-stats']['ingress_mtu'] = DataUtils.diffdf(self.dfs['port-stats'], ['ingress_bytes', 'ingress_packets'], 
                                                                operation=divide)
            self.dfs['port-stats']['egress_mtu'] = DataUtils.diffdf(self.dfs['port-stats'], ['egress_bytes', 'egress_packets'], 
                                                               operation=divide)

            self.dfs['port-stats'] = DataUtils.dropdf(self.dfs['port-stats'], 'timediff', lambda t: t.isna() | (t <= 0))
            DataUtils.printdf(self.dfs['port-stats'], 'PORT STATS')

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
            
