__author__ = 'Nathan'

"""
Count Words in a String
Counts the number of individual words in a string.
For added complexity read these strings in from a text file
and generate a summary.
"""

from collections import defaultdict
import string

text = raw_input("Enter a string, and I'll print out a word count. ").lower()
copy = text.translate(string.maketrans("",""), string.punctuation)

wordcount = defaultdict(int)

words = copy.split()

for word in words:
    wordcount[word] += 1

print wordcount.items()