import unittest
from points import Point
from triangles import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(1, 1, 3, 3, 3, 1)
        self.t2 = Triangle(4, 2, 5, 4, 6, 1)
        self.t3 = Triangle(2, -2, 4, 1, 5, -1)
        self.t4 = Triangle(3, 3, 1, 1, 3, 1)
        self.t5 = Triangle(6, 1, 5, 4, 2, 4)
        with self.assertRaises(ValueError):
            self.err1 = Triangle(1, 1, 2, 2, 3, 3)
        with self.assertRaises(ValueError):
            self.err2 = Triangle(4, 2, 6, 1, 2, 3)

    def test_str(self):
        self.assertEqual(str(self.t1), '[(1, 1), (3, 3), (3, 1)]')

    def test_repr(self):
        self.assertEqual(repr(self.t2), 'Triangle(4, 2, 5, 4, 6, 1)')

    def test_eq(self):
        self.assertTrue(self.t1 == self.t4)
        self.assertFalse(self.t2 == self.t5)

    def test_ne(self):
        self.assertTrue(self.t1 != self.t2)
        self.assertFalse(self.t1 != self.t4)

    def test_center(self):
        self.assertEqual(self.t1.center(), Point(7/3, 5/3))
        self.assertEqual(self.t4.center(), Point(7/3, 5/3))
        self.assertEqual(self.t3.center(), Point(11/3, -2/3))

    def test_area(self):
        self.assertAlmostEqual(self.t1.area(), 2.00, places=2)
        self.assertAlmostEqual(self.t2.area(), 2.50, places=2)
        self.assertAlmostEqual(self.t3.area(), 3.50, places=2)

    def test_move(self):
        self.t3.move(-4, 1)
        self.t5.move(0, -1)
        self.assertEqual(self.t3, Triangle(-2, -1, 0, 2, 1, 0))
        self.assertEqual(self.t5, Triangle(6, 0, 5, 3, 2, 3))

    def test_new_move(self):
        self.assertEqual(self.t3.new_move(-4, 1), Triangle(-2, -1, 0, 2, 1, 0))
        self.assertEqual(self.t3, Triangle(2, -2, 4, 1, 5, -1))

    def test_make4(self):
        self.assertEqual(self.t2.make4(), (Triangle(4, 2, 9/2, 3, 5, 3/2),
                                           Triangle(9/2, 3, 11/2, 5/2, 5, 3/2),
                                           Triangle(5, 3/2, 11/2, 5/2, 6, 1),
                                           Triangle(9/2, 3, 5, 4, 11/2, 5/2)))
        self.assertEqual(self.t3.make4(), (Triangle(2, -2, 3, -1/2, 7/2, -3/2),
                                           Triangle(3, -1/2, 9/2, 0, 7/2, -3/2),
                                           Triangle(7/2, -3/2, 9/2, 0, 5, -1),
                                           Triangle(3, -1/2, 4, 1, 9/2, 0)))

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
