'''
Write a program to count the number of bits set to 1 in a positive int
'''

def count_set_bits(x):
    count = 0
    while x:
        count += x & 1
        x = x >> 1
    return count

print('Count set bits {}'.format(count_set_bits(12) == 2))
