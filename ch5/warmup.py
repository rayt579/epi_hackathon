'''
Input is an array of integers, reorder its entries so that the even entries appear first.
'''
# Space complexity is O(1), time O(N)
def even_odd(A):
    odd = len(A) - 1
    even = 0
    while even < odd:
        if A[even] % 2 == 0:
            even += 1
        else:
            A[even], A[odd] = A[odd], A[even]
            odd -= 1
    return A

a = [1,4,5,9,10,14,20,19]
print('Before partition: {}'.format(a))
print('After partition: {}'.format(even_odd(a)))
