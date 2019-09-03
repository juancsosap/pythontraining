import sqlite3 as dbdriver
import json

from db_manager import DBManager

class GenericSqlDAO:
    def __init__(self, conn_str, config_path, element, tablename, driver=dbdriver):
        self.dbman = DBManager(conn_str, driver)
        self.element = element

        with open(config_path) as file:
            self.config = json.loads(file.read())[tablename]
    
    def __enter__(self): return self

    def __exit__(self, etype, evalue, etb): pass
    
    def create(self, *items):
        created = []
        for item in items:
            sql = self.config['create']
            data = item.__dict__
            try:
                self.dbman.execute(sql, data)
                created.append(item)
            except: pass
        return created if len(items) > 1 else created[0] if len(created) > 0 else None
        
    def retrive(self, *idxs):
        retrived = []
        if len(idxs) == 0:
            sql = self.config['retriveall']
            try:
                rows = self.dbman.query(sql)
                retrived.extend(self.add_items(*rows))
            except Exception as e: print(e)
        else:
            sql = self.config['retrive']
            for idx in idxs:
                try:
                    data = [idx]
                    rows = self.dbman.query(sql, data)
                    retrived.extend(self.add_items(*rows))
                except Exception as e: print(e)
        return retrived if len(idxs) != 1 else retrived[0] if len(retrived) > 0 else None

    def update(self, *items):
        updated = []
        for item in items:
            sql = self.config['update']
            data = item.__dict__
            try:
                self.dbman.execute(sql, data)
                updated.append(item)
            except Exception as e: print(e)
        return updated if len(items) > 1 else updated[0] if len(updated) > 0 else None

    def delete(self, *idxs):
        deleted = []
        if len(idxs) == 0:
            sql = self.config['deleteall']
            try:
                items = self.retrive()
                self.dbman.execute(sql)
                deleted = items
            except Exception as e: print(e)
        else:
            sql = self.config['delete']
            for idx in idxs:
                try:
                    item = self.retrive(idx)
                    data = [idx]
                    self.dbman.execute(sql, data)
                    deleted.append(item)
                except Exception as e: print(e)
        return deleted if len(idxs) != 1 else deleted[0] if len(deleted) > 0 else None
    
    def add_items(self, *rows):
        items = []
        for row in rows:
            item = self.element(*row)
            items.append(item)
        return items
