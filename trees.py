from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def height(root):
    if root is None:
        return 0

    l = height(root.left)
    r = height(root.right)

    return 1 + max(l, r)


def isIdentical(x, y):
    if x is None and y is None:
        return True

    return x and y and x.val == y.val and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)


def level_order_iterative(root):
    if root is None:
        return -1

    q = deque()
    q.append(root)
    while (len(q) > 0):
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


def printGivenLevel(root, i):
    if root is None:
        return

    if i == 1:
        print(root.val)
    elif i > 1:
        printGivenLevel(root.left, i - 1)
        printGivenLevel(root.right, i - 1)


def spiral_order(root):
    pass

def specific_order_traversal(root):
    pass


def left_view(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        i = 0
        n = len(q)
        while i < n:
            curr = q.popleft()
            i = i + 1
            if i == 1:
                print(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

def top_view(root):
    pass

def bottom_view(root):
    pass

def print_cousin():
    pass










if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    print(findRightNode(root1,4))
