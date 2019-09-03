# python3 -m unittest <file_name>.py

import unittest as ut
import calc as mod

class Test(ut.TestCase):
    def setUp(self):
        print('\nSet Up Test')
        self.obj = mod.Calc()               # Arrange

    def tearDown(self):
        print('Tear Down Test')
    
    def test_add_null(self):
        print('Executing Test')
        val = self.obj.add(0.0, 0.0)        # Act
        self.assertAlmostEqual(val, 0.0)    # Assert

    def test_add_positive(self):
        print('Executing Test')
        val = self.obj.add(5.5, 4.3)        # Act
        self.assertAlmostEqual(val, 9.8)    # Assert

    def test_add_negative(self):
        print('Executing Test')
        val = self.obj.add(-5.5, -4.3)      # Act
        self.assertAlmostEqual(val, -9.8)   # Assert

if __name__ == "__main__":
    ut.main()