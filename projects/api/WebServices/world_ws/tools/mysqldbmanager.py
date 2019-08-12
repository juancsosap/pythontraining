# -*- coding:utf-8 -*-

import pymysql

from tools.dbmanager import DBManager


class MySQLDBManager(DBManager):

    def __init__(self, **kwargs):
        self.host = kwargs['host'] if 'host' in kwargs else 'localhost'
        self.port = kwargs['port'] if 'port' in kwargs else 3306
        self.user = kwargs['user'] if 'user' in kwargs else 'root'
        self.autocommit = kwargs['autocommit'] if 'autocommit' in kwargs else True
        self.password = kwargs['password']
        self.db = kwargs['db']
        self.connect()

    def getconnection(self):
        return pymysql.connect(host=self.host, port=self.port, autocommit=self.autocommit,
                               user=self.user, password=self.password, db=self.db)


module_name = 'tools.MySQLDBManager'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
