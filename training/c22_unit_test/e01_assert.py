# python3 -m unittest <file_name>.py

import unittest as ut
import calc as mod

class Test(ut.TestCase):
    def test_add(self):
        print('\nExecuting Test')
        # Arrange
        obj = mod.Calc()

        # Act
        val1 = obj.add( 0.0,  0.0)
        val2 = obj.add( 3.2,  2.9)
        val3 = obj.add(-3.6,  5.2)
        val4 = obj.add(-5.7, -2.3)
        
        # Assert
        self.assertEqual(val1,  0.0)
        self.assertEqual(val2,  6.1)
        self.assertEqual(val3,  1.6)
        self.assertEqual(val4, -8.0)
