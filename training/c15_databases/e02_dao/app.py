from person_memory_dao import PersonMemoryDAO
from person import Person

if __name__ == "__main__":
    dao = PersonMemoryDAO()

    print('-'*90)

    people = [Person('23.914.881-6', 'Juan Sosa', 37),
              Person('24.914.881-6', 'Luis Prada', 38),
              Person('25.914.881-6', 'Jose Lopez', 39),
              Person('26.914.881-6', 'Pepe Peña', 40),
              Person('27.914.881-6', 'Ana Perez', 41)]
    dao.create(*people)
    for item in dao.retrive():
        print(item)

    print('-'*90)

    dao.update(Person('27.914.881-6', 'Ana Perez', 50))
    for item in dao.retrive():
        print(item)

    print('-'*90)
    
    dao.delete('25.914.881-6', '27.914.881-6')
    for item in dao.retrive():
        print(item)
