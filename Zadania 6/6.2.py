import unittest
import math
from points import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(2, 2)
        self.p2 = Point(1, 0)
        self.p3 = Point(-3, 4)

    def test_str(self):
        self.assertEqual(self.p1.__str__(), '(2, 2)')

    def test_repr(self):
        self.assertEqual(self.p2.__repr__(), 'Point(1, 0)')

    def test_eq(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p2 == self.p3)

    def test_ne(self):
        self.assertFalse(self.p1 != self.p1)
        self.assertTrue(self.p2 != self.p3)

    def test_add(self):
        self.assertEqual(self.p2 + self.p3, Point(-2, 4))

    def test_sub(self):
        self.assertEqual(self.p2 - self.p3, Point(4, -4))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 2)
        self.assertEqual(self.p1 * self.p3, 2)
        self.assertEqual(self.p2 * self.p3, -3)

    def test_cross(self):
        self.assertEqual(Point.cross(self.p1, self.p2), -2)
        self.assertEqual(Point.cross(self.p1, self.p3), 14)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(8))
        self.assertEqual(self.p2.length(), 1)
        self.assertEqual(self.p3.length(), 5)

    def tearDown(self):
        del self.p1, self.p2, self.p3

if __name__=='__main__':
    unittest.main()
