import sqlite3 as dbdriver

from db_manager import DBManager
from person import Person

class PersonSqlDAO:
    def __init__(self, conn_str, driver=dbdriver):
        self.dbman = DBManager(conn_str, driver)
    
    def __enter__(self): return self

    def __exit__(self, etype, evalue, etb): pass
    
    def create(self, *items):
        created = []
        for item in items:
            sql = """INSERT INTO 'person' VALUES (:rut, :name, :age);"""
            data = {'rut':item.rut, 'name':item.name, 'age':item.age}
            try:
                self.dbman.execute(sql, data)
                created.append(item)
            except: pass
        return created if len(items) > 1 else created[0] if len(created) > 0 else None
        
    def retrive(self, *ruts):
        retrived = []
        if len(ruts) == 0:
            sql = """SELECT * FROM 'person';"""
            try:
                rows = self.dbman.query(sql)
                retrived.extend(self.add_items(*rows))
            except Exception as e: print(e)
        else:
            sql = "SELECT * FROM 'person' WHERE rut=:rut;"""
            for rut in ruts:
                try:
                    data = {'rut':rut}
                    rows = self.dbman.query(sql, data)
                    retrived.extend(self.add_items(*rows))
                except Exception as e: print(e)
        return retrived if len(ruts) != 1 else retrived[0] if len(retrived) > 0 else None

    def update(self, *items):
        updated = []
        for item in items:
            sql = """UPDATE 'person' SET name=:name, age=:age WHERE rut=:rut;"""
            data = {'rut':item.rut, 'name':item.name, 'age':item.age}
            try:
                self.dbman.execute(sql, data)
                updated.append(item)
            except Exception as e: print(e)
        return updated if len(items) > 1 else updated[0] if len(updated) > 0 else None

    def delete(self, *ruts):
        deleted = []
        if len(ruts) == 0:
            sql = """DELETE FROM 'person';"""
            try:
                items = self.retrive()
                self.dbman.execute(sql)
                deleted = items
            except Exception as e: print(e)
        else:
            sql = "DELETE FROM 'person' WHERE rut=:rut;"""
            for rut in ruts:
                try:
                    item = self.retrive(rut)
                    data = {'rut':rut}
                    self.dbman.execute(sql, data)
                    deleted.append(item)
                except Exception as e: print(e)
        return deleted if len(ruts) != 1 else deleted[0] if len(deleted) > 0 else None
    
    def add_items(self, *rows):
        items = []
        for row in rows:
            item = Person(row[0], row[1], row[2])
            items.append(item)
        return items
