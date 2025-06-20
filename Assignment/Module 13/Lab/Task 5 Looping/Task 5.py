# 9)  Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "mango", "orange", "grapes"]
for fruit in fruits:
    print(fruit)
    


# 10) Write a Python program to find the length of each string in List1.

List1 = ["apple", "banana", "mango", "orange", "grapes"]
for item in List1:
    print(item, "length is :", len(item))
    
    
# 11) Write a Python program to find a specific string in the list using a simple for loop and if condition.

fruits = ["apple", "banana", "mango", "orange", "grapes"]
print(fruits)
search_item = input("Enter the fruit name to search: ")

found = False

for fruit in fruits:
    if fruit == search_item:
        print(search_item, "is found in the list.")
        found = True
        break
    
    
# 12) : Print this pattern using nested for loop:


rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
