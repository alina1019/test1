import unittest

from question3 import get_next_permutation


class GetNextPermutation(unittest.TestCase):
    def test_next_permutation(self):
        self.assertEqual(get_next_permutation([1, 3, 2, 4]), [1, 3, 4, 2])

    def test_next_permutation_one_integer(self):
        self.assertEqual(get_next_permutation([5]), [5])

    def test_next_permutation_same_integers(self):
        self.assertEqual(get_next_permutation([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_next_permutation_last_permutation(self):
        self.assertEqual(get_next_permutation([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_next_permutation_empty_list(self):
        self.assertEqual(get_next_permutation([]), [])

    def test_next_permutation_two_integers(self):
        self.assertEqual(get_next_permutation([0, 0, 1, 1]), [0, 1, 0, 1])

    def test_negative_next_permutation1(self):
        self.assertNotEqual(get_next_permutation([1, 2]), [])

    def test_negative_next_permutation2(self):
        self.assertNotEqual(get_next_permutation([]), [1, 2, 4, 3])

    def test_next_permutation_all(self):
        l1 = [1, 2, 3]
        all_permutations = [
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        for i in all_permutations:
            self.assertEqual(get_next_permutation(l1), i)


if __name__ == '__main__':
    unittest.main()
