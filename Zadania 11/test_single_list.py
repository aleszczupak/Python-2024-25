import unittest
from single_node import Node
from single_list import SingleList

class TestSingleList(unittest.TestCase):

    def setUp(self):
        self.sl1 = SingleList() # 5, 4, 3, 2, 1, 0
        self.sl1.insert_head(Node(1))
        self.sl1.insert_head(Node(2))
        self.sl1.insert_tail(Node(0))
        self.sl1.insert_head(Node(3))
        self.sl1.insert_head(Node(4))
        self.sl1.insert_head(Node(5))
        self.sl2 = SingleList()
        self.sl2.insert_head(Node(6))
        self.sl2.insert_head(Node(7))
        self.sl2.insert_head(Node(8)) # 8, 7, 6
        self.sl3 = SingleList() # pusta
        self.sl4 = SingleList() # 1, 3, 9, 1, 4, 5
        self.sl4.insert_head(Node(5))
        self.sl4.insert_head(Node(4))
        self.sl4.insert_head(Node(1))
        self.sl4.insert_head(Node(9))
        self.sl4.insert_head(Node(3))
        self.sl4.insert_head(Node(1))

    def test_is_empty(self):
        self.assertFalse(self.sl1.is_empty(), False)
        self.assertTrue(self.sl3.is_empty(), True)

    def test_count(self):
        self.assertEqual(self.sl1.length, 6)
        self.assertEqual(self.sl2.length, 3)
        self.assertEqual(self.sl3.length, 0)

    def test_next(self):
        self.assertEqual(list(self.sl1), [5, 4, 3, 2, 1, 0])

    def test_insert_head(self):
        self.sl1.insert_head(Node(22))
        self.assertEqual(list(self.sl1), [22, 5, 4, 3, 2, 1, 0])

    def test_insert_tail(self):
        self.sl1.insert_tail(Node(33))
        self.assertEqual(list(self.sl1), [5, 4, 3, 2, 1, 0, 33])

    def test_remove_head(self):
        self.sl2.remove_head()
        self.assertEqual(list(self.sl2), [7, 6])
        with self.assertRaises(ValueError):
            self.sl3.remove_head()

    def test_remove_tail(self):
        self.sl2.remove_tail()
        self.assertEqual(list(self.sl2), [8, 7])
        with self.assertRaises(ValueError):
            self.sl3.remove_tail()

    def test_join(self):
        self.sl2.join(self.sl1)
        self.assertEqual(self.sl2.length, 9)
        self.assertEqual(self.sl1.length, 0)
        self.assertEqual(list(self.sl2), [8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_clear(self):
        self.sl2.clear()
        self.assertEqual(self.sl2.count(), 0)
        with self.assertRaises(ValueError):
            self.sl3.clear()

    def test_search(self):
        self.assertEqual(self.sl4.search(16), None)
        self.assertEqual(self.sl4.search(4), Node(4))
        self.assertEqual(self.sl4.search(3), Node(3))

    def test_find_min(self):
        self.assertEqual(self.sl4.find_min(), Node(1))

    def test_find_max(self):
        self.assertEqual(self.sl4.find_max(), Node(9))

    def test_reverse(self):
        self.sl1.reverse()
        self.assertEqual(list(self.sl1), [0, 1, 2, 3, 4, 5])
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
