import unittest
from datetime import date
from person import Person, InvalidTimeError


class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('')

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.user = Person(name='NUser', surname='SUser')

    def tearDown(self):
        pass

    def test_name(self):

        # Test Initial Value
        self.assertAlmostEqual(self.user.name, 'NUser')

        # Test Valid String Value asignation
        self.user.name = 'NRoot'
        self.assertAlmostEqual(self.user.name, 'NRoot')

        # Test Valid String Value asignation with extra spaces
        self.user.name = '   Name   User    '
        self.assertAlmostEqual(self.user.name, 'Name User')

        # Test inValid String Value asignation (too short)
        with self.assertRaises(ValueError):
            self.user.name = 'N'

        # Test inValid String Value asignation with all spaces (too short)
        with self.assertRaises(ValueError):
            self.user.name = '      '

        # Test inValid String Value asignation with extra spaces (too short)
        with self.assertRaises(ValueError):
            self.user.name = '   N   '

        # Test inValid non-String Value asignation
        with self.assertRaises(ValueError):
            self.user.name = ['N', 'U', 's', 'e', 'r']

        # Test Default Value
        with self.assertRaises(ValueError):
            self.user = Person(name='', surname='SUser')

    def test_surname(self):

        # Test Initial Value
        self.assertAlmostEqual(self.user.surname, 'SUser')

        # Test Valid String Value asignation
        self.user.surname = 'SRoot'
        self.assertAlmostEqual(self.user.surname, 'SRoot')

        # Test Valid String Value asignation with extra spaces
        self.user.surname = '   Surname   User    '
        self.assertAlmostEqual(self.user.surname, 'Surname User')

        # Test inValid String Value asignation (too short)
        with self.assertRaises(ValueError):
            self.user.surname = 'S'

        # Test inValid String Value asignation with all spaces (too short)
        with self.assertRaises(ValueError):
            self.user.surname = '      '

        # Test inValid String Value asignation with extra spaces (too short)
        with self.assertRaises(ValueError):
            self.user.surname = '   S   '

        # Test inValid non-String Value asignation
        with self.assertRaises(ValueError):
            self.user.surname = ['S', 'U', 's', 'e', 'r']

        # Test Default Value
        with self.assertRaises(ValueError):
            self.user = Person(name='NUser', surname='')

    def test_height(self):

        # Test Default Value
        self.assertAlmostEqual(self.user.height, 1)

        # Test Valid float Value asignation
        self.user.height = 1.7
        self.assertAlmostEqual(self.user.height, 1.7)

        # Test Valid int Value asignation
        self.user.height = 2
        self.assertAlmostEqual(self.user.height, 2)

        with self.assertRaises(ValueError):
            self.user.height = 0

        with self.assertRaises(ValueError):
            self.user.height = 10

        with self.assertRaises(ValueError):
            self.user.height = '1'

    def test_birthday(self):

        # Test Default Value
        self.assertAlmostEqual(self.user.birthday, date.today())

        # Test Valid date Value asignation
        self.user.birthday = date(2000, 2, 1)
        self.assertAlmostEqual(self.user.birthday, date(2000, 2, 1))

        # Test Valid String Value asignation (%d-%m-%Y)
        self.user.birthday = '01-02-2000'
        self.assertAlmostEqual(self.user.birthday, date(2000, 2, 1))

        # Test Valid String Value asignation (%d/%m/%Y)
        self.user.birthday = '01/02/2000'
        self.assertAlmostEqual(self.user.birthday, date(2000, 2, 1))

        with self.assertRaises(InvalidTimeError):
            self.user.birthday = '01/02/00'

        with self.assertRaises(InvalidTimeError):
            self.user.birthday = '30/02/2000'

        with self.assertRaises(InvalidTimeError):
            self.user.birthday = '2000/02/01'

        with self.assertRaises(ValueError):
            self.user.birthday = 2000

    def test_isalive(self):

        # Test Default Value
        self.assertAlmostEqual(self.user.isalive, True)

        # Test Valid bool Value asignation
        self.user.isalive = False
        self.assertAlmostEqual(self.user.isalive, False)

        with self.assertRaises(ValueError):
            self.user.isalive = 0


if __name__ == '__main__':
    unittest.main()
