class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Trunk:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str


def show_trunks(p, filename):
    if p is None:
        return
    show_trunks(p.prev, filename)
    with open(filename, "a") as f:
        print(p.str, end='', file=f)


def print_binary_tree(root, filename, prev=None, is_left=False):
    if root is None:
        return

    prev_str = '	'
    trunk = Trunk(prev, prev_str)
    print_binary_tree(root.right, filename, trunk, True)

    if prev is None:
        trunk.str = '-'
    elif is_left:
        trunk.str = '.-'
        prev_str = '   |'
    else:
        trunk.str = '`-'
        prev.str = prev_str

    show_trunks(trunk, filename)
    with open(filename, "a") as f:
        print(' ' + str(root.data), file=f)
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    print_binary_tree(root.left, filename, trunk, False)
