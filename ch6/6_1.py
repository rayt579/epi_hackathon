'''
Implement methods that take a string representing an integer and
return the corresponding integer, and vice versa. Your code should
handle negative integers
'''

# O(n) solution, iterative through each digit in string
def strtoint(text):
    n = len(text)
    num = 0
    is_negative = False

    for letter in text:
        if letter is '-':
            is_negative = True
        else:
            digit = ord(letter) - ord('0')
            num += (digit * 10 ** (n-1))
        n -= 1

    return -num if is_negative else num

# O(n) solution, where we build a string with the digits in reverse order
def inttostr(num):
    text = []
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    while num > 0:
        lsd = num % 10
        digit = chr(ord('0') + lsd)
        text.append(digit)
        num //= 10
    if is_negative:
        text.append('-')

    text.reverse()
    return ''.join(text)



print('Converting -10348691 (string) to: {}'.format(strtoint('-10348691')))
print('Converting -10348691 (int) to: {}'.format(inttostr(-10348691)))


