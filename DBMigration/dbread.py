# -*- coding:utf-8 -*-

import pymysql
import sqlite3
import io


class MySQLDBManager:

    def __init__(self, **kwargs):
        self.host = kwargs['host'] if 'host' in kwargs else 'localhost'
        self.port = kwargs['port'] if 'port' in kwargs else 3306
        self.user = kwargs['user'] if 'user' in kwargs else 'root'
        self.password = kwargs['password']
        self.db = kwargs['db']

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port,
                                    db=self.db, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


class SQLiteDBManager:

    def __init__(self, target):
        self.target = str(target)

    def connect(self):
        self.conn = sqlite3.connect(self.target)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


if __name__ == '__main__':
    dbmngrMySQL = MySQLDBManager(password='roottoor', db='world')
    dbmngrMySQL.connect()
    resultMySQL = dbmngrMySQL.execute('SELECT * FROM city')
    with io.open('world.csv', 'w', encoding='utf-8') as file:
        for register in resultMySQL:
            ID, name, countryCode, disctrict, population = register
            file.write(f'{ID},{name},{countryCode},{disctrict},{population}\n')

    dbmngrSQlite = SQLiteDBManager('world.db')
    dbmngrSQlite.connect()
    dbmngrSQlite.execute('''CREATE TABLE IF NOT EXISTS city (ID integer, 
		                                             name text, 
		                                             countryCode text, 
		                                             disctrict text, 
		                                             population integer)''')
    for register in resultMySQL:
        ID, name, countryCode, disctrict, population = register
        dbmngrSQlite.execute(f'''INSERT INTO city VALUES({ID},
			                                      "{name}",
			                                      "{countryCode}",
			                                      "{disctrict}",
			                                       {population})''')

    resultSQlite = dbmngrSQlite.execute('SELECT * FROM city')
    for register in resultSQlite:
        ID, name, countryCode, disctrict, population = register
        print(f'{ID},{name},{countryCode},{disctrict},{population}')

    resultMySQL2 = dbmngrMySQL.execute('SELECT code, name FROM country')

    dbmngrSQlite.execute('''CREATE TABLE IF NOT EXISTS country (code text, 
		                                             name text)''')
    for register in resultMySQL2:
        code, name = register
        dbmngrSQlite.execute(f'''INSERT INTO country VALUES("{code}",
			                                      "{name}")''')

    resultSQlite = dbmngrSQlite.execute('SELECT * FROM country')
    for register in resultSQlite:
        code, name = register
        print(f'{code},{name}')

    dbmngrSQlite.disconnect()
    dbmngrMySQL.disconnect()
