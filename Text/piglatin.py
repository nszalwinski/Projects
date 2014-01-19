__author__ = 'Nathan'

"""
Pig Latin
Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant
sound is transposed to the end of the word and an ay is affixed
(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
"""

string = raw_input("Enter a word, and I'll say it back in Pig Latin. ")
vowels = "aeiou"

if string[0] in vowels:
    print(string + "way")
else:
    print(string[1:] + string[0] + "ay")