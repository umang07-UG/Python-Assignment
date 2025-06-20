#4) Write a Python program to remove elements from a list using pop() and remove().

numbers = [5, 10, 15, 20, 25]

numbers.remove(15)

popped = numbers.pop()

print("Updated numbers list:", numbers)
print("Popped value:", popped)