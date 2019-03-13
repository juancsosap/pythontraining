from dao import DAO
from model import Vehiculo, Patente


class VehiculoDAO(DAO):
    def __init__(self):
        DAO.__init__(self, password='roottoor', db='register')

    def create(self, obj):
        sql = '''INSERT INTO vehiculo (patente, marca, modelo, color)
                 VALUES (%s, %s, %s, %s)'''
        self.cursor.execute(sql, (obj.patente, obj.marca, obj.modelo, obj.color))
        self.conn.commit()
        return self.retrive(obj)

    def retrive(self, obj):
        sql = 'SELECT * FROM vehiculo WHERE idvehiculo=%s'
        self.cursor.execute(sql, (obj.id,))
        self.conn.commit()
        result = self.cursor.fetchone()
        return self.topersona(result)

    def retrive_all(self):
        sql = 'SELECT * FROM vehiculo'
        self.cursor.execute(sql)
        self.conn.commit()
        results = self.cursor.fetchall()
        return [self.tovehiculo(result) for result in results]

    def update(self, obj):
        sql = '''UPDATE vehiculo
                 SET patente=%s, marca=%s, modelo=%s, color=%s
                 WHERE idvehiculo=%s'''
        self.cursor.execute(sql, (obj.patente, obj.marca, obj.modelo, obj.color, obj.id))
        self.conn.commit()
        return self.retrive(obj)

    def delete(self, obj):
        sql = '''DELETE vehiculo
                 WHERE idvehiculo=%s'''
        self.cursor.execute(sql, (obj.id,))
        self.conn.commit()
        return self.retrive(obj)

    @staticmethod
    def tovehiculo(result):
        if result is None:
            return Vehiculo()
        else:
            return Vehiculo(patente=Patente(result[1]), marca=result[2], modelo=result[3],
                            color=result[4], id=result[0])
