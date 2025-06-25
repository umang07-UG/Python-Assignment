# Write Python programs to demonstrate method overloading and method overriding.


# method overloading

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

p = Parent()
p.greet()  

c = Child()
c.greet() 


# method overriding

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       
print(calc.add(2, 3, 4))    
