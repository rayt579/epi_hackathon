'''
Write a program that takes two lists, assumed to be sorted, and returns their merge.
The only field you can change is your next field
'''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge_sorted_lists(A, B):
    merge = Node('Sentinel')
    merge_ptr = merge
    while A and B:
        if A.data < B.data:
            merge_ptr.next = A
            A = A.next
        else:
            merge_ptr.next = B
            B = B.next

        merge_ptr = merge_ptr.next

    merge_ptr.next = A or B

    return merge.next

L1 = Node(1)
L1.next = Node(5)
L2 = Node(2)
L2.next = Node(6)
merged = merge_sorted_lists(L1, L2)
print('Merged lists')
while merged:
    print(merged.data)
    merged = merged.next
