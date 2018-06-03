'''
Write a program to check whether the string is palindromic
'''

def is_palindrome(sequence):
    start = 0
    end = len(sequence) - 1
    while start < len(sequence) // 2:
        if sequence[start] != sequence[end]:
            return False
        start += 1
        end -= 1
    return True

print('Is palindrome RACECAR: {}'.format(is_palindrome('RACECAR')))
print('Is palindrome RACECARS: {}'.format(is_palindrome('RACECARS')))
print('Is palindrome CAAC: {}'.format(is_palindrome('CAAC')))
print('Is palindrome CAAD: {}'.format(is_palindrome('CAAD')))
