from person_memory_db import PersonMemoryDB

class PersonMemoryDAO:
    def __init__(self):
        self.db = PersonMemoryDB()
    
    def create(self, *items):
        created = []
        for item in items:
            item = self.db.insert(item)
            if item != None: created.append(item)
        return created if len(items) > 1 else created[0] if len(created) > 0 else None
    
    def retrive(self, *ruts):
        if(len(ruts) == 0):
            return self.db.select()
        else:
            retrived = []
            for rut in ruts:
                item = self.db.select(rut)
                if item != None: retrived.append(item)
        return retrived if len(ruts) != 1 else retrived[0] if len(retrived) > 0 else None

    def update(self, *items):
        updated = []
        for item in items:
            item = self.db.update(item)
            if item != None: updated.append(item)
        return updated if len(items) > 1 else updated[0] if len(updated) > 0 else None

    def delete(self, *ruts):
        if(len(ruts) == 0):
            return self.db.delete()
        else:
            deleted = []
            for rut in ruts:
                item = self.db.delete(rut)
                if item != None: deleted.append(item)
        return deleted if len(ruts) != 1 else deleted[0] if len(deleted) > 0 else None
