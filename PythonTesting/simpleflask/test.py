import unittest

import app


class SimpleFlaskTester(unittest.TestCase):

    def setUp(self):
        print('SimpleFlaskTester SetUp Loaded')
        self.app = app.app.test_client(self)
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        print('SimpleFlaskTester TearDown Loaded')

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_home_code(self):
        print('SimpleFlaskTester test_home_code Loaded')
        self.assertEqual(self.app.get('/').status_code, 200)

    def test_home_data(self):
        print('SimpleFlaskTester test_home_data Loaded')
        self.assertEqual(self.app.get('/').data, b'Hello World Home')


if __name__ == '__main__':
    unittest.main()
