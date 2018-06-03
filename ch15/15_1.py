'''
Towers of Hanoi

Write a program which prints a sequence of operations that transfers n rings
from one peg to another.
'''

# T(N) = 2 T(N - 1) + 1, O(2^n) complexity
def towers_of_hanoi(n_rings):
    def recursive_towers(n_rings, source, target, temp):
        if n_rings == 1:
            print('Moving ring from {} to {}'.format(source, target))
            return
        recursive_towers(n_rings - 1, source, temp, target)
        print('Moving ring from {} to {}'.format(source, target))
        recursive_towers(n_rings - 1, temp, target, source)

    towers = ['X', 'Y', 'Z']
    recursive_towers(n_rings, towers[0], towers[1], towers[2])

towers_of_hanoi(10)
