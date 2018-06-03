'''
Write a program which takes letter text and magazine text,
and determines if it is possible to write the letter using the magazine.

The anonymous letter can be written using the magazine if for each
character in the letter, the number of times it appears is no more than the number of times it
appears in the magazine
'''
import collections

# O(n + m) time complexity, O(n) space where n is unique char in letter_text

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_char_frequencies = collections.Counter(letter_text)

    for c in magazine_text:
        if c in letter_char_frequencies:
            letter_char_frequencies[c] -= 1
            if letter_char_frequencies[c] == 0:
                del letter_char_frequencies[c]
            if not letter_char_frequencies:
                return True
    return False

def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not (collections.Counter(letter_text) - collections.Counter(magazine_text))

good_letter = 'abca'
magazine = 'fgccaabd'
bad_letter = 'aabca'

print('Good letter: {}'.format(is_letter_constructible_from_magazine(good_letter, magazine)))
print('Bad letter: {}'.format(is_letter_constructible_from_magazine(bad_letter, magazine)))

good_letter = 'abca'
magazine = 'fgccaabd'
bad_letter = 'aabca'

print('Good letter: {}'.format(is_letter_constructible_from_magazine_pythonic(good_letter, magazine)))
print('Bad letter: {}'.format(is_letter_constructible_from_magazine_pythonic(bad_letter, magazine)))
