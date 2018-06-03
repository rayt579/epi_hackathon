'''
Write a program that takes as input the root of a binary tree and checks
whether the tree is height balanced.

Height balanced: Each node in tree has left and right subtree that differ by height of at most 1
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
Brute Force Method
'''
# O(n^2) solution, O(h) space
def is_height_balanced_bruteforce(root):
    if root is None:
        return True
    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False
    return is_height_balanced_bruteforce(root.left) and is_height_balanced_bruteforce(root.right)

# O(n) time, O(h) space
def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1

tree = Node(10)
tree.right = Node(15)
tree.right.right = Node(20)
tree.right.right.right = Node(50)
tree.left = Node(2)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.left.right.right = Node(4)
tree.left.right.right.right = Node(5)

print(is_height_balanced_bruteforce(tree))

balance = Node(10)
balance.right = Node(20)
balance.left = Node(5)
print(is_height_balanced_bruteforce(balance))

'''
Space efficient method where we also calculate the height
'''

from collections import namedtuple

# Postorder traversal, O(n) time, O(h) space
def is_height_balanced(root):
    BalanceWithHeight = namedtuple('BalanceWithHeight', ('is_balanced', 'height',))

    def check_balanced(root):
        if root is None:
            return BalanceWithHeight(True, -1)
        left = check_balanced(root.left)
        right = check_balanced(root.right)
        height = max(left.height, right.height) + 1
        is_balanced = abs(left.height - right.height) <= 1

        if left.is_balanced and right.is_balanced and is_balanced:
            return BalanceWithHeight(True, height)
        else:
            return BalanceWithHeight(False, height)

    return check_balanced(root).is_balanced

tree = Node(10)
tree.right = Node(15)
tree.right.right = Node(20)
tree.right.right.right = Node(50)
tree.left = Node(2)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.left.right.right = Node(4)
tree.left.right.right.right = Node(5)
print(is_height_balanced(tree))


balance = Node(10)
balance.right = Node(20)
balance.left = Node(5)
print(is_height_balanced(balance))
