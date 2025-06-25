# Write a Python program to write multiple strings into a file.



lines = [
    "Hello, this is line 1.\n",
    "This is line 2 of the file.\n",
    "Python makes file handling easy!\n"
]

with open("multilines.txt", "w") as file:
    file.writelines(lines)