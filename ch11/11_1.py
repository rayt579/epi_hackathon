'''
Write a method that takes a sorted array and a key and returns the
first instance of the key in the array.
'''

# Modified binary search, O(log n) time worst case
def search_first_of_k(sorted_array, key):
    index = len(sorted_array) - 1
    lo, hi = 0, len(sorted_array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_array[mid] < key:
            lo = mid + 1
        elif sorted_array[mid] > key:
            hi = mid - 1
        else:
            index = mid
            hi = mid - 1
    return index


a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print('Found -14 at index: {}'.format(search_first_of_k(a, -14)))
print('Found 108 at index: {}'.format(search_first_of_k(a, 108)))
print('Found 285 at index: {}'.format(search_first_of_k(a, 285)))
