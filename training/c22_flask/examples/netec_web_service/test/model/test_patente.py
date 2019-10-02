import unittest

from model import Patente


class TestPatente(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_patente(self):
        # Success
        patente = Patente('HJZJ11')
        self.assertEqual(patente.patente, 'HJZJ11')

        # Failed
        with self.assertRaises(ValueError):
            Patente('AJZJ11')


module_name = 'TestPatente'
if __name__ == '__main__':
    print('Executing {}'.format(module_name))
else:
    print('Importing {}'.format(module_name))
