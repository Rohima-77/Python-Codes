 Ekta paragraph e prottek word koto bar ase, ta count koro.

Solve:

from collections import Counter

text = input("Enter a paragraph: ")
words = text.lower().split()
freq = Counter(words)

print(freq)
