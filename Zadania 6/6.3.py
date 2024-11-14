import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 2, 8, 8)
        self.r2 = Rectangle(6, 7, -1, -2)
        self.r3 = Rectangle(-1, -2, 6, 7)
        self.r4 = Rectangle(1, 8, 8, 2)
        self.r5 = Rectangle(6, 7, -1, -2)
        with self.assertRaises(ValueError):
            self.err = Rectangle(1, 2, 1, 2)

    def test_str(self):
        self.assertEqual(self.r1.__str__(), '[(1, 2), (8, 8)]')
        self.assertEqual(self.r4.__str__(), '[(1, 2), (8, 8)]')

    def test_repr(self):
        self.assertEqual(self.r1.__repr__(), 'Rectangle(1, 2, 8, 8)')
        self.assertEqual(self.r5.__repr__(), 'Rectangle(-1, -2, 6, 7)')

    def test_eq(self):
        self.assertTrue(self.r1 == self.r1)
        self.assertTrue(self.r2 == self.r3)
        self.assertFalse(self.r2 == self.r1)
        self.assertTrue(self.r1 == self.r4)

    def test_ne(self):
        self.assertFalse(self.r1 != self.r1)
        self.assertFalse(self.r2 != self.r3)
        self.assertTrue(self.r2 != self.r1)
        self.assertFalse(self.r3 != self.r5)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(4.5, 5))
        self.assertEqual(self.r2.center(), Point(2.5, 2.5))
        self.assertEqual(self.r4.center(), Point(4.5, 5))

    def test_area(self):
        self.assertEqual(self.r1.area(), 42)
        self.assertEqual(self.r2.area(), 63)
        self.assertEqual(self.r5.area(), 63)

    def test_move(self):
        self.r1.move(1, 1)
        self.r2.move(-2, -3)
        self.r4.move(2, 2)
        self.assertEqual(self.r1, Rectangle(2, 3, 9, 9))
        self.assertEqual(self.r2, Rectangle(4, 4, -3, -5))
        self.assertEqual(self.r4, Rectangle(3, 4, 10, 10))

    def test_new_move(self):
        self.assertEqual(self.r1.new_move(1, 1), Rectangle(2, 3, 9, 9))
        self.assertEqual(self.r1, Rectangle(1, 2, 8, 8))

    def tearDown(self):
        del self.r1, self.r2, self.r3, self.r4, self.r5

if __name__=='__main__':
    unittest.main()
