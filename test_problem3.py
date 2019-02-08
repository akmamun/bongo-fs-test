import unittest

from problem3 import Node, lca


class LCATest(unittest.TestCase):

    def lca_test(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)


        lca(1, 5)
        lca(1, 3)
        lca(4, 3)


if __name__ == '__main__':
    unittest.main()
