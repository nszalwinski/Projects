__author__ = 'Nathan'

"""
Count Words in a String
Counts the number of individual words in a string.
For added complexity read these strings in from a text file
and generate a summary.
"""

from collections import defaultdict
import string
import operator

text = raw_input("Enter a string, and I'll print out a word count. ").lower()
copy = text.translate(string.maketrans("",""), string.punctuation)

counts = defaultdict(int)

words = copy.split()
total = 0

for word in words:
    counts[word] += 1
    total += 1

sortcount = sorted(counts.iteritems(), key = operator.itemgetter(1), reverse=True)

print "Most used words:"
for (word, count) in sortcount[:5]:
    print(word, count)

print "Total words: " + str(total)