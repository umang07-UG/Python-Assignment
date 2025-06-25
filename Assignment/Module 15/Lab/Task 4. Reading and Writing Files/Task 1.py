# Write a Python program to read the contents of a file and print them on the console.


file = open("example.txt", "r")

content = file.read()
print("File Contents:")
print(content)

file.close()