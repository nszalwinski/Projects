__author__ = 'Nathan'

"""
Count Vowels
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

string = raw_input("Enter a string, and I'll count the vowels. ")
vowels = 'aeiou'
count = 0

for c in string:
    if c in vowels:
        count += 1

print count