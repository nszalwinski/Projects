__author__ = 'Nathan'

"""
Check if Palindrome
Checks if the string entered by the user is a palindrome.
That is, that it reads the same forwards as backwards like 'racecar'
"""

string = raw_input("Enter a string, and I'll tell you if it's a palindrome. ").lower()

if string[::-1] == string:
    print "Your string is a palindrome."

else:
    print "Your string is not a palindrome."