# python3 -m unittest <file_name>.py

import unittest as ut
import calc as mod

def setUpModule():
    print('Set Up Module Test')

class AddTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Add Set Up Class Test')

    @classmethod
    def tearDownClass(cls):
        print('\nAdd Tear Down Class Test')

    def setUp(self):
        print('\nAdd Set Up Test')
        self.obj = mod.Calc()               # Arrange

    def tearDown(self):
        print('Add Tear Down Test')
    
    def test_add_null(self):
        print('Add Executing Test')
        val = self.obj.add(0.0, 0.0)        # Act
        self.assertAlmostEqual(val, 0.0)    # Assert

    def test_add_positive(self):
        print('Add Executing Test')
        val = self.obj.add(5.5, 4.3)        # Act
        self.assertAlmostEqual(val, 9.8)    # Assert

    def test_add_negative(self):
        print('Add Executing Test')
        val = self.obj.add(-5.5, -4.3)      # Act
        self.assertAlmostEqual(val, -9.8)   # Assert

class SubTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Sub Set Up Class Test')

    @classmethod
    def tearDownClass(cls):
        print('\nSub Tear Down Class Test')

    def setUp(self):
        print('\nSub Set Up Test')
        self.obj = mod.Calc()               # Arrange

    def tearDown(self):
        print('Sub Tear Down Test')
    
    def test_sub_null(self):
        print('Sub Executing Test')
        val = self.obj.sub(0.0, 0.0)        # Act
        self.assertAlmostEqual(val, 0.0)    # Assert

    def test_sub_positive(self):
        print('Sub Executing Test')
        val = self.obj.sub(5.5, 4.3)        # Act
        self.assertAlmostEqual(val, 1.2)    # Assert

    def test_sub_negative(self):
        print('Sub Executing Test')
        val = self.obj.sub(-5.5, -4.3)      # Act
        self.assertAlmostEqual(val, -1.2)   # Assert

if __name__ == "__main__":
    ut.main()