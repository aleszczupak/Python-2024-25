import unittest
from sparsematrices import *

class TestSparseMatrices(unittest.TestCase):

    def setUp(self):
        self.s1 = {(1, 2): 2, (3, 2): 3, (3, 3): 4}
        self.s2 = {}
        self.s3 = {(1, 1): -1, (3, 3): 3}

    def test_add_sparse_matrix(self):
        self.assertEqual(add_sparse_matrix(self.s1, self.s2),
                         {(1, 2): 2, (3, 2): 3, (3, 3): 4})
        self.assertEqual(add_sparse_matrix(self.s1, self.s3),
                         {(1, 2): 2, (3, 2): 3, (3, 3): 7, (1, 1): -1})

    def test_sub_sparse_matrix(self):
        self.assertEqual(sub_sparse_matrix(self.s2, self.s1),
                         {(1, 2): -2, (3, 2): -3, (3, 3): -4})
        self.assertEqual(sub_sparse_matrix(self.s3, self.s2), self.s3)
        self.assertEqual(sub_sparse_matrix(self.s1, self.s1), {})
        
    def test_mul_sparse_matrix(self):
        self.assertEqual(mul_sparse_matrix(self.s3, self.s1),
                         {(1, 2): -2, (3, 2): 9, (3, 3): 12})
        self.assertEqual(mul_sparse_matrix(self.s1, self.s1),
                         {(3, 2): 12, (3, 3): 16})

    def test_is_diagonal(self):
        self.assertFalse(is_diagonal(self.s1))
        self.assertTrue(is_diagonal(self.s2))
        self.assertTrue(is_diagonal(self.s3))
        
    def test_is_empty(self):
        self.assertTrue(is_empty(self.s2))
        self.assertFalse(is_empty(self.s3))

    def test_new_sparse_matrix(self):
        self.assertEqual(new_sparse_matrix({(1, 2): 0, (22, 17): 5}),
                         {(22, 17): 5})

    def tearDown(self):
        del self.s1, self.s2, self.s3

if __name__ == '__main__':
    unittest.main()
