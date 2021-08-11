from datatools.utils import * 

class Processor:
    dirpath = 'datatools/processors/configs'
    
    def __init__(self, config_item, categories='all', dates=None):
        self.configs = FileUtils.readjson(f'{Processor.dirpath}/{config_item}.json')
        self.categories = tuple(self.configs['dtypes'].keys()) if categories == 'all' else categories
        self.dates = dates
        
    def process(self, filters={}):
        pass
    
    # set dtypes to the fields in a pandas dataframe
    # base on a category in the config
    def setdtypes(self, df, category):
        for field, dtype in self.configs['dtypes'][category].items():
            df[field] = df[field].astype(dtype)
        return df
