#Write a Python program to add elements to a list using insert() and append().

fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)

# append()
fruits.append('orange')
print("After append('orange'):", fruits)

# insert()
fruits.insert(1, 'mango')  # Inserts at index 1
print("After insert(1, 'mango'):", fruits)