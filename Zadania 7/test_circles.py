import unittest
from points import Point
from circles import Circle
import math

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(3, 2, 1)
        self.c2 = Circle(3.5, 2, 0.5)
        self.c3 = Circle(2.5, 2, 2)
        self.c4 = Circle(4, -2, 2)
        with self.assertRaises(ValueError):
            self.err = Circle(1, 1, -1)

    def test_repr(self):
        self.assertEqual(repr(self.c2), 'Circle(3.5, 2, 0.5)')

    def test_eq(self):
        self.assertTrue(self.c3 == self.c3)
        self.assertFalse(self.c2 == self.c4)

    def test_ne(self):
        self.assertTrue(self.c3 != self.c4)
        self.assertFalse(self.c1 != self.c1)

    def test_area(self):
        self.assertEqual(self.c1.area(), math.pi)
        self.assertEqual(self.c2.area(), math.pi / 4)
        self.assertEqual(self.c3.area(), math.pi * 4)

    def test_move(self):
        self.c4.move(2, -1)
        self.assertEqual(self.c4, Circle(6, -3, 2))

    def test_new_move(self):
        self.assertEqual(self.c4.new_move(2, -1), Circle(6, -3, 2))
        self.assertEqual(self.c4, Circle(4, -2, 2))

    def test_cover(self):
        self.assertEqual(self.c2.cover(self.c1), self.c1)
        self.assertEqual(self.c1.cover(self.c2), self.c1)
        self.assertEqual(self.c1.cover(self.c3), self.c3)
        self.assertEqual(self.c3.cover(self.c2), self.c3)
        self.assertEqual(self.c3.cover(self.c4).p.x, 3.25)
        self.assertEqual(self.c3.cover(self.c4).p.y, 0.0)
        self.assertAlmostEqual(self.c3.cover(self.c4).rad, 4.136, places=3)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
