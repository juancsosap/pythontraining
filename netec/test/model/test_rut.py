import unittest

from model import Rut


class TestRut(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rut(self):
        # Success
        rut = Rut('23914881-4')
        self.assertEqual(rut.rut, '23.914.881-4')

        # Failed
        with self.assertRaises(ValueError):
            Rut('23914881-7')


module_name = 'TestRut'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
