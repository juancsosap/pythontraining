# Package Drivers

# SQLite3 Database
# import sqlite3 as dbdriver
# conn_config = db_file_path
# conn_config = 'data.db'

# SQL Server Database
# import pyodbc as dbdriver
# conn_config = 'Driver={SQL Server};Server=server_name;Database=db_name;Trusted_Connection=yes;'
# conn_config = 'Driver={SQL Server};Server=MyDatabaseServer;Database=ProductionDB;Trusted_Connection=yes;'

# Oracle Database
# import cx_Oracle as dbdriver
# conn_config = 'username/password@server-ip/db_name'
# conn_config = 'admin/admin@127.0.0.1/productiondb'
 
# MySQL Database            
# import mysql.connector as dbdriver
# conn_config = { 'user': username, 'password': password, 'host': server-ip, 'database': db_name, 'raise_on_warnings': True }
# conn_config = { 'user': 'admin, 'password': 'admin', 'host': '127.0.0.1', 'database': 'productiondb, 'raise_on_warnings': True }

import sqlite3 as dbdriver
import re

class DBManager:
    def __init__(self, conn_config, driver=dbdriver):
        print('Connecting to Database')
        if(isinstance(conn_config, dict)):
            self.conn = driver.connect(**conn_config) # For MySQL
        else:    
            self.conn = driver.connect(conn_config) 
        self.cursor = self.conn.cursor()

    def __del__(self):
        print('Disconnecting from Database')
        if self.conn: self.conn.close()
    
    def __enter__(self): return self

    def __exit__(self, etype, evalue, etb): pass
    
    @staticmethod
    def split_sql(sql):
        regex = r'--.*|/\*.*\*/;|\n'
        sql = re.sub(regex, '', sql)
        return sql.split(';')

    def execute(self, sql, data=[], batch=False):
        if batch:
            for cmd in self.split_sql(sql):
                self.cursor.execute(cmd, data) 
        else:
            self.cursor.execute(sql, data)
        self.conn.commit()

    def query(self, sql, data=[]):
        self.cursor.execute(sql, data)
        result = self.cursor.fetchall()
        return result
