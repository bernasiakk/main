import unittest
from math import pi

# import the function you want to test
from circles import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)
    
    def test_exceptions(self):
        self.assertRaises(ValueError, circle_area, 0)

        with self.assertRaises(ValueError):
            circle_area(-1)
        
        with self.assertRaises(TypeError):
            circle_area("test")


if __name__ == '__main__':
    unittest.main()