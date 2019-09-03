# python3 -m unittest <file_name>.py

import unittest as ut
import calc as mod

class Test(ut.TestCase):
    # Test methods must start with the word 'test'
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
        self.assertEqual(val1,  0.0, 'null add')
        self.assertEqual(val2,  6.1, 'positive add')
        self.assertEqual(val3,  1.6, 'different add')
        self.assertEqual(val4, -8.0, 'negative add')

if __name__ == "__main__":
    ut.main()