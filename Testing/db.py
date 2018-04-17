import sqlite3
import pymysql # pip install PyMySQL
from functools import reduce

class Person:
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age

class DBManager:
	def __init__(self, driver='sqlite3', db=':memory', port=3306,
		         host='localhost', user='root', password=''):
		self.connect(driver, db, host, user, password, port)

	def __del__(self):
		self.disconnect()
	
	def connect(self, driver, db, host, user, password, port):
		print('DB connected\n')
		if driver == 'sqlite3':
			self.__conn = sqlite3.connect(db)
		elif driver == 'pymysql':
			self.__conn =pymysql.connect(user=user, password=password, host=host, db=db, port=port)
		self.__curs = self.__conn.cursor()
		
	def disconnect(self):
		print('DB disconnected\n')
		del self.__curs
		self.__conn.close()
		del self.__conn
	
	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		del self

	def create_table(self, table, fields):
		flds = [f'{x} {y}' for x, y in fields]
		flds = reduce(lambda x,y: f'{x}, {y}',flds)
		sql = f'''CREATE TABLE IF NOT EXISTS {table} ( {flds} )'''
		self.__curs.execute(sql)
		self.__conn.commit()

	def insert_data(self, table, fields, values):
		for val in values:
			vals = [f'"{vls}"' if tpe == 'text' else f'{vls}' for fld, tpe in fields for key, vls in val.__dict__.items() if fld == key]
			vals = reduce(lambda x,y: f'{x}, {y}',vals)
			flds = [f'{fld}' for fld, tpe in fields]
			flds = reduce(lambda x,y: f'{x}, {y}',flds)
			sql = f'''INSERT INTO {table} ( {flds} ) VALUES ( {vals} )'''
			self.__curs.execute(sql)
		self.__conn.commit()

	def retrive_data(self, table, fields):
		flds = [f'{x}' for x, y in fields]
		flds = reduce(lambda x,y: f'{x}, {y}',flds)
		sql = f'''SELECT {flds} FROM {table}'''
		self.__curs.execute(sql)
		result = self.__curs.fetchall()
		self.__conn.commit()
		return result


if __name__ == '__main__':
	with DBManager(db='people.db') as dbman:

		fields = [('name', 'text'), 
		          ('surname', 'text'), 
		          ('age', 'integer')]
		table = 'people'
		dbman.create_table('people', fields)

		people = [Person('Juan', 'Sosa', 35), 
		          Person('Carlos', 'Perez', 50),
				  Person('Maria', 'Lopez', 15), 
				  Person('Ana', 'Prada', 60)]
		dbman.insert_data(table, fields, people)

		data = dbman.retrive_data(table, fields)
		for name, surname, age in data:
			print(f'Name:\t\t{name}')	
			print(f'Surname:\t{surname}')	
			print(f'Age:\t\t{age}\n')	

	with DBManager(driver='pymysql', host='localhost', user='root',
            password='roottoor', db='mydb', port=3306) as dbman:

		fields = [('name', 'text'), 
		          ('surname', 'text'), 
		          ('age', 'integer')]
		table = 'people'
		dbman.create_table('people', fields)

		people = [Person('Juan', 'Sosa', 35), 
		          Person('Carlos', 'Perez', 50),
				  Person('Maria', 'Lopez', 15), 
				  Person('Ana', 'Prada', 60)]
		dbman.insert_data(table, fields, people)

		data = dbman.retrive_data(table, fields)
		for name, surname, age in data:
			print(f'Name:\t\t{name}')	
			print(f'Surname:\t{surname}')	
			print(f'Age:\t\t{age}\n')	