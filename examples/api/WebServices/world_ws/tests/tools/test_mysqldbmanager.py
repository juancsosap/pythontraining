import unittest

from tools import MySQLDBManager

from pymysql.err import OperationalError, InternalError
from pymysql.err import IntegrityError, ProgrammingError


class TestMySQLDBManager(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation(self):
        # Success Creation
        # All Arguments
        with MySQLDBManager(host='localhost', port=3306, db='world',
                            user='root', password='roottoor', autocommit=True) as dbman:
            self.assertFalse(not dbman)
        # Only not default Arguments
        with MySQLDBManager(db='world', password='roottoor') as dbman:
            self.assertFalse(not dbman)

        # Failed Creation
        # Hostname Argument
        with self.assertRaises(TypeError):
            MySQLDBManager(host=127, password='roottoor', db='world')
        # Port Argument
        with self.assertRaises(TypeError):
            MySQLDBManager(port='3306', password='roottoor', db='world')
        # DB Argument
        with self.assertRaises(TypeError):
            MySQLDBManager(password='roottoor', db=True)
        # User Argument
        with self.assertRaises(TypeError):
            MySQLDBManager(user=True, password='roottoor', db='world')
        # Password Argument
        with self.assertRaises(AttributeError):
            MySQLDBManager(password=True, db='world')

    def test_connection(self):
        # Success Connection
        with MySQLDBManager(password='roottoor', db='world') as dbman:
            self.assertFalse(not dbman)

        # Failed Connection
        # Wrong Host
        with self.assertRaises(OperationalError):
            MySQLDBManager(host='localhos', password='roottoor', db='world')
        # Wrong Port
        with self.assertRaises(OperationalError):
            MySQLDBManager(port=3606, password='roottoor', db='world')
        # Wrong DB
        with self.assertRaises(InternalError):
            MySQLDBManager(password='roottoor', db='wolrd')
        # Wrong User
        with self.assertRaises(OperationalError):
            MySQLDBManager(user='ROOT', password='roottoor', db='world')
        # Wrong Password
        with self.assertRaises(OperationalError):
            MySQLDBManager(password='ROOTTOOR', db='world')

    def test_disconnection(self):
        # Success Disconnection
        # Using With
        with MySQLDBManager(password='roottoor', db='world') as dbman:
            self.assertTrue(dbman.conn.open)
        self.assertFalse(dbman.conn.open)
        # Manual
        dbman = MySQLDBManager(password='roottoor', db='world')
        self.assertTrue(dbman.conn.open)
        dbman.disconnect()
        self.assertFalse(dbman.conn.open)

        # Failed Disconnection
        # Using With
        with MySQLDBManager(password='roottoor', db='world') as dbman:
            self.assertTrue(dbman.conn.open)
            dbman.disconnect()
            self.assertFalse(dbman.conn.open)
        self.assertFalse(dbman.conn.open)
        # Manual doble disconnection
        dbman = MySQLDBManager(password='roottoor', db='world')
        self.assertTrue(dbman.conn.open)
        dbman.disconnect()
        self.assertFalse(dbman.conn.open)
        dbman.disconnect()
        self.assertFalse(dbman.conn.open)

    def test_read(self):
        with MySQLDBManager(password='roottoor', db='world') as dbman:
            # Success Read
            # Without arguments
            name = dbman.read('SELECT name, countrycode FROM city WHERE id=1')
            self.assertEqual(name, ('Kabul', 'AFG'))
            name = dbman.read('SELECT name FROM city WHERE id=1')
            self.assertEqual(name, ('Kabul',))
            name = dbman.read('SELECT name FROM city WHERE id=1')
            self.assertEqual(name, ('Kabul',))
            # With arguments
            name = dbman.read('SELECT name, countrycode FROM city WHERE id=%s', 1)
            self.assertEqual(name, ('Kabul', 'AFG'))
            id = dbman.read('SELECT id, countrycode FROM city WHERE name=%s', 'Kabul')
            self.assertEqual(id, (1, 'AFG'))
            name = dbman.read('SELECT name FROM city WHERE countrycode=%s', 'AFG')
            self.assertEqual(name, ('Kabul',))

            # Failed Read
            # No Info
            name = dbman.read('SELECT name, countrycode FROM city WHERE id=%s', 10_000)
            self.assertEqual(name, None)
            # Bad SQL Arguments
            name = dbman.read('SELECT name, countrycode FROM city WHERE id=%s', 'Kabul')
            self.assertEqual(name, None)
            # Not enough arguments
            with self.assertRaises(TypeError):
                name = dbman.read('SELECT name, countrycode FROM city WHERE id=%s')
            # Bad SQL Syntax
            with self.assertRaises(ProgrammingError):
                name = dbman.read('SELEC name, countrycode FROM city WHERE id=1')

    def test_readmany(self):
        with MySQLDBManager(password='roottoor', db='world') as dbman:
            # Success Read
            # Without arguments
            expected = (('Kabul',), ('Qandahar',), ('Herat',), ('Mazar-e-Sharif',))
            names = dbman.readmany('SELECT name FROM city LIMIT 4')
            self.assertEqual(names, expected)
            # With arguments
            names = dbman.readmany('SELECT name FROM city LIMIT %s', 4)
            self.assertEqual(names, expected)

            # Failed Read
            # No Info
            names = dbman.readmany('SELECT name FROM city LIMIT %s', 0)
            self.assertEqual(names, ())
            # Bad SQL Arguments
            with self.assertRaises(ProgrammingError):
                dbman.readmany('SELECT name FROM city LIMIT %s', 'AFG')
            # Not enough arguments
            with self.assertRaises(TypeError):
                dbman.readmany('SELECT name FROM city LIMIT %s')
            # Bad SQL Syntax
            with self.assertRaises(ProgrammingError):
                dbman.readmany('SELEC name FROM city LIMIT %s', 4)

    def test_write(self):
        with MySQLDBManager(password='roottoor', db='world') as dbman:
            # Success Write
            # Without arguments
            sql = '''INSERT INTO city (id, name, countrycode, population)
                     VALUES (10000, 'Santiago', 'CHL', 10000000)'''
            count = dbman.write(sql)
            self.assertEqual(count, 1)
            sql = '''SELECT population FROM city
                     WHERE id=10000'''
            result = dbman.read(sql)
            self.assertEqual(result, (10_000_000,))
            # With arguments
            sql = '''DELETE FROM city WHERE id=%s'''
            count = dbman.write(sql, 10000)
            self.assertEqual(count, 1)
            sql = 'SELECT * FROM city WHERE id=%s'
            result = dbman.read(sql, 10_000)
            self.assertEqual(result, None)

            # Failed Write
            # No Info
            count = dbman.write('DELETE FROM city WHERE id=%s', 10000)
            self.assertEqual(count, 0)
            # Bad SQL Arguments
            count = dbman.write('DELETE FROM city WHERE id=%s', 'AFG')
            self.assertEqual(count, 0)
            # Not enough arguments
            with self.assertRaises(TypeError):
                dbman.write('DELETE FROM city WHERE id=%s')
            # Bad SQL Syntax
            with self.assertRaises(ProgrammingError):
                dbman.write('DELET FROM city WHERE id=%s', 10000)
            # Bad SQL Syntax - Not Constrain Compliance
            with self.assertRaises(IntegrityError):
                dbman.write('INSERT INTO city (id, name) VALUES (%s, %s)', 10000, 'Santiago')


module_name = 'tests.TestMySQLDBManager'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
    unittest.main()
else:
    print('Importing {} class'.format(module_name))
