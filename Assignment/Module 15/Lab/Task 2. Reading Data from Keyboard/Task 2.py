# Converting user input into different data types (e.g., int, float, etc.).

# 1. String 
name = input("Enter your name: ")
print("Hello,", name)

# 2. Integer 
try:
    age = int(input("Enter your age (whole number): "))
    print("In 5 years, you'll be:", age + 5)
except ValueError:
    print("Invalid age input!")

# 3. Float Input
try:
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    print("Half your height is:", height / 2)
except ValueError:
    print("Invalid height input!")

# 4. Boolean I
bool_input = input("Do you like Python? (True/False): ").strip().lower()
likes_python = bool_input == "true"
print("Likes Python:", likes_python)


