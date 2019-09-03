import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

from db_manager import DBManager
from person_sql_dao import PersonSqlDAO
from person import Person

dbpath = basedir + '../data/data.db'
sqlpath = basedir + '../data/person.sql'

if __name__ == "__main__":
    with DBManager(dbpath) as dbman:
        sql = open(sqlpath).read()
        dbman.execute(sql, batch=True)

    print('-'*50)
        
    with PersonSqlDAO(dbpath) as dao:
        for person in dao.retrive():
            print(person)
        
        print('-'*50)

        p1 = Person('12.345.678-9', 'Ana Prada', 50)
        print(dao.update(p1))

        print('-'*50)

        print(dao.retrive('12.345.678-9'))

        print('-'*50)

        for person in dao.retrive():
            print(person)
        
        print('-'*50)

        print(dao.delete('12.345.678-9'))

        print('-'*50)

        for person in dao.retrive():
            print(person)

        print('-'*50)

        print(dao.create(p1))

        print('-'*50)

        for person in dao.retrive():
            print(person)

        print('-'*50)
        