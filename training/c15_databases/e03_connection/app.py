import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

from db_manager import DBManager

dbpath = basedir + '../data/data.db'

if __name__ == "__main__":    
    with DBManager(dbpath) as db:
        print('Opened Database 1')

    with DBManager(dbpath) as db:
        print('Opened Database 2')

    db = DBManager(dbpath)
    print('Opened Database 3') 
