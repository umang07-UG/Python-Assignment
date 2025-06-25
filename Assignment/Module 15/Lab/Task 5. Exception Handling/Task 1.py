# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter an operator (+, -, *, /): ")

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b == 0:
            print("You cannot divide by zero!")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator! Please use +, -, *, or /.")
        
except:
    print("Please enter valid numbers.")