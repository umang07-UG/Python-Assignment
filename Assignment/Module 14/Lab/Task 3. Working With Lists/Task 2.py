#Write a Python program to sort a list using both sort() and sorted().

numbers = [42, 10, 7, 99, 23]
print("Original list",numbers)

# Using sort() - modifies the original list
numbers.sort()
print("List after sort():", numbers)

# Re-define list to original for using sorted()
numbers = [42, 10, 7, 99, 23]

# Using sorted() - creates a new sorted list
sorted_numbers = sorted(numbers)
print("Original list after sorted():", numbers)
print("New sorted list:", sorted_numbers)