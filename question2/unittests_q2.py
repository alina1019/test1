import filecmp
import os
import unittest

from question2 import print_binary_tree, Node


class TestPrintBinaryTree(unittest.TestCase):
    def test_binary_tree_none(self):
        self.assertEqual(print_binary_tree(None, "test.txt"), None)

    def test_binary_tree_one_node(self):
        print_binary_tree(Node(1), "test2.txt")
        with open('test2.txt', 'r') as file:
            binary_tree = file.read()
        self.assertEqual(binary_tree, "- 1\n")
        if os.path.exists("test2.txt"):
            os.remove("test2.txt")

    def test_binary_tree(self):
        root2 = Node(1)
        root2.left = Node(2)
        root2.right = Node(3)
        root2.left.left = Node(4)
        root2.left.right = Node(5)
        root2.right.left = Node(6)
        root2.right.right = Node(7)
        print_binary_tree(root2, "unit_test_verification.txt")
        self.assertEqual(filecmp.cmp("unit_test_verification.txt", "binary_tree.txt"), True)
        if os.path.exists("unit_test_verification.txt"):
            os.remove("unit_test_verification.txt")


if __name__ == '__main__':
    unittest.main()
