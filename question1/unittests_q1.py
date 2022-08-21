import unittest

from question1 import sort_function


class TestSortAlgorithm(unittest.TestCase):
    def test_sort_positive_numbers(self):
        self.assertEqual(sort_function([4, 77, 9, 98, 4, 0, 15]),
                         [0, 4, 4, 9, 15, 77, 98])

    def test_sort_negative_numbers(self):
        self.assertEqual(sort_function([-5, -29, -6, -3, -1, -19, -6]),
                         [-29, -19, -6, -6, -5, -3, -1])

    def test_sort_negative_positive_numbers(self):
        self.assertEqual(sort_function([0, 5, 5, -5, 7, -4, 8, 2, 4, 1, -6]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_sort_same_numbers(self):
        self.assertEqual(sort_function([8, 8, 8, 8, 8]), [8, 8, 8, 8, 8])

    def test_sort_empty_list(self):
        self.assertEqual(sort_function([]), [])


if __name__ == '__main__':
    unittest.main()
