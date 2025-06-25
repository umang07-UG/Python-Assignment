# Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python.

# Single Inheritance

class Parent:
    def parent_method(self):
        print("Parent method")

class Child(Parent):  # Single inheritance
    def child_method(self):
        print("Child method")

obj = Child()
obj.parent_method()  
obj.child_method()


#Multilevel Inheritance

class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")

class Parent(Grandparent):  
    def parent_method(self):
        print("Parent method")

class Child(Parent):  
    def child_method(self):
        print("Child method")

obj = Child()
obj.grandparent_method()  
obj.parent_method()       
obj.child_method()


#Multiple Inheritance

class Father:
    def father_method(self):
        print("Father's method")

class Mother:
    def mother_method(self):
        print("Mother's method")

class Child(Father, Mother):  # Multiple parents
    def child_method(self):
        print("Child's method")

obj = Child()
obj.father_method()  
obj.mother_method()  
obj.child_method()


# Hierarchical Inheritance

class Parent:
    def parent_method(self):
        print("Parent method")

class Child1(Parent):
    def child1_method(self):
        print("Child1 method")

class Child2(Parent):
    def child2_method(self):
        print("Child2 method")

obj1 = Child1()
obj2 = Child2()
obj1.parent_method()  
obj2.parent_method()


# Hybrid Inheritance


class Grandparent:
    def family_name(self):
        print("Smith")

class Parent1(Grandparent):
    def parent1_method(self):
        print("Parent1 method")

class Parent2(Grandparent):
    def parent2_method(self):
        print("Parent2 method")

class Child(Parent1, Parent2):  # Hybrid (hierarchical + multiple)
    def child_method(self):
        print("Child method")

obj = Child()
obj.family_name()    
obj.parent1_method() 
obj.parent2_method() 
obj.child_method()  