'''
Write a program that takes as input a set of sorted sequences
and computes the union of these sequences as a sorted sequence.
'''
import heapq

def merge_sorted_arrays_pythonic(arrays):
    return list(heapq.merge(*arrays))

# O(n + k) space, O(n log k) time, where k is the number of arrays
def merge_sorted_arrays(arrays):
    min_heap = []
    results = []

    # Build min_heap
    list_its = [iter(sl) for sl in arrays]
    for i, it in enumerate(list_its):
        val = next(it, None)
        if val is not None:
            heapq.heappush(min_heap, (val, i))

    # Fill results
    while len(min_heap) > 0:
        val, it_index = heapq.heappop(min_heap)
        results.append(val)
        next_val = next(list_its[it_index], None)
        if next_val is not None:
            heapq.heappush(min_heap, (next_val, it_index))

    return results


a = [3, 5, 7]
b = [0, 6]
c = [0, 6, 28]

sortedlists = [a, b, c]
print(merge_sorted_arrays_pythonic(sortedlists))
print('The results of the minheap merge')
print(merge_sorted_arrays(sortedlists))


