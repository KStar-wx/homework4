import unittest
from func import add, minus, divide, distance

class test_func(unittest.TestCase):

    def test_add(self):
        """Test method add(a, b).\n"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b).\n"""
        self.assertEqual(1, minus(3, 2))
        self.assertNotEqual(1, minus(3, 1))

    def test_divide(self):
        """Test method divide(a, b).\n"""
        self.assertEqual(1.5, divide(3, 2))
        self.assertNotEqual(1, divide(3, 1))
        
    def test_distance(self):
        """Test method distance(x1, y1, x2, y2).\n"""
        self.assertEqual(2**0.5, distance(1, 1, 2, 2))
        self.assertNotEqual(3, distance(1, 1, 1, 2))
    



if __name__ == '__main__':

    unittest.main(verbosity=2)
