import unittest

import app


class TestCityService(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.app.test_client(self)

    def tearDown(self):
        pass

    def test_getcities(self):
        # Success Request
        response = self.app.get('/api/world').status_code
        self.assertEqual(response, 200)


module_name = 'tests.TestCityService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
    unittest.main()
else:
    print('Importing {} class'.format(module_name))
