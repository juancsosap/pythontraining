from datatools.processors import CPEProcessor
from datatools.utils import *

class CPEAvailability:
    def __init__(self, register):
        self.register = register
        
    def process(self, availability=95, ingress_bw=0, egress_bw=0, dates='today'):
        categories = ['port-states', 'port-stats', 'latency']
        today = str(dt.date.today())
        dates = [today] if dates == 'today' else dates
        processor = CPEProcessor(self.register, categories=categories, dates=[dates])
        processor.process()
        
        print('Merging Sources ...      ', end='')
        dfs_ports = [processor.dfs['port-states'], processor.dfs['port-stats']]
        keycolumns_ports = ['hostname', 'time', 'port_id', 'date', 'week', 'group', 'app', 'timediff']
        mdf_ports = DataUtils.mergedf(dfs_ports, keycolumns_ports, how='outer')
        DataUtils.printdf(mdf_ports, 'PORTS')
        
        dfg = {}
        print('Grouping Data ...        ', end='')
        fields = [{'field':'group',       'aggs':[]}, 
                  {'field':'hostname',    'aggs':[]}, 
                  {'field':'app',         'aggs':[]}, 
                  {'field':'port_id',     'aggs':[]}, 
                  {'field':'week',        'aggs':[]}, 
                  {'field':'date',        'aggs':[('count','time'), ('sum','timediff')]},
                  {'field':'oper_state',  'aggs':[('count','time'), ('sum','timediff'), 
                                                  ('mean','ingress_bandwidth'), ('mean','egress_bandwidth')]}]
        out_columns = ['group', 'hostname', 'app', 'port_id', 'weekval', 'date', 'date_count', 'date_duration', 
                       'oper_state', 'oper_state_count', 'oper_state_duration', 'ingress_bw', 'egress_bw']
        dfg['port'] = DataUtils.dataagg(mdf_ports, fields, out_columns)
        DataUtils.printdf(dfg['port'], 'PORTS')
        
        print('Grouping Data ...        ', end='')
        fields = [{'field':'group',      'aggs':[]}, 
                  {'field':'hostname',   'aggs':[]}, 
                  {'field':'week',       'aggs':[]}, 
                  {'field':'date',       'aggs':[]}, 
                  {'field':'remote_ip',  'aggs':[('count','time'), ('sum','packet_loss'), 
                                                 ('median','latency_avg'), ('max','latency_max')]}]
        out_columns = ['group', 'hostname', 'week', 'date', 'remote_ip', 'pings', 'packet_loss', 'latency_avg', 'latency_max']
        dfg['latency'] = DataUtils.dataagg(processor.dfs['latency'], fields, out_columns)
        
        fields = [{'field':'group',      'aggs':[]}, 
                  {'field':'hostname',   'aggs':[]}, 
                  {'field':'week',       'aggs':[]}, 
                  {'field':'date',       'aggs':[('mean', 'pings'), ('min', 'packet_loss'), 
                                                 ('mean', 'latency_avg'), ('max', 'latency_max')]}]
        out_columns = ['group', 'hostname', 'weekval', 'date', 'pings', 'packet_loss', 'latency_avg', 'latency_max']
        dfg['latency'] = DataUtils.dataagg(dfg['latency'], fields, out_columns)
        DataUtils.printdf(dfg['latency'], 'LATENCY')
        
        print('Processing Data ...      ')
        dfg['port']['count_availability'] = dfg['port']['oper_state_count'] / dfg['port']['date_count']
        dfg['port']['time_availability'] = dfg['port']['oper_state_duration'] / dfg['port']['date_duration']
        dfg['port']['duration'] = dfg['port']['oper_state_duration'] / 3600
        dfg['latency']['availability'] = 1 - dfg['latency']['packet_loss'] / dfg['latency']['pings'] / 100
        for category in dfg:
            dfg[category]['week'] = dfg[category]['weekval'].apply(lambda val: 'W{:02d}'.format(val))
            dfg[category]['month'] = dfg[category]['date'].apply(lambda val: 'M' + val[5:7])
            dfg[category]['year'] = dfg[category]['date'].str.slice(0, 4)

        print('Loading List ...         ', end='')
        df_mig = {}
        df_mig['port'] = DataUtils.loadcsv(['datatools/repository/migrated.csv'])
        self.migrated = df_mig['port']
        
        df_mig['node'] = df_mig['port'].copy()
        df_mig['node']['migrated_date'] = df_mig['node']['migrated_date'].apply(lambda v: TimeUtils.todatetime(v, '%Y-%m-%d'))
        df_mig['node'] = df_mig['node'][['hostname', 'migrated_date']].groupby(['hostname']).min()
        df_mig['node']['hostname'] = df_mig['node'].index
        df_mig['node']['migrated_date'] = df_mig['node']['migrated_date'].apply(lambda v: str(v)[:10])
        df_mig['node'] = df_mig['node'].reset_index(drop=True)
        DataUtils.printdf(self.migrated, 'MIGRATED')
        
        df_mer = {}
        print('Merging List ...         ', end='')
        df_mer['port'] = DataUtils.mergedf([dfg['port'], df_mig['port']], ['hostname', 'port_id'], how='left')
        DataUtils.printdf(df_mer['port'], 'PORTS')
        
        print('Merging List ...         ', end='')
        df_mer['latency'] = DataUtils.mergedf([dfg['latency'], df_mig['node']], ['hostname'], how='left')
        DataUtils.printdf(df_mer['latency'], 'LATENCY')
        
        for category in df_mer:
            print('Processing List ...      ', end='') 
            df_mer[category]['migrated_date'] = df_mer[category]['migrated_date'].fillna('2100-01-01')
            df_mer[category]['date'] = df_mer[category]['date'].apply(lambda v: TimeUtils.todatetime(v, '%Y/%m/%d'))
            df_mer[category]['migrated_date'] = df_mer[category]['migrated_date'].apply(lambda v: TimeUtils.todatetime(v, '%Y-%m-%d'))
            df_mer[category]['migrated'] = df_mer[category]['date'] > df_mer[category]['migrated_date']
            DataUtils.printdf(df_mer[category], category.upper())

        print('Sorting Data ...')
        self.output, out_columns = {}, {}
        out_columns['port'] = ['group', 'hostname', 'app', 'port_id', 'week', 'date', 'date_count', 'date_duration', 
                               'oper_state', 'oper_state_count', 'oper_state_duration', 'count_availability', 
                               'time_availability', 'duration', 'month', 'year', 'migrated', 'ingress_bw', 'egress_bw']
        out_columns['latency'] = ['group', 'hostname', 'week', 'date', 'pings', 'packet_loss', 
                                  'latency_avg', 'latency_max', 'availability', 'month', 'year', 'migrated']
        for category in out_columns:
            df_out = df_mer[category].sort_values(['date']).reset_index(drop=True)[out_columns[category]]
            self.output[category] = df_out
        
        print('Filtering Data ...       ', end='')
        df_out = self.output['port']
        # AVAILABILITY
        dff = (df_out['migrated'] == True) & (df_out['oper_state'] == 'Down') & (df_out['time_availability'] > (100 - availability)/100)
        # EGRESS BW
        dff |= (df_out['migrated'] == True) & (df_out['oper_state'] == 'Up') & (df_out['egress_bw'] < egress_bw) 
        # INGRESS BW
        dff |= (df_out['migrated'] == True) & (df_out['oper_state'] == 'Up') & (df_out['ingress_bw'] < ingress_bw)
        
        df_sum = df_out[dff].sort_values(['hostname', 'app', 'date']).reset_index(drop=True)
        DataUtils.printdf(df_sum, 'PORTS')
        
        print('Preparing Result Data ...', end='')
        availability = lambda row: (1 - row['time_availability']) if row['oper_state'] == 'Down' else row['time_availability'] 
        df_sum['availability'] = 100 * df_sum.apply(availability, axis=1)
        columns = ['group', 'hostname', 'app', 'port_id', 'week', 'date', 'availability', 'ingress_bw', 'egress_bw']
        df_res = df_sum[columns][df_sum['date'].isin(dates)].sort_values(['hostname', 'app']).reset_index(drop=True)
        self.result = df_res
        DataUtils.printdf(df_res, 'PORTS')
    
    @staticmethod
    def printdf(df, field, title, columns=7):
        items = df[field].unique()
        items.sort()
        print(f'{title}:', len(items))
        for index, item in enumerate(items):
            print(item, end='\t')
            if index % columns == (columns-1): print()
        
    def getmigrated(self, filter_ports='all', onlyprint=False):
        result = self.migrated if filter_ports == 'all' else self.migrated[self.migrated['port_id'].isin(filter_ports)]
        CPEAvailability.printdf(result, 'hostname', 'MIGRATED CPE')
        if not onlyprint: return result.reset_index(drop=True)
        
    def getresult(self, filter_apps='all', onlyprint=False):
        result = self.result if filter_apps == 'all' else self.result[self.result['app'].isin(filter_apps)]
        CPEAvailability.printdf(result, 'hostname', 'RESULT CPE')
        if not onlyprint: return result.reset_index(drop=True)
    
    def getoutput(self, filter_apps='all', onlyprint=False):
        result = self.output['port'] if filter_apps == 'all' else self.output['port'][self.output['port']['app'].isin(filter_apps)]
        CPEAvailability.printdf(result, 'hostname', 'OUTPUT CPE')
        if not onlyprint: return result.reset_index(drop=True)
    
    def store(self):
        for category in self.output:
            output = self.output[category].copy()
            if os.path.exists(f'outputs/CPE/aggregated/{category}_{self.register}.csv'):
                df_temp = pd.read_csv(f'outputs/CPE/aggregated/{category}_{self.register}.csv')
                output = pd.concat([output, df_temp]).drop_duplicates()
            output = output.sort_values(['date', 'hostname'])
            output.to_csv(f'outputs/CPE/aggregated/{category}_{self.register}.csv', index=False)
        