# Using the super() function to access properties of the parent class.

class Parent:
    def fun1(self):
        print("Hello from Parent")

class Child(Parent):
    def fun1(self):
        super().fun1()  
        print("Hello from Child")

obj = Child()
obj.fun1()