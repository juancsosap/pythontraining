class Person:
    def __init__(self, rut, name, age):
        self.rut = rut
        self.name = name
        self.age = age

class MemoryDB:
    def __init__(self, type):
        self.db = []
        self.type = type

    def search(self, rut):
        ruts = [r for r in map(lambda p : p.rut, self.db)]
        if(rut in ruts):
            idx = ruts.index(rut)
            return self.db[idx]
        else:
            return None

    def insert(self, item):
        if(item is self.type):
            self.db.add(item)
        else:
            raise Exception('Invalid Input')

    def delete(self, rut):
        item = search(rut)
        if(item is not None):
            self.db.remove(item)
        else:
            raise Exception('Input not Available')
    
def main():
    db = MemoryDB(Person)
    db.add(Person('23.9141.881-6', 'Juan Sosa', 37))


if __name__ == "__main__":
    main()