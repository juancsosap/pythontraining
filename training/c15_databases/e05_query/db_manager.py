# Package Drivers

# SQLite3 Database
# import sqlite3 as dbdriver
# conn_str = db_file_path
# conn_str = 'data.db'

# SQL Server Database
# import pyodbc as dbdriver
# conn_str = 'Driver={SQL Server};Server=server_name;Database=db_name;Trusted_Connection=yes;'
# conn_str = 'Driver={SQL Server};Server=MyDatabaseServer;Database=ProductionDB;Trusted_Connection=yes;'

# Oracle Database
# import cx_Oracle as dbdriver
# conn_str = 'username/password@server-ip/db_name'
# conn_str = 'admin/admin@127.0.0.1/productiondb'
 
# MySQL Database            py
# import mysql.connector as dbdriver
# conn_config = { 'user': username, 'password': password, 'host': server-ip, 'database': db_name, 'raise_on_warnings': True }
# conn_config = { 'user': 'admin, 'password': 'admin', 'host': '127.0.0.1', 'database': 'productiondb, 'raise_on_warnings': True }

import sqlite3 as dbdriver
import re

class DBManager:
    def __init__(self, conn_str, driver=dbdriver):
        print('Connecting to Database')
        self.conn = driver.connect(conn_str) # driver.connect(**conn_config) for MySQL
        self.cursor = self.conn.cursor()

    def __del__(self):
        print('Disconnecting from Database')
        if self.conn: self.conn.close()
    
    def __enter__(self): return self

    def __exit__(self, etype, evalue, etb): del self
    
    @staticmethod
    def split_sql(sql):
        regex = r'--.*|/\*.*\*/;|\n'
        sql = re.sub(regex, '', sql)
        return sql.split(';')

    def execute(self, sql, batch=False):
        if batch:
            for cmd in self.split_sql(sql)[:-1]:
                self.cursor.execute(cmd) 
        else:
            self.cursor.execute(sql)
        self.conn.commit()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
