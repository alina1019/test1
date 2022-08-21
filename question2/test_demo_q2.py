from question2 import Node, print_binary_tree

# Construct the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(2)
root.left.left.left = Node(3)
root.left.left.right = Node(4)
root.left.right.left = Node(5)
root.left.right.right = Node(1)
root.right.left.left = Node(2)
root.right.left.right = Node(3)
root.right.right.left = Node(4)
root.right.right.right = Node(5)

# print the binary tree
print_binary_tree(root, filename="demo_binary_tree_print.txt")



