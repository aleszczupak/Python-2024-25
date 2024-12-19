import unittest
from double_node import Node
from double_list import DoubleList

class TestDoubleList(unittest.TestCase):

    def setUp(self):
        self.dl1 = DoubleList() # 4, 2, 7, 5, 10, 5, 6
        self.dl1.insert_head(Node(10))
        self.dl1.insert_head(Node(5))
        self.dl1.insert_head(Node(7))
        self.dl1.insert_head(Node(2))
        self.dl1.insert_head(Node(4))
        self.dl1.insert_tail(Node(5))
        self.dl1.insert_tail(Node(6))
        self.dl2 = DoubleList() # pusta

    def test_is_empty(self):
        self.assertFalse(self.dl1.is_empty(), False)
        self.assertTrue(self.dl2.is_empty(), True)

    def test_count(self):
        self.assertEqual(self.dl1.count(), 7)

    def test_next(self):
        self.assertEqual(list(self.dl1), [4, 2, 7, 5, 10, 5, 6])

    def test_insert_head(self):
        self.dl1.insert_head(Node(22))
        self.assertEqual(list(self.dl1), [22, 4, 2, 7, 5, 10, 5, 6])

    def test_insert_tail(self):
        self.dl1.insert_tail(Node(33))
        self.assertEqual(list(self.dl1), [4, 2, 7, 5, 10, 5, 6, 33])

    def test_remove_head(self):
        self.dl1.remove_head()
        self.assertEqual(list(self.dl1), [2, 7, 5, 10, 5, 6])
        with self.assertRaises(ValueError):
            self.dl2.remove_head()

    def test_remove_tail(self):
        self.dl1.remove_tail()
        self.assertEqual(list(self.dl1), [4, 2, 7, 5, 10, 5])
        with self.assertRaises(ValueError):
            self.dl2.remove_tail()

    def test_reversed(self):
        self.assertEqual(list(reversed(self.dl1)), [6, 5, 10, 5, 7, 2, 4])

    def test_find_min(self):
        self.assertEqual(self.dl1.find_min(), Node(2))

    def test_find_max(self):
        self.assertEqual(self.dl1.find_max(), Node(10))

    def test_clear(self):
        self.dl1.clear()
        self.assertEqual(self.dl1.count(), 0)
        with self.assertRaises(ValueError):
            self.dl2.clear()

    def test_remove_index(self):
        with self.assertRaises(ValueError):
            self.dl1.remove_index(7)
        self.dl1.remove_index(2)
        self.assertEqual(list(self.dl1), [4, 2, 5, 10, 5, 6])                         

    def test_remove(self):
        self.dl1.remove(5)
        self.assertEqual(list(self.dl1), [4, 2, 7, 10, 5, 6])
        self.assertEqual(self.dl1.count(), 6)
        with self.assertRaises(ValueError):
            self.dl1.remove(444)
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
