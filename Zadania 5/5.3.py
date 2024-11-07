import unittest
import polys

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [1, 2, 0, -3, 5, 0, -7] # W(x) = 1 + 2x - 3x^3 + 5x^4 - 7x^6
        self.p2 = [2, 0, -3] # W(x) = 2 - 3x^2
        self.p3 = [0, 5, 0, -7] # W(x) = 5x - 7x^3
        self.p4 = [5, 0, 0, -7] # W(x) = 5 - 7x^3
        self.p5 = [0, 0, 0] # W(x) = 0
        self.p6 = [2, 1, 0] # W(x) = 2 + x

    def test_add_poly(self):
        self.assertEqual(polys.add_poly(self.p1, self.p2),
                         [3, 2, -3, -3, 5, 0, -7])
        self.assertEqual(polys.add_poly(self.p3, self.p4),
                         [5, 5, 0, -14])
        self.assertEqual(polys.add_poly(self.p3, self.p6),
                         [2, 6, 0, -7])

    def test_sub_poly(self):
        self.assertEqual(polys.sub_poly(self.p3, self.p1),
                         [-1, 3, 0, -4, -5, 0, 7])
        self.assertEqual(polys.sub_poly(self.p6, self.p5),
                         [2, 1])

    def test_mul_poly(self):
        self.assertEqual(polys.mul_poly(self.p1, self.p2),
                         [2, 4, -3, -12, 10, 9, -29, 0, 21])
        self.assertEqual(polys.mul_poly(self.p1, self.p4),
                         [5, 10, 0, -22, 11, 0, -14, -35, 0, 49])
        self.assertEqual(polys.mul_poly(self.p2, self.p6),
                         [4, 2, -6, -3])
        self.assertEqual(polys.mul_poly(self.p1, self.p6),
                         [2, 5, 2, -6, 7, 5, -14, -7])

    def test_is_zero(self):
        self.assertFalse(polys.is_zero(self.p3))
        self.assertTrue(polys.is_zero([0, 0, 0, 0]))                 

    def test_eq_poly(self):
        self.assertTrue(polys.eq_poly(self.p1, self.p1))
        self.assertFalse(polys.eq_poly(self.p1, self.p2))
        self.assertTrue(polys.eq_poly(self.p6, [2, 1]))

    def test_eval_poly(self):
        self.assertEqual(polys.eval_poly(self.p1, -2), -347)
        self.assertEqual(polys.eval_poly(self.p2, -2), -10)
        self.assertEqual(polys.eval_poly(self.p3, 6), -1482)

    def test_pow_poly(self):
        self.assertEqual(polys.pow_poly(self.p2, 4),
                         [16, 0, -96, 0, 216, 0, -216, 0, 81])
        self.assertEqual(polys.pow_poly(self.p4, 3),
                         [125, 0, 0, -525, 0, 0, 735, 0, 0, -343])
        
    def test_diff_poly(self):
        self.assertEqual(polys.diff_poly(self.p1), [2, 0, -9, 20, 0, -42])
        self.assertEqual(polys.diff_poly(self.p4), [0, 0, -21])
        self.assertEqual(polys.diff_poly(self.p6), [1])

    def test_combine_poly(self):
        self.assertEqual(polys.combine_poly(self.p1, self.p2),
        [-387, 0, 3654, 0, -14202, 0, 29241, 0, -33615, 0, 20412, 0, -5103])
        self.assertEqual(polys.combine_poly(self.p2, self.p3),
                         [2, 0, -75, 0, 210, 0, -147])

    def test_cut_zeros(self):
        self.assertEqual(polys.cut_zeros([2, 3, 0, 0, 1, 0, 0, 0]),
                         [2, 3, 0, 0, 1])

    def tearDown(self):
        del self.p1, self.p2, self.p3, self.p4, self.p5, self.p6

if __name__ == '__main__':
    unittest.main(verbosity=2)
