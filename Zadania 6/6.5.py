import unittest
from fracs import Frac
import math

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 2)
        self.f2 = Frac(4, 8)
        self.f3 = Frac(0, 3)
        self.f4 = Frac(1, 4)
        self.f5 = Frac(-5, 1)
        self.f6 = Frac(0, 1)
        self.f7 = Frac(-3, -2)
        self.f8 = Frac(2, -3)
        with self.assertRaises(ZeroDivisionError):
            self.err = Frac(2, 0)

    def test_str(self):
        self.assertEqual(self.f1.__str__(), '1/2')
        self.assertEqual(self.f3.__str__(), '0')
        self.assertEqual(self.f5.__str__(), '-5')
        self.assertEqual(self.f7.__str__(), '3/2')
        self.assertEqual(self.f8.__str__(), '-2/3')

    def test_repr(self):
        self.assertEqual(self.f2.__repr__(), 'Frac(1, 2)')
        self.assertEqual(self.f3.__repr__(), 'Frac(0)')

    def test_eq(self):
        self.assertTrue(self.f1 == self.f1)
        self.assertTrue(self.f1 == self.f2)
        self.assertTrue(self.f3 == self.f6)
        self.assertFalse(self.f1 == self.f4)

    def test_ne(self):
        self.assertFalse(self.f1 != self.f1)
        self.assertFalse(self.f1 != self.f2)
        self.assertFalse(self.f3 != self.f6)
        self.assertTrue(self.f1 != self.f4)

    def test_lt(self):
        self.assertTrue(self.f4 < self.f1)
        self.assertTrue(self.f5 < self.f6)
        self.assertFalse(self.f1 < self.f2)

    def test_le(self):
        self.assertTrue(self.f4 <= self.f1)
        self.assertTrue(self.f1 <= self.f2)
        self.assertFalse(self.f4 <= self.f5)

    def test_gt(self):
        self.assertTrue(self.f1 > self.f4)
        self.assertTrue(self.f6 > self.f5)
        self.assertFalse(self.f1 > self.f2)

    def test_ge(self):
        self.assertTrue(self.f1 >= self.f4)
        self.assertTrue(self.f1 >= self.f2)
        self.assertFalse(self.f5 >= self.f4)

    def test_add(self):
        self.assertEqual(self.f1 + self.f4, Frac(3, 4))
        self.assertEqual(self.f1 + self.f2, Frac(1, 1))
        self.assertEqual(self.f3 + self.f7, self.f7)

    def test_sub(self):
        self.assertEqual(self.f4 - self.f1, Frac(-1, 4))
        self.assertEqual(self.f1 - self.f2, Frac(0, 1))
        self.assertEqual(self.f1 - self.f6, Frac(1, 2))

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Frac(1, 4))
        self.assertEqual(self.f7 * self.f8, Frac(-1, 1))

    def test_truediv(self):
        self.assertEqual(self.f1 / self.f2, Frac(1, 1))
        self.assertEqual(self.f1 / self.f8, Frac(-3, 4))
        self.assertEqual(self.f1 / self.f8, Frac(3, -4))

    def test_floordiv(self):
        self.assertEqual(self.f1 // self.f2, 1.0)
        self.assertEqual(self.f1 // self.f4, 2.0)
        self.assertEqual(self.f2 // self.f8, -1.0)
        with self.assertRaises(ZeroDivisionError):
            self.f1 // self.f3

    def test_mod(self):
        self.assertEqual(self.f1 % self.f2, 0.0)
        self.assertEqual(self.f1 % self.f5, -4.5)
        self.assertAlmostEqual(self.f1 % self.f8, -0.1666, places=2)
        with self.assertRaises(ZeroDivisionError):
            self.f2 % self.f6

    def test_pos(self):
        self.assertEqual(+self.f1, self.f1)
        self.assertEqual(+self.f6, self.f6)

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-1, 2))
        self.assertEqual(-self.f5, Frac(5, 1))

    def test_invert(self):
        self.assertEqual(~self.f2, Frac(8, 4))

    def test_float(self):
        self.assertEqual(self.f1.float(), 1/2)

    def tearDown(self):
        del self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8
        
if __name__=='__main__':
    unittest.main()
