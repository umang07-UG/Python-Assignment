# Write a Python program to demonstrate handling multiple exceptions.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception as e:
    print("Something went wrong:", e)
