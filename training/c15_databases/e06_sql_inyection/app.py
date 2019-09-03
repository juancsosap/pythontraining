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

        print('Authentication')
        username = input('Username : ') # ' OR ''='
        password = input('Password : ') # ' OR ''='
        
        sql = '''SELECT email, password FROM person WHERE email='{}' AND password='{}';'''
        table = dbman.query(sql.format(username, password))

        if(len(table) == 0):
            print('Rejected')
        else:
            print('Authenticated')
        
            sql = '''SELECT * FROM person WHERE email='{email}';'''
            table = dbman.query(sql.format(email=username))

            for row in table:
                print(row)
