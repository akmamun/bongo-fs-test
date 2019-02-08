# Time complexity of this solution  O(n)

class Node(object):
    def __init__(self, value):
        # create a tree
        self.value = value
        self.left = None
        self.right = None


def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.value)

    if root.value == k:
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False


def lca(node1, node2):
    global root

    path1 = []
    path2 = []

    if (not findPath(root, path1, node1) or not findPath(root, path2, node2)):
        return -1


    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

print("6,7 pass return: ", lca(6, 7))
print("3,7 pass return: ", lca(3, 7))
