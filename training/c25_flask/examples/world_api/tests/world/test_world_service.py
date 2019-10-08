import unittest

import app


class TestWorldService(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.app.test_client(self)

    def tearDown(self):
        pass

    def test_getworld(self):
        # Success Request
        # JSON
        response = self.app.get('/api/world', headers={'Accept': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 201)
        # XML
        response = self.app.get('/api/world', headers={'Accept': 'application/xml'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 346)
        self.assertTrue(b'xmlns' in response.data)
        # Other
        response = self.app.get('/api/world', headers={'Accept': 'text/plain'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 201)


module_name = 'tests.TestWorldService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
    unittest.main()
else:
    print('Importing {} class'.format(module_name))
