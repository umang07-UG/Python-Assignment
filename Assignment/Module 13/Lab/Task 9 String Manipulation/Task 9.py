# Control Statements



# 1) Write a Python program to demonstrate string slicing


text = "PythonProgramming"


print("Original string:", text)


print("text[:6] =", text[:6]) 


print("text[6:] =", text[6:])  


print("text[0:10] =", text[0:10])  


print("text[::2] =", text[::2])  


print("text[1:10:2] =", text[1:10:2])  


print("text[::-1] =", text[::-1])


#-----------------------------------------------------------------------------

# 1) Write a Python program to demonstrate string slicing



message = "  hello World!  "

# Case methods
print("\nCase Methods:")
print("Upper case:", message.upper())         
print("Lower case:", message.lower())        
print("Title case:", message.title())         
print("Capitalized:", message.capitalize())   

# Cleaning methods
print("\nCleaning Methods:")
print("Stripped:", message.strip())           
print("Left stripped:", message.lstrip())     
print("Right stripped:", message.rstrip())    

# Search methods
print("\nSearch Methods:")
print("Position of 'World':", message.find("World"))  
print("Count of 'l':", message.count("l"))    
print("Starts with 'hello':", message.lstrip().startswith("hello")) 

# Transformation methods
print("\nTransformation Methods:")
print("Replace 'World' with 'Python':", message.replace("World", "Python"))
print("Split into words:", message.strip().split())  
print("Joined with dashes:", "-".join(["hello", "world"]))

# Formatting methods
print("\nFormatting Methods:")
print("Centered string:", message.strip().center(20, "*")) 
print("Zero-padded number:", "42".zfill(5)) 
