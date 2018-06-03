'''
Write a program that takes a set of words and returns groups
of anagrams for those words. Each group must contain at least two words
'''
from collections import defaultdict

# O(n m log(m)), where m is length of a word, n is number of words
def find_anagrams(words):
    groups = defaultdict(list)

    # Build dictionary
    for word in words:
        groups[''.join(sorted(word))].append(word)

    return [groups[anagram] for anagram in groups if len(groups[anagram]) > 1]


words = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'lives', 'levis', 'money']
print(find_anagrams(words))

