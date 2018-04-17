# -*- coding:utf-8 -*-

from db import DB


class MemoryDB(DB):

    def __init__(self):
        self.data = ['TEST0', 'TEST1', 'TEST2', 'TEST3']

    def create(self, value):
        self.data.append(value)
        return len(self.data) - 1

    def retrive(self, index):
        return self.data[int(index)]

    def retrive_all(self):
        return self.data

    def update(self, index, value):
        self.data[int(index)] = value

    def delete(self, value):
        self.data.remove(value)


module_name = 'MemoryDB'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
