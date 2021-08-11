import pandas as pd
from pexpect import pxssh
import re

from datatools.utils import *

class Executor:
    dirpath = 'datatools/collectors/cli/configs'
    
    def __init__(self, script, verbose=False):
        self.config = FileUtils.readjson(f'{Executor.dirpath}/{script}.json')
        self.loadhosts()
        self.verbose = verbose
        self.now = dt.datetime.now()
        
        self.regexcompile()

    def loadhosts(self):
        hosts = FileUtils.readjson(f'{Executor.dirpath}/hosts.json')
        self.hosts = {hostname:hosts[hostname] for hostname in self.config['hosts']}
            
    def ssh(self, host):
        ses = pxssh.pxssh()
        ip = self.hosts[host]['ip']
        user, pswd = tuple(self.hosts[host]['auth'].split(' '))
        cmds = self.config['commands']
        try:
            if ses.login(ip, user, pswd, auto_prompt_reset=False):
                ses.sync_original_prompt()
                for cmd in cmds:
                    ses.sendline(cmd)
                    ses.prompt(self.config['wait'])
                output = ses.before.decode('utf-8').replace('\r\n', '\n')
                ses.close()
                print('\tOK')
                if self.verbose: print(output)
                return output, 'OK'
        except Exception as e:
            print('\tERROR:', e)
        return '', 'FAIL'
    
    def regexcompile(self):
        for file in self.config['files']:
            self.config['files'][file]['cregex'] = []
            for regex in self.config['files'][file]['regex']:
                #print(regex)
                cre = re.compile(regex)
                self.config['files'][file]['cregex'].append(cre)

    def log(self, hostname, ip_node, role, location, state):
        data = {'hostname':[hostname], 'ip_node':[ip_node], 'role':[role], 
                'location':[location], 'state':[state]}
        self.savecsv('log', pd.DataFrame(data))
        
    def savecsv(self, item, df):
        today = dt.date.today()
        folder = self.config['outputfolder'] + f'/{today}'
        FileUtils.mkfolder(folder)
        filepath = f'{folder}/{self.now}_{item}.csv'
        if os.path.isfile(filepath):
            df = pd.concat([pd.read_csv(filepath, sep=';'), df])
        df.to_csv(filepath, sep=';', index=False)
    
    def getdata(self, file, text):
        results = {}
        for cre in self.config['files'][file]['cregex']:
            groups = cre.groupindex.items()
            for items in cre.findall(text):
                for name, index in groups:
                    value = items[index-1] if len(groups) > 1 else items
                    value = value.replace(';', ',')
                    if name not in results:
                        results[name] = []
                    results[name].append(value)
        return results
    
    def savedata(self, file, data, ip_node):
        df = pd.DataFrame(data)
        df['ip_node'] = ip_node
        self.savecsv(file, df)
        
    def run(self, host, verbose=False):
        ip_node = self.hosts[host]['ip']
        print(host, ip_node, self.hosts[host]['role'], self.hosts[host]['location'], sep='\t', end='')
        tmp_path = f'tmp/{ip_node}.tmp'
        result, state = self.ssh(host)
        self.log(host, ip_node, self.hosts[host]['role'], self.hosts[host]['location'], state)
        for file in self.config['files']:
            output = self.getdata(file, result)
            if verbose: print(output)
            self.savedata(file, output, ip_node)
