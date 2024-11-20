import unittest
from points import Point
from rectangles import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(-1, 1, 2, 3)
        self.r2 = Rectangle(1, 2, 5, 5)
        self.r3 = Rectangle(4, 3, 6, 6)
        self.r4 = Rectangle(6, 1, 8, 2)
        self.r5 = Rectangle(6, 2, 8, 1)
        with self.assertRaises(ValueError):
            self.err = Rectangle(1, 2, 1, 2)

    def test_str(self):
        self.assertEqual(str(self.r1), '[(-1, 1), (2, 3)]')
        self.assertEqual(str(self.r5), '[(6, 1), (8, 2)]')

    def test_repr(self):
        self.assertEqual(repr(self.r1), 'Rectangle(-1, 1, 2, 3)')

    def test_eq(self):
        self.assertTrue(self.r1 == self.r1)
        self.assertFalse(self.r1 == self.r2)
        self.assertTrue(self.r4 == self.r5)

    def test_ne(self):
        self.assertFalse(self.r1 != self.r1)
        self.assertTrue(self.r1 != self.r2)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(0.5, 2))
        self.assertEqual(self.r4.center(), Point(7, 1.5))
        self.assertEqual(self.r5.center(), Point(7, 1.5))

    def test_area(self):
        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r4.area(), 2)

    def test_move(self):
        self.r1.move(-1, 1)
        self.r3.move(2, -3)
        self.assertEqual(self.r1, Rectangle(-2, 2, 1, 4))
        self.assertEqual(self.r3, Rectangle(6, 0, 8, 3))

    def test_new_move(self):
        self.assertEqual(self.r1.new_move(-1, 1), Rectangle(-2, 2, 1, 4))
        self.assertEqual(self.r1, Rectangle(-1, 1, 2, 3))

    def test_intersection(self):
        self.assertEqual(self.r1.intersection(self.r2), Rectangle(1, 2, 2, 3))
        self.assertEqual(self.r3.intersection(self.r2), Rectangle(4, 3, 5, 5))
        with self.assertRaises(ValueError):
            self.r1.intersection(self.r3)
        with self.assertRaises(ValueError):
            self.r4.intersection(self.r2)

    def test_cover(self):
        self.assertEqual(self.r1.cover(self.r2), Rectangle(-1, 1, 5, 5))
        self.assertEqual(self.r2.cover(self.r1), Rectangle(-1, 1, 5, 5))
        self.assertEqual(self.r4.cover(self.r3), Rectangle(4, 1, 8, 6))

    def test_make4(self):
        self.assertEqual(self.r2.make4(), (Rectangle(1, 3.5, 3, 5),
                                           Rectangle(3, 3.5, 5, 5),
                                           Rectangle(1, 2, 3, 3.5),
                                           Rectangle(3, 2, 5, 3.5)))
        self.assertEqual(self.r3.make4(), (Rectangle(4, 4.5, 5, 6),
                                           Rectangle(5, 4.5, 6, 6),
                                           Rectangle(4, 3, 5, 4.5),
                                           Rectangle(5, 3, 6, 4.5)))

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
