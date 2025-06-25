# Write a Python program to open a file in write mode, write some text, and then close it.


file = open("text1.txt", "w")

file.write("Hello, this is a sample text file.\n")
file.write("You are learning Python!\n")
file.close()