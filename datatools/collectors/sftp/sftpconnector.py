import paramiko, time

from datatools.utils import *

class SFTPConnector:
    dirpath = 'datatools/collectors/sftp/configs'
    
    def __init__(self, script, timeout=5):
        self.config = FileUtils.readjson(f'{SFTPConnector.dirpath}/{script}.json')
        self.loadhosts()
        self.timeout = timeout
    
    def loadhosts(self):
        self.items, self.hosts = {}, []
        for net in self.config['hosts']:
            network, prefix = tuple(net['ip-network'].split('/'))
            for ip in IPv4(network, int(prefix)).hostrange():
                self.items[ip] = net['auth']
                self.hosts.append(ip)
    
    def run(self, host):
        self.results = []
        
        if host in self.config['exclude']:
            print('EXCLUDED\n')
            return
        
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            user, pswd = tuple(self.items[host].split(' '))
            
            commands = self.config['commands']
            for command in commands:
                try:
                    print(command['operation'].upper(), '', end='')
                    ssh.connect(hostname=host, username=user, password=pswd, port=22, timeout=self.timeout)
                    
                    if command['operation'] == 'get':
                        print(command['source'], 'from', command['destination'], end='')
                        sftp = ssh.open_sftp()
                        
                        sftp.get(command['source'], command['destination'])
                        self.results.append((command['source'], False))
                        
                        print('\tOK')
                    if command['operation'] == 'put':
                        print(command['source'], 'to', command['destination'], end='')
                        sftp = ssh.open_sftp()
                        
                        sftp.put(command['source'], command['destination'])
                        self.results.append((command['source'], False))
                        
                        print('\tOK')
                    if command['operation'] == 'cli':
                        print('execute command :', command['command'], end='')
                        chan = ssh.invoke_shell()
                        
                        while not chan.send_ready(): time.sleep(0.1)
                        chan.send(command['command'] + '\n')
                        
                        time.sleep(command['wait'])
                            
                        while not chan.recv_ready(): time.sleep(0.1)
                        self.results.append((chan.recv(100_000).decode('utf-8'), False))
                        
                        print('\tOK')
                
                except Exception as e:
                    if str(e) == 'timed out':
                        print('\tERROR', e)
                        break
                    else:
                        self.results.append(('', True))
                        print('\tFAIL')

                ssh.close()
                time.sleep(1)
            print()
                
        except Exception as e:
            print('Error:', e, end='\n\n')