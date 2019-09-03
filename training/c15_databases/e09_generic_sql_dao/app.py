import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

from db_manager import DBManager
from generic_sql_dao import GenericSqlDAO
from person import Person
from country import Country

dbpath = basedir + '../data/data.db'
daoconfig = basedir + '../data/data.json'

sqlpath_person = basedir + '../data/person.sql'
sqlpath_country = basedir + '../data/country.sql'

if __name__ == "__main__":
    with DBManager(dbpath) as dbman:
        sql = open(sqlpath_person).read()
        dbman.execute(sql, batch=True)

    with DBManager(dbpath) as dbman:
        sql = open(sqlpath_country).read()
        dbman.execute(sql, batch=True)
    
    with GenericSqlDAO(dbpath, daoconfig, Person, 'person') as dao:
        print('-'*50)
    
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
        
        print()

    with GenericSqlDAO(dbpath, daoconfig, Country, 'country') as dao:
        print('-'*50)
    
        for country in dao.retrive():
            print(country)
        
        print('-'*50)

        c1 = Country('VEN', 'Republica de Venezuela', 'America')
        print(dao.update(c1))

        print('-'*50)

        print(dao.retrive('VEN'))

        print('-'*50)

        for country in dao.retrive():
            print(country)
        
        print('-'*50)

        print(dao.delete('VEN'))

        print('-'*50)

        for country in dao.retrive():
            print(country)

        print('-'*50)

        print(dao.create(c1))

        print('-'*50)

        for country in dao.retrive():
            print(country)

        print('-'*50)
        