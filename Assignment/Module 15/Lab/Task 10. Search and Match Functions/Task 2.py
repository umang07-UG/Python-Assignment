# Write a Python program to match a word in a string using re.match().

import re

text = "Python is fun"
word = "Python"


if re.match(word, text):
    print(f"'{word}' matches at the start of the string!")
else:
    print(f"'{word}' does NOT match at the start of the string.")