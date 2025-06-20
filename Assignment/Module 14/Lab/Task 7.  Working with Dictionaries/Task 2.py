#Write a Python program to merge two lists into one dictionary using a loop.

keys = ["name", "age", "city"]
values = ["ug", 20, "Gir"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Merged dictionary:", my_dict)