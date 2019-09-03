import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

from db_manager import DBManager

dbpath = basedir + '../data/data.db'
sqlpath = basedir + '../data/script.sql'

if __name__ == "__main__":
    with DBManager(dbpath) as dbman:
        sql = open(sqlpath).read()
        dbman.execute(sql, True)

        sql = '''SELECT * FROM person'''
        table = dbman.query(sql)

        for row in table:
            print(row)
