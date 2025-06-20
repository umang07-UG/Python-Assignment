#Write a Python program to create a calculator using functions.

def fun1():
    n= int(input("Enter First Number : "))
    n1= int(input("Enter Second Number : "))
    
    print(n+n1)
    
    
def fun2():
    n= int(input("Enter First Number : "))
    n1= int(input("Enter Second Number : "))
    
    print(n-n1)
    
    
    
def fun3():
    n= int(input("Enter First Number : "))
    n1= int(input("Enter Second Number : "))
    
    print(n*n1)
    
    
def fun4():
    n= int(input("Enter First Number : "))
    n1= int(input("Enter Second Number : "))
    
    print(n/n1)
    

menu = """

    Press 1 For Addition
    Press 2 For Subtraction
    Press 3 For Multiplication  
    Press 4 For Division
 """

while True:
    print(menu)
    choise=int(input("Press Key : "))
    
    if choise == 1:
        fun1()
    elif choise == 2:
        fun2()
    elif choise == 3:
        fun3()
    elif choise == 4:
        fun4()
    else:
        print("Press valid key")
        break