from person import Person

class PersonMemoryDB:
    def __init__(self):
        self.db = dict()

    def insert(self, item): # CREATE
        if(isinstance(item, Person)):
            if(self.select(item.rut) == None):    
                self.db[item.rut] = item
                return item
        return None

    def select(self, rut=''): # RETRIVE
        if(rut == ''):
            return self.db.values()
        else:
            return self.db.get(rut, None)

    def update(self, item): # UPDATE
        if(isinstance(item, Person)):
            if(self.select(item.rut) != None):
                self.db[item.rut] = item
                return item
        return None

    def delete(self, rut=''): # DELETE
        if(rut == ''):
            all = self.db.values()
            self.db.clear()
            return all
        else:
            return self.db.pop(rut, None)
