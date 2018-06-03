'''
Compute the parity of the a very large number of 64-bit words
'''

# Brute force O(N)
def parity_brute_force(x):
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity

# Bit fiddle, use x & (x -1) to remove least set bit O(k), where k is number of set bits in x
# Also, x & ~(x-1) isolates least set bit
def parity_bit_fiddle(x):
    parity = 0
    while x:
        parity ^= 1
        x &= (x - 1)
    return parity

# Aggregrate XOR bits together, O(log N)
def parity_divide_and_conquer(x):
    x ^= (x >> 32)
    x ^= (x >> 16)
    x ^= (x >> 8)
    x ^= (x >> 4)
    x ^= (x >> 2)
    x ^= (x >> 1)

    return x & 1

print('---------------------------------------')
print('Brute force')
print('---------------------------------------')
print('Parity of 10001000 is: {}'.format(parity_brute_force(136)))
print('Parity of 1011 is: {}'.format(parity_brute_force(11)))

print('---------------------------------------')
print('Bit fiddle')
print('---------------------------------------')
print('Parity of 10001000 is: {}'.format(parity_bit_fiddle(136)))
print('Parity of 1011 is: {}'.format(parity_bit_fiddle(11)))

print('---------------------------------------')
print('Divide and conquer')
print('---------------------------------------')
print('Parity of 10001000 is: {}'.format(parity_divide_and_conquer(136)))
print('Parity of 1011 is: {}'.format(parity_divide_and_conquer(11)))

'''
Interesting fact: Consider a lookup table for all 2^16 integers containing parity.
This changes time complexity to be a function of O(N / 16)
'''
