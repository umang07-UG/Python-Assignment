#Write a Python program to remove elements from a list using pop() and remove().


numbers = [10, 20, 30, 40, 50, 30, 60]
print("Original list:", numbers)

# remove()
numbers.remove(30)
print("After remove(30):", numbers)

# pop()
popped = numbers.pop()
print("After pop():", numbers)