import unittest
from single_node import Node
from sorted_list import SortedList

class TestSortedList(unittest.TestCase):

    def setUp(self):
        self.sorl1 = SortedList() # 12, 5, 4, 1
        self.sorl1.insert(Node(5))
        self.sorl1.insert(Node(4))
        self.sorl1.insert(Node(1))
        self.sorl1.insert(Node(12))
        self.sorl2 = SortedList() # 7, 3, 1, 1
        self.sorl2.insert(Node(1))
        self.sorl2.insert(Node(3))
        self.sorl2.insert(Node(7))
        self.sorl2.insert(Node(1))
        self.sorl3 = SortedList() # pusta

    def test_is_empty(self):
        self.assertFalse(self.sorl1.is_empty(), False)
        self.assertTrue(self.sorl3.is_empty(), True)

    def test_count(self):
        self.assertEqual(self.sorl1.length, 4)
        self.assertEqual(self.sorl3.length, 0)

    def test_next(self):
        self.assertEqual(list(self.sorl1), [12, 5, 4, 1])
        self.assertEqual(list(self.sorl2), [7, 3, 1, 1])

    def test_insert(self):
        self.sorl1.insert(Node(7))
        self.sorl1.insert(Node(22))
        self.sorl1.insert(Node(-1))
        self.assertEqual(list(self.sorl1), [22, 12, 7, 5, 4, 1, -1])

    def test_remove(self):
        self.sorl2.remove()
        self.assertEqual(list(self.sorl2), [3, 1, 1])
        with self.assertRaises(ValueError):
            self.sorl3.remove()

    def test_merge(self):
        self.sorl1.merge(self.sorl2)
        self.assertEqual(list(self.sorl1), [12, 7, 5, 4, 3, 1, 1, 1])
        self.assertEqual(self.sorl1.length, 8)
        self.assertEqual(self.sorl2.length, 0)

    def test_clear(self):
        self.sorl1.clear()
        self.assertEqual(self.sorl1.length, 0)
        with self.assertRaises(ValueError):
            self.sorl3.clear()
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
