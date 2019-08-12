# -*- coding:utf-8 -*-

from tools.mysqldbmanager import MySQLDBManager


class DAO:

    def __init__(self):
        self.dbman = MySQLDBManager(password='roottoor', db='world')

    def create(self, obj):
        pass

    def retrive(self, obj):
        pass

    def retrive_all(self, offset, limit):
        pass

    def retrive_next(self, obj):
        pass

    def retrive_previous(self, obj):
        pass

    def update(self, obj):
        pass

    def delete(self, obj):
        pass


module_name = 'tools.DAO'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
