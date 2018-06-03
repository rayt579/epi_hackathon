'''
Write a program that takes an array A and an index i into  A, and rearranges
the elements such that all elements less than A[i] appear first, followed by elements equal
to the pivot, followed by elements greater than the pivot
'''

# O(N) time, O(1) space.
# Consider invariants! Less will never be greater than equal
def dnf_partition(A, i):
    less, equal, greater = 0, 0, len(A) - 1
    pivot = A[i]
    while equal < greater:
        if A[equal] < pivot:
            A[less], A[equal] = A[equal], A[less]
            less += 1
            equal += 1
        elif A[equal] > pivot:
            A[equal], A[greater] = A[greater], A[equal]
            greater -= 1
        else:
            equal += 1

a = [0, 1, 2, 0, 2, 1, 1]
print('Before applying partition {}'.format(a))
dnf_partition(a, 1)
print('After partition at {}: {}'.format(1, a))
