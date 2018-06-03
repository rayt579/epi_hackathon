'''
Write a program that takes as input a binary tree and checks if the tree
satisfies the BST property.
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# O(n) time, O(h) space
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.data < min_val or root.data > max_val:
        return False
    return is_bst(root.left, min_val, root.data) and is_bst(root.right, root.data, max_val)

print('Using inorder tree traversal')
good_tree = Node(4)
good_tree.right = Node(10)
good_tree.right.right = Node(14)
good_tree.right.left = Node(8)
print('Good tree: {}'.format(is_bst(good_tree)))

bad_tree = Node(4)
bad_tree.right = Node(10)
bad_tree.right.right = Node(14)
bad_tree.right.left = Node(11)
print('Bad tree: {}'.format(is_bst(bad_tree)))



import collections
# O(n) time, O(h)
def is_bst_using_bfs(root):
    NodeWithMinMax = collections.namedtuple('NodeWithMinMax', ('node', 'min','max',))
    queue = collections.deque([NodeWithMinMax(root, float('-inf'), float('inf'))])
    while queue:
        front = queue.popleft()
        if not front.min <= front.node.data < front.max:
            return False
        if front.node.left:
            queue.append(NodeWithMinMax(front.node.left, front.min, front.node.data))
        if front.node.right:
            queue.append(NodeWithMinMax(front.node.right, front.node.data, front.max))

    return True


print('Using BFS')
good_tree = Node(4)
good_tree.right = Node(10)
good_tree.right.right = Node(14)
good_tree.right.left = Node(8)
print('Good tree: {}'.format(is_bst_using_bfs(good_tree)))

bad_tree = Node(4)
bad_tree.right = Node(10)
bad_tree.right.right = Node(14)
bad_tree.right.left = Node(11)
print('Bad tree: {}'.format(is_bst_using_bfs(bad_tree)))
