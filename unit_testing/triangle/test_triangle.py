import unittest

from triangle import is_triangle

class TestTriangle(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, is_triangle, [1,2,'three'])
        self.assertRaises(Exception, is_triangle, [0,0,0])
        self.assertRaises(Exception, is_triangle, [0,0,-5])
        self.assertRaises(Exception, is_triangle, [6,6,[1,2,3]])

if __name__ == '__main__':
    unittest.main()