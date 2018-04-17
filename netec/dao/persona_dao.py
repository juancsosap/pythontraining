from dao import DAO
from model import Persona, Rut


class PersonaDAO(DAO):
    def __init__(self):
        DAO.__init__(self, password='roottoor', db='register')

    def create(self, obj):
        sql = '''INSERT INTO persona (nombre, apellido, rut)
                 VALUES (%s, %s, %s)'''
        self.cursor.execute(sql, (obj.nombre, obj.apellido, obj.rut))
        self.conn.commit()
        return self.retrive(obj)

    def retrive(self, obj):
        sql = 'SELECT * FROM persona WHERE idpersona=%s'
        self.cursor.execute(sql, (obj.id,))
        self.conn.commit()
        result = self.cursor.fetchone()
        return self.topersona(result)

    def retrive_all(self):
        sql = 'SELECT * FROM persona'
        self.cursor.execute(sql)
        self.conn.commit()
        results = self.cursor.fetchall()
        return [self.topersona(result) for result in results]

    def update(self, obj):
        sql = '''UPDATE persona
                 SET nombre=%s, apellido=%s, rut=%s
                 WHERE idpersona=%s'''
        self.cursor.execute(sql, (obj.nombre, obj.apellido, obj.rut, obj.id))
        self.conn.commit()
        return self.retrive(obj)

    def delete(self, obj):
        sql = '''DELETE FROM persona
                 WHERE idpersona=%s'''
        self.cursor.execute(sql, (obj.id,))
        self.conn.commit()
        return self.retrive(obj)

    @staticmethod
    def topersona(result):
        if result:
            return Persona(nombre=result[2], apellido=result[3], rut=Rut(result[1]), id=result[0])
        else:
            return Persona()
