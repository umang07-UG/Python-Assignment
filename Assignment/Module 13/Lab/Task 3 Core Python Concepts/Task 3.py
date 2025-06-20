#   • Write a Python program to demonstrate the creation of variables and different data types.



# 1)  Practical Example 1: How does the Python code structure work?

# Python executes code sequentially from top to bottom

print("This line executes first")
print("This line executes second")



# 2)  Practical Example 2: How to create variables in Python?

# Integer variable
age = 25
print("Integer variable (age):", age)

# Float variable
temperature = 98.6
print("Float variable (temperature):", temperature)

# String variable
name = "Alice"
print("String variable (name):", name)

# Boolean variable
student = True
print("Boolean variable (student):", student)

# List (mutable collection)
fruits = ["apple", "banana", "cherry"]
print("List variable (fruits):", fruits)

# Tuple (immutable collection)
coordinates = (10.5, 20.3)
print("Tuple variable (coordinates):", coordinates)



# 3)  Practical Example 3: : How to take user input using the input() function.


# Basic input (always returns a string)
name = input("Enter your name: ")
print("Hello,", name)

# Converting input to other types

age=int(input("Enter Age"))
print(age)



# 4)  Practical Example 4: : How to check the type of a variable dynamically using type().

#using type function

a=10
print(type(a))

# Different variables with different types

name = "raj"          # string
age = 20                # integer
price = 19.99           # float
is_student = True       # boolean
fruits = ["apple", "banana"]  # list