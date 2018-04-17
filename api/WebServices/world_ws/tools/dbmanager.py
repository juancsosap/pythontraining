# -*- coding:utf-8 -*-


class DBManager:

    def getconnection(self):
        return None

    def connect(self):
        self.conn = self.getconnection()
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn.open:
            self.conn.close()

    def read(self, sql, *args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def readmany(self, sql, *args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def write(self, sql, *args):
        return self.cursor.execute(sql, args)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()


module_name = 'tools.DBManager'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
