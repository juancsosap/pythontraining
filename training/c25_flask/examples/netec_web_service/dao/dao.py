import pymysql


class DAO:
    def __init__(self, **kwargs):
        self.host = kwargs['host'] if 'host' in kwargs else 'localhost'
        self.port = kwargs['port'] if 'port' in kwargs else 3306
        self.user = kwargs['user'] if 'user' in kwargs else 'root'
        self.password = kwargs['password']
        self.db = kwargs['db']
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port,
                                    db=self.db, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def create(self, obj):
        pass

    def retrive(self, obj):
        pass

    def retrive_all(self):
        pass

    def update(self, obj):
        pass

    def delete(self, obj):
        pass
