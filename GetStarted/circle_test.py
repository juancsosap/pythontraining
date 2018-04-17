import unittest
from GetStarted.circle import Circle
from math import pi


class TestCircle(unittest.TestCase):

    def testArea(self):
        self.assertAlmostEqual(Circle(10).getArea(), pi * 100)
        self.assertAlmostEqual(Circle(1).getArea(), pi)
        self.assertAlmostEqual(Circle(0).getArea(), 0)

    def testValues(self):
        self.assertRaises(ValueError, Circle, -1)

    def testTypes(self):
        self.assertRaises(TypeError, Circle, 1 + 1j)
        self.assertRaises(TypeError, Circle, True)
        self.assertRaises(TypeError, Circle, '3')
