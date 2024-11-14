import unittest
from points import Point
from triangles import Triangle
#from itertools import permutations
import math

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t1 = Triangle(1, 2, 3, 4, 3, 1)
        self.t2 = Triangle(-2, -1, -1, 1, 2, -1)
        self.t3 = Triangle(3, 4, 1, 2, 3, 1)
        self.t4 = Triangle(-1, 1, 2, -1, -2, -1)
        with self.assertRaises(ValueError):
            self.err = Triangle(4, 2, 6, 1, 2, 3)

    def test_str(self):
        self.assertEqual(self.t1.__str__(), '[(1, 2), (3, 4), (3, 1)]')

    def test_repr(self):
        self.assertEqual(self.t2.__repr__(), 'Triangle(-2, -1, -1, 1, 2, -1)')

    def test_eq(self):
        self.assertTrue(self.t1 == self.t1)
        self.assertTrue(self.t1 == self.t3)
        self.assertTrue(self.t2 == self.t4)
        self.assertFalse(self.t1 == self.t2)
        self.assertFalse(self.t3 == self.t2)

    def test_ne(self):
        self.assertFalse(self.t2 != self.t2)
        self.assertFalse(self.t3 != self.t1)
        self.assertTrue(self.t3 != self.t4)

    def test_center(self):
        self.assertAlmostEqual(self.t1.center(), Point(7/3, 7/3), places=5)
        self.assertAlmostEqual(self.t2.center(), Point(-1/3, -1/3), places=5)

    def test_area(self):
        self.assertAlmostEqual(self.t1.area(), 3.0, places=1)
        self.assertAlmostEqual(self.t3.area(), 3.0, places=1)
        self.assertAlmostEqual(self.t4.area(), 4.0, places=1)

    def test_move(self):
        self.t1.move(1, 1)
        self.t4.move(-2, -3)
        self.assertEqual(self.t1, Triangle(2, 3, 4, 5, 4, 2))
        self.assertEqual(self.t4, Triangle(-3, -2, 0, -4, -4, -4))

    def test_new_move(self):
        self.assertEqual(self.t1.new_move(1, 1), Triangle(2, 3, 4, 5, 4, 2))
        self.assertEqual(self.t1, Triangle(1, 2, 3, 4, 3, 1))

    def tearDown(self):
        del self.t1, self.t2, self.t3, self.t4

if __name__=='__main__':
    unittest.main()
