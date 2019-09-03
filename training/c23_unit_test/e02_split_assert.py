# python3 -m unittest <file_name>.py

import unittest as ut
import calc as mod

class Test(ut.TestCase):
    def test_add_null(self):
        print('\nExecuting Test')
        obj = mod.Calc()                    # Arrange
        val = obj.add(0.0, 0.0)             # Act
        self.assertAlmostEqual(val, 0.0)    # Assert

    def test_add_positive(self):
        print('\nExecuting Test')
        obj = mod.Calc()                    # Arrange
        val = obj.add(5.5, 4.3)             # Act
        self.assertAlmostEqual(val, 9.8)    # Assert

    def test_add_negative(self):
        print('\nExecuting Test')
        obj = mod.Calc()                    # Arrange
        val = obj.add(-5.5, -4.3)           # Act
        self.assertAlmostEqual(val, -9.8)   # Assert

if __name__ == "__main__":
    ut.main()