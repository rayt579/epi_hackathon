'''
Write a program that takes as input two sorted arrays,
and returns a new array containing elements that are present in
both arrays. The new array will not have any duplicates.
'''

# O(log (n + m) time, O(1) space
def intersect_two_sorted_arrays(A, B):
    results = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            if i == 0 or A[i] != A[i - 1]:
                results.append(A[i])
            i, j = i + 1, j + 1
    return results

A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
B = [5, 5, 6, 8, 8, 9, 10, 10]

print(intersect_two_sorted_arrays(A,B))
