import pandas as pd
import numpy as np
import os

from datatools.utils import FileUtils, TimeUtils

class DataUtils:
    dirpath = 'datatools/utils/configs'
    
    # verify that all values are equals
    @staticmethod
    def comparerows(row1, row2, fields, condition):
        result = True
        for field in fields:
            result = result and condition(row1[field], row2[field])
        return result
    
    # load a pandas dataframe from multiple csv files
    @staticmethod
    def loadcsv(filepaths, dropduplicates=True):
        dflist = []
        for filepath in filepaths:
            if os.path.exists(filepath):
                df = pd.read_csv(filepath, low_memory=False)
                dflist.append(df)
        rdf = pd.concat(dflist, sort=False) if len(dflist) > 1 else dflist[0]
        if dropduplicates:
            rdf = rdf.drop_duplicates()
        return rdf
    
    # add data to csv file
    @staticmethod
    def addtocsv(filepath, data, dropduplicates=True):
        for key in data:
            if type(data[key]) != list:
                data[key] = [data[key]]
        ndf = pd.DataFrame(data)
        if os.path.exists(filepath):
            odf = pd.read_csv(filepath, low_memory=False)
            ndf = pd.concat([odf, ndf], sort=False)
        if dropduplicates:
            ndf = ndf.drop_duplicates()
        ndf.to_csv(filepath, index=False)
        
    # merge many dataframes using the given key fields
    @staticmethod
    def mergedf(dfs, keyfields, how='inner'):
        df = dfs[0]
        for odf in dfs[1:]:
            df = pd.merge(df, odf, on=keyfields, how=how)
        return df
    
    # merge many dataframes using the given condition
    @staticmethod
    def mergedfbycond(d1, d2, keys, cond, outcol):
        data = {k:[] for k in outcol}
        for key in keys:
            data[key] = []
        for index1 in d1.index:
            for index2 in d2.index:
                if cond(d1.iloc[index1], d2.iloc[index2]):
                    for key in keys:
                        data[key].append(d1.iloc[index1][key])
                    for k in outcol:
                        if k not in keys:
                            data[k].append(d2.iloc[index2][k])
                    break
        return pd.merge(d1, pd.DataFrame(data), on=keys, how='left')

    # apply operations between pandas dataframe fields differences
    @staticmethod
    def diffdf(df, fields, count=1, operation=None, apply=None):
        ddfs = [df[field].diff(count) for field in fields]
        if not (operation == None):
            ddfs = [operation(*ddfs)]
        if not (apply == None):
            ddfs = [ddf.apply(apply) for ddf in ddfs]
        return ddfs[0] if len(ddfs) == 1 else tuple(ddfs)
    
    # drop rows from a pandas dataframe based on conditions
    @staticmethod
    def dropdf(df, field, condition):
        df_filter = ~condition(df[field])
        return df[df_filter]

    # fill null or na values with a value within a
    # pandas dataframe
    @staticmethod
    def fillna(df, field, value):
        df[field] = df[field].fillna(value)
        return df

    # drop None and na values in a pandas dataframe
    # others aditional values could be considered
    # to be dropped
    @staticmethod
    def dropna(df, others=['None', 'None None']):
        df = df.replace(others, None)
        df = df.dropna()
        return df
    
    # print pandas dataframe
    @staticmethod
    def printdf(df, name='', size=None):
        print('{:<10} {:<15}'.format(name, str(list(df.shape))))
        if size != None:
            if size == 0:
                print(list(df.columns))
            elif size > 0:
                return df.head(size)

    # print series
    @staticmethod
    def prettyds(ds, columns=6):
        text = ''
        for index, data in enumerate(list(ds)):
            text += '{:<10}\t'.format(data)
            text += '\n' if (index + 1) % columns == 0 else ''
        return text
    
    # filter pandas dataframe based on filters 
    @staticmethod
    def filterdf(df, filters):
        for field, params in filters.items():
            if field in df.columns:
                if params['type'] == 'string':
                    if 'values' in params:
                        df_filter = df[field].isin(params['values'])
                    else:
                        df_filter = False
                        for pattern in params['pattern']:
                            df_filter = df[field].str.contains(pattern) | df_filter 
                if params['type'] == 'number':
                    if 'equal' in params:
                        df_filter = (df[field] == params['equal'])
                    else:
                        df_filter = True
                        if 'max' in params:
                            df_filter &= (df[field] <= params['max'])
                        if 'min' in params:
                            df_filter &= (df[field] >= params['min'])
                df = df[df_filter].reset_index(drop=True)
        return df
    
    @staticmethod
    def importfilters(filterlist):
        configs = FileUtils.readjson(f'{DataUtils.dirpath}/filters.json') 
        maps = FileUtils.readjson(f'{DataUtils.dirpath}/maps.json') 

        filters = dict()
        for filteritem in filterlist:
            if not filteritem.startswith('|'):
                filters.update(config[filteritem]['definition'])
            else:
                items = filteritem[1:].split('|')
                template = configs[f'|{items[0]}']['template']
                values = items[1:]
                for fkey, field in template.items():
                    fillfilter = {'type':field['type']}
                    for ikey, item in field['items'].items():
                        if item['type'] == 'string':
                            fillfilter[ikey] = item['template'].format(*values)
                            continue
                        if item['type'] == 'list':
                            fillfilter[ikey] = [item['template'].format(value) for value in values]
                            continue
                        if item['type'] == 'coordinates':
                            fillfilter[ikey] = maps[items[1]][fkey][ikey]
                            continue
                    filters[fkey] = fillfilter
        return DataUtils.updatefilters(filters)
    
    @staticmethod
    def updatefilters(filters):
        for fkey, field in filters.items():
            if field['type'] == 'time':
                filters[fkey]['type'] = 'number'
                filters[fkey]['min'] = TimeUtils.todatetime(filters[fkey]['min'])
                filters[fkey]['max'] = TimeUtils.todatetime(filters[fkey]['max'])
            if field['type'] == 'coordinates':
                filters[fkey]['type'] = 'number'
                filters[fkey]['min'] = DataUtils.tocoo(*filters[fkey]['min'])
                filters[fkey]['max'] = DataUtils.tocoo(*filters[fkey]['max'])
        return filters

    # generate a decimal coordinate
    @staticmethod
    def tocoo(grades, minutes, seconds):
        return grades + minutes / 60 + seconds / 3600
    
    @staticmethod
    def describedata(data, fieldlabel, fieldvalue):
        info = pd.DataFrame({fieldlabel:data[fieldlabel], '%':data[fieldvalue]})
        size = info.shape[0]
        percentage = info.groupby(fieldlabel).count()/size*100
        return percentage.apply(lambda x:round(x,2)) 
    
    @staticmethod
    def foreach(df, fields, register={}):
        result = []
        field = fields[0]
        items = df[field['field']].unique()
        for item in items:
            item_filter = df[field['field']] == item
            register[field['field']] = [item]
            for agg, aggfield in field['aggs']:
                register[field['field']].append(df[item_filter][aggfield].agg(agg))
            if len(fields) > 1:
                inner_result = DataUtils.foreach(df[item_filter], fields[1:], register)
                for inner in inner_result:
                    result.append(inner)
            else:
                result.append(register.copy())
        return result
    
    @staticmethod
    def dataagg(df, fields, columns=None):
        groups = DataUtils.foreach(df, fields, {})
        result = {}
        for group in groups:
            for gindex, key in enumerate(group):
                if key not in result:
                    result[key] = []
                    for aindex, aggdata in enumerate(fields[gindex]['aggs']):
                        agg, aggfield = aggdata
                        result[f'{key}_{aindex}'] = []
                result[key].append(group[key][0])
                for aindex, aggdata in enumerate(fields[gindex]['aggs']):
                    agg, aggfield = aggdata
                    result[f'{key}_{aindex}'].append(group[key][aindex + 1])
        df = pd.DataFrame(result)
        if not (columns is None):
            df.columns = columns
        return df
