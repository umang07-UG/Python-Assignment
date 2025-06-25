# Write a Python program to search for a word in a string using re.search().

import re

text = "Hello, welcome to the world of Python programming."
word = "Python"


if re.search(word, text):
    print(f"'{word}' found in the text!")
else:
    print(f"'{word}' NOT found in the text.")
