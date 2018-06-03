'''
Find the maximum sum of all subarrays of a given array of integers
'''


def kadane_algorithm(A):
    current_max = A[0]
    global_max = A[0]

    for i in range(1, len(A)):
        current_max = max(A[i], current_max + A[i])
        global_max = max(global_max, current_max)

    return global_max

import itertools
def find_maximum_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

print('Kadane for array: {}'.format(kadane_algorithm([-2, 3, 2, -1])))
print('Kadane for all negative: {}'.format(kadane_algorithm([-2, -3, -2, -1])))
print('Kadane for all positive: {}'.format(kadane_algorithm([2, 3, 2, 1])))

print('MSS for array: {}'.format(find_maximum_subarray([-2, 3, 2, -1])))
print('MSS for all negative: {}'.format(find_maximum_subarray([-2, -3, -2, -1])))
print('MSS for all positive: {}'.format(find_maximum_subarray([2, 3, 2, 1])))
