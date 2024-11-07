import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, -1], [2, 2]), [2, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-2, 4], [2, -4]), [1, 4])
        self.assertEqual(mul_frac([1, 4], [1, -2]), [-1, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([-1, 2], [-1, 2]), [1, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([2, 4], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([-2, 8]), -0.25)
        self.assertEqual(frac2float([0, 2]), 0.0)
        self.assertEqual(frac2float([6, -2]), -3.0)

    def test_minus(self):
        self.assertEqual(minus([1, -2]), [-1, 2])
        self.assertEqual(minus([-1, -5]), [1, 5])

    def test_exeptions(self):
        self.assertRaises(ZeroDivisionError, add_frac, [1, 0], [2, 1])
        self.assertRaises(ZeroDivisionError, add_frac, [1, 5], [2, 0])
        self.assertRaises(ZeroDivisionError, sub_frac, [1, 0], [2, 1])
        self.assertRaises(ZeroDivisionError, sub_frac, [1, 5], [2, 0])
        self.assertRaises(ZeroDivisionError, mul_frac, [1, 0], [2, 1])
        self.assertRaises(ZeroDivisionError, mul_frac, [1, 5], [2, 0])
        self.assertRaises(ZeroDivisionError, div_frac, [1, 0], [2, 1])
        self.assertRaises(ZeroDivisionError, div_frac, [1, 5], [2, 0])
        self.assertRaises(ZeroDivisionError, div_frac, [1, 0], [0, 1])
        self.assertRaises(ZeroDivisionError, is_positive, [1, 0])
        self.assertRaises(ZeroDivisionError, is_zero, [2, 0])
        self.assertRaises(ZeroDivisionError, cmp_frac, [1, 0], [2, 1])
        self.assertRaises(ZeroDivisionError, cmp_frac, [1, 5], [2, 0])        
        self.assertRaises(ZeroDivisionError, frac2float, [1, 0])

    def tearDown(self):
        del self.zero

if __name__ == '__main__':
    unittest.main(verbosity=2)
