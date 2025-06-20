#18) Write a Python program to count how many times each character appears in a string

text = "programming"

d = {}

for i in text:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print("Character Frequency:")
for char, count in d.items():
    print(char,":",count)