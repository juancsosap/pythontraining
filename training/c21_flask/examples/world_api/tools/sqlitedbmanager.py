# -*- coding:utf-8 -*-

import sqlite3

from tools.dbmanager import DBManager


class SqliteDBManager(DBManager):

    def __init__(self, dbpath):
        self.dbpath = dbpath
        self.connect()

    def getconnection(self):
        return sqlite3.connect(self.dbpath)


module_name = 'tools.SqliteDBManager'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
