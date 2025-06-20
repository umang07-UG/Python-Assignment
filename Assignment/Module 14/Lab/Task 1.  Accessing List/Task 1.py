# Write a Python program to create a list of multiple data type elements.


mixed_list = [42, "hello", 3.14, True, None, "Python", 99]


print("Mixed Data Type List:", mixed_list)

# Optional: Print each element with its data type
for item in mixed_list:
    print(f"Value: {item}  →  Type: {type(item)}")