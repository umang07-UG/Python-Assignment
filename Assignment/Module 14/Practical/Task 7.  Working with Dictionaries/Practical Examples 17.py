#17) Write a Python program to convert two lists into one dictionary using a for loop.


keys = ["id", "name", "subject"]
values = [101, "divyesh", "Maths"]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)