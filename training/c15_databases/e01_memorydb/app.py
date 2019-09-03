from person import Person
from person_memory_db import PersonMemoryDB
    
if __name__ == "__main__":
    db = PersonMemoryDB()
    print('Quantity:', len(db.select()))
    print(db.insert(Person('23.914.881-6', 'Juan Sosa', 37)))
    print('Quantity:', len(db.select()))
    print(db.insert(Person('23.914.890-5', 'Ana Prada', 36)))
    print('Quantity:', len(db.select()))
    print(db.insert(Person('23.914.881-6', 'Luis Perez', 37)))
    print('Quantity:', len(db.select()))
    print(db.update(Person('23.914.881-6', 'Luis Perez', 37)))
    print('Quantity:', len(db.select()))
    print(db.delete('23.914.881-6'))
    print('Quantity:', len(db.select()))
