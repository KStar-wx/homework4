import unittest
from func import add, minus, multiply, divide
import circle_packing
from circle_packing import circle
from circle_packing import *
import numpy as np


class test_func(unittest.TestCase):

    def test_add(self):
        """Test method add(a, b).\n"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b).\n"""
        self.assertEqual(1, minus(3, 2))
        self.assertNotEqual(1, minus(3, 1))

    def test_multiply(self):
        """Test method multiply(a, b).\n"""
        self.assertEqual(6, multiply(3, 2))
        self.assertNotEqual(1, multiply(3, 1))

    def test_divide(self):
        """Test method divide(a, b).\n"""
        self.assertEqual(1.5, divide(3, 2))
        self.assertNotEqual(1, divide(3, 1))

    def setUp(self):
        self.c1=circle(1,0,0)
        self.c2=circle(1,1,0)
        self.c3=circle(0.5,0,0)
        self.c4=circle(0,-0.9,0.9)
        self.c_list=[]
        self.c_list.append(self.c2)
        self.c_list.append(self.c3)
        
    def test_distance(self):
        """Test method distance(c1,c2).\n"""
        distance_func=self.c1.distance(self.c2)
        distance_real=np.linalg.norm([self.c1.x-self.c2.x,self.c1.y-self.c2.y])      
        self.assertEqual(distance_real, distance_func)

    def test_whether_cross(self):
        """Test method whether_cross.\n"""
        self.assertEqual(self.c4.whether_cross(self.c_list),1)
        
    def test_MaxR(self):
        """Test method MaxR.\n"""
        self.assertNotEqual(MaxR(self.c4,self.c_list), 1)

    def test_Find_m_Circuit(self):
        """Test method Find_m_Circuit.\n"""
        m = 100
        c_list = Find_m_Circuit(m)
        RR = 0
        for c in c_list:
            RR += c.radius**2
        self.assertGreaterEqual(RR,1)
    


if __name__ == '__main__':

    unittest.main(verbosity=2)
