from datatools.utils import *

class LocalCollector:
    dirpath = 'datatools/collectors/local/configs'
    
    def __init__(self, basefolder, group, configs=None, verbose=True, prename=None):
        self.basefolder = basefolder
        self.config = self.readconfig(group, configs)
        self.verbose = verbose
        self.prename = '' if prename is None else f'{prename}-' 

    # move data from one folder to another based on their name
    def movedata(self, srcfolder):
        if not srcfolder.startswith('/'): srcfolder = f'{self.basefolder}/{srcfolder}'
        filelist = os.listdir(srcfolder)
        days = set([val[12:20] for val in filelist])
        folders = {day:f'{day[:4]}-{day[4:6]}-{day[6:]}' for day in days}
        folderlist = os.listdir(self.basefolder)
        for day, folder in folders.items():
            dstfolder = f'{self.basefolder}/{folder}/'
            print('MOVING TO -->', dstfolder)
            #mkfolder(folder)
            if folder not in folderlist: os.mkdir(dstfolder)
            for file in filelist:
                if day in file:
                    if self.verbose: print('!', end='')
                    try:
                        shutil.move(f'{srcfolder}/{self.prename}{file}', dstfolder)
                    except: 
                        if os.path.exists(f'{srcfolder}/{self.prename}{file}'):
                            os.remove(f'{srcfolder}/{self.prename}{file}')
            print()
        return folders.values()

    # read a config JSON file and return the content as dictionary
    def readconfig(self, group, configs=None):
        basedir = f'{LocalCollector.dirpath}/{group}'
        configpath = f'{basedir}/global.json'
        config = {'global':FileUtils.readjson(configpath)}

        # read the global config references and load them into the 
        # config dictionary 
        config['configs'] = config['global']['configs'] if configs == None else configs
        for config_item in config['configs']:
            configpath = f'{basedir}/{config_item}.json'
            configfile = FileUtils.readjson(configpath)
            config[config_item] = configfile

        return config

    # get the information from a list of output files based 
    # on regex matching
    def getdata(self, config_item, custom=None):
        # load all the regex finder functions
        getters = {key:RegexUtils.getter(value) for key, value in self.config[config_item]['regex'].items()}
        data = {key:[] for key in self.config[config_item]['regex']}

        # iterate over all the folders that contain output files
        # based on the information contained in the config
        countok, countbad = 0, 0
        for sourcepath in self.config['global']['sourcefolders']:
            dirfilter = [] if custom == None else [custom]
            dirpaths = FileUtils.listfiles(sourcepath, dirfilter)
            
            # if there're any forlder on it
            # continue with the next folder
            if len(dirpaths) > 0:
                print(config_item, 'collecting folder :', sourcepath)
            else:
                print(config_item, 'ignoring folder :', sourcepath)
                break
                
            for dirpath in dirpaths:
                # if there're any forlder on it
                # continue with the next folder
                if len(dirpaths) > 0:
                    print(config_item, 'collecting folder :', dirpath)
                else:
                    print(config_item, 'ignoring folder :', dirpath)
                    break
                    
                dirpath += '/'

                # list all the output files in the folder
                filepaths = FileUtils.listfiles(dirpath)

                # verify if there are any file within the folder
                if len(filepaths) == 0:
                    print(config_item, 'skipping :', dirpath)
                    continue

                # iterate over all the output files within the folder
                countok, countbad = 0, 0
                for filepath in filepaths:
                    #print(config_item, 'collecting :', filepath)
                    bad = False

                    # read the data using the regex finder functions
                    text = FileUtils.readfile(filepath)
                    if self.config['global']['skiplines']:
                        text = text.replace('\n', '~~')
                    values = {key:[] for key in data}
                    for key in data:
                        values[key] = getters[key](text)

                    # verify data length before try to storage
                    size = len(values[self.config[config_item]['key']])
                    if size == 0:
                        #print(f'\n{config_item} empty file : {filepath}')
                        bad = True
                        if self.verbose: print('?', end='')
                        countbad += 1
                        continue

                    # verify if any data has less values than the key field
                    # and complete them the with None
                    for key, value in values.items():
                        if len(value) < size:
                            count = size - len(value)
                            values[key].extend([None for i in range(count)])

                    # if there are any field with longer data length and based on
                    # the config and multiply the other data fields by a factor
                    size = len(values[self.config[config_item]['size']])
                    for key in self.config[config_item]['multiplier']:
                        factor = math.ceil(size / len(values[key]))
                        for index in range(0, size, factor):
                            for count in range(1, factor):
                                values[key].insert(index, values[key][index])

                    # verify if any data has more values than the key field
                    # and remove them
                    for key, value in values.items():
                        if len(value) > size:
                            bad = True
                            values[key] = values[key][:(size - len(value))]

                    if bad:
                        if self.verbose: print('?', end='')
                        countbad += 1
                        continue
                    else:
                        if self.verbose: print('!', end='')
                        countok += 1

                    # record the data
                    same = True
                    for key in data:
                        if not (len(values[key]) == size):
                            print(f'\n{config_item} error file : {filepath}')
                            same = False
                            break

                    if not same:    
                        print([(key, len(val)) for key, val in values.items()])
                        continue

                    for key in data:
                        data[key].extend(values[key])

            print(f'OK: {countok}\tNOK: {countbad}')
        return pd.DataFrame(data)

    # create new fields from the existing ones
    def splitdata(self, df, config_item):
        data = {key:[] for key in self.config[config_item]['split']}

        # iterate over all the split described in the config
        for key, params in self.config[config_item]['split'].items():
            print(config_item, 'splitting :', key)

            # iterate over all items in the split described in the 
            # config
            value = df[params['field']] 
            splitter = lambda row: row if row is None else row[params['index']]
            df[key] = value.apply(splitter)
        
        return df
            
    def transformdata(self, df, config_item):
        data = {key:[] for key in self.config[config_item]['transform']}

        # iterate over all the transform described in the config
        for key in self.config[config_item]['transform']:
            print(config_item, 'transforming :', key)

            # iterate over all items in the transform described in the 
            # config
            values = []
            for item in self.config[config_item]['transform'][key]['items']:
                value = df[item['field']] 
                transform = lambda row: row if row is None else row[item['index']] if 'index' in item else row
                value = value.apply(transform)
                values.append(value)

            # apply the transform template described in the config
            # with the values prepared from the items
            operation = lambda row: self.config[config_item]['transform'][key]['template'].format(*row)
            df[key] = pd.concat(values, axis=1).apply(operation, axis=1)

        return df

    # process each data config
    def loaddata(self, config_item, custom=None):
        df = self.getdata(config_item, custom)
        if df.shape[0] > 0:
            df = self.splitdata(df, config_item)
            df = self.transformdata(df, config_item)
        return df

    # store the data in CSV files with the fields indicated in the config
    def savedata(self, custom=None):
        # iterate over each config described in the config
        for config_item in self.config['configs']:
            df = self.loaddata(config_item, custom)
            
            columns = self.config[config_item]['columns']
            currentdate = dt.date.today() if custom == None else custom
            filename = f"{self.config['global']['destinationfolder']}{config_item}/{self.prename}{config_item}-{currentdate}.csv"
            if os.path.exists(filename):
                if open(filename).read().find(',') > -1:
                    odf = pd.read_csv(filename, low_memory=False)
                    df = odf if df.shape[0] == 0 else pd.concat([odf, df[columns]], sort=False)
            
            if df.shape[0] == 0: continue
            # store the data in the file
            print(config_item, 'saving :', filename, '\n')
            df[columns].drop_duplicates().to_csv(filename, index=False, mode=self.config['global']['mode'])
        for sourcepath in self.config['global']['sourcefolders']:
            dirfilter = [] if custom == None else [custom]
            dirpaths = FileUtils.listfiles(sourcepath, dirfilter)
            for dirpath in dirpaths:
                FileUtils.mvfiles(dirpath, f'{sourcepath}/done/', movefolder=True)
        
