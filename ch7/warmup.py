'''
Implement a basic list API - search, insert, delete - for singly linked lists
'''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# O(n) time
def search_list(L, key):
    """Move the L to current pointer"""
    while L and L.data != key:
        L = L.next
    return L

# O(1) insert
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

# O(1) delete
def delete_after(node):
    node.next = node.next.next
