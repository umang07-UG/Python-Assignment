# Control Statements



# 1) Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    if fruit == 'banana':
        break  
    print(fruit)

#-------------------------------------------------

# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.

fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    if fruit == 'banana':
        break  
    print(fruit)