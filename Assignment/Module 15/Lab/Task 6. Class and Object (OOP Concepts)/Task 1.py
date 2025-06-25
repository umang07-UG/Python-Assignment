# Write a Python program to create a class and access its properties using an object


class Person:
    def fun1(self, name, age):
        self.name = name  
        self.age = age    

obj = Person()
obj.fun1("ug", 20)


print("Name:", obj.name)
print("Age:", obj.age)