#! Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects
# It is a peradiam to structure the code to solve real world problems like create own structures ,showing the real world relationship.

# Class is a blueprint of a instance that how the instance behave .
# Instance  is an object that’s built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. 

# ! Inheritance : - it means taking the properties from the parent class.
# ?(parent, Base,super) -> (child,Derived,subclass)
# !types of inheritance available in OOPS :
# ? Single Inheritance

class A:
    pass

class B(A):
    pass


# ? Multilevel Inheritance
class Grandfather:
    pass

class Father(Grandfather):
    pass

class Son(Father):
    pass

# !in this ,the son class can directly access both class property.

# ? Multiple Inheritance
class A:
    pass

class B:
    pass

class C(B,A):
    pass
# ! now here both class A and B are different from each other ,now c can access both ,here comes the mro concepts like if the C wants to search a property in parent class so in which class it will looking first.then the order of inheriting class is play a crutial role.
 
# ? Hierarchical Inheritance
class A :
    pass

class B(A):
    pass

class C(A):
    pass

# !Here C and B both are diffrent from each other .
# ? Hybrid Inheritance 
# !combination of any two other inheritance called HybridInheritance
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

# !Herarchical + multiple = Hybrid


# !---------------------------------------------------------------------------------------------
# ?Create a class hierarchy with a parent class Vehicle, a child class Car, and a mixin class ElectricMixin. The Vehicle class should have an instance method drive, the Car class should override this method, and the ElectricMixin should add an additional method charge. Additionally, use a special method in the Car class to represent the car as a string, and include a class method to change the car's type, and a static method to calculate the total price of the car based on its price and tax rate.

class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    type = "Disel"
    
    def __init__(self, name, model) -> None:
        self.name = name 
        self.model = model
    
        

    @classmethod
    def change_type(cls, new_type):
        cls.type = new_type

    def drive(self):
        pass
    
    # special method/dunder method/magic method
    def __str__(self) -> str:
        return f"{self.name} and model {self.model}"
    
    @staticmethod
    def Calculate_Price(price, trate):
        return price + (price * trate)
        

class ElectricMixin(Car):
    
    def charge(self):
        pass

# !Polymorphism :-Polymorphism in programming refers to the ability of different objects to respond to the same method or function call in a way specific to their types. This allows for a single interface to control access to a general class of actions. It is a core concept of object-oriented programming that enhances flexibility and reusability of code.

# ?Types of Polymorphism :
"""
1.Compile Time:
    Methode overloading
    Operator overloading
2.Run Time:
    methode overriding
"""
# Method overriding
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Example usage
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Methode and operator overloading
class Student:
    def __init__(self, *args) -> None:
        self.marks = args

    def __add__(self,othe):
        return sum(self.marks) + sum(othe.marks)

std1 = Student(10,10,50,12,54)
std2 = Student(10,10,50)# we can acuhive overloading but it is not by default supported
print(std1 + std2) #operator overloading


# ! MRO
# ?MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance. In Python,

# !Old Style Class :
"""In Python 2.x, if you define a class without explicitly inheriting from the built-in object class, it's considered an "old-style" class."""
# Old-style class definition (Python 2.x)
class OldStyleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Example usage
old_instance = OldStyleClass("Alice")
print(old_instance.greet())  # Output: Hello, Alice!

# !New Class style :while in new class we can explicitly inherit a object class
class NewStyleClass(object):
    def __init__(self, name) -> None:
        self.name = name

    def greet(self):
        return f"Hello ,{self.name}"
    
old_instance = OldStyleClass("Alice")
print(old_instance.greet())
# !but after python 3.x all the classes are by default inherit from object class, New-style classes use the C3 linearization algorithm for method resolution order, which is more predictable and powerful compared to the old-style depth-first left-to-right order.

class A:
    def greet(self):
        print("Hello Good Morning By A")
        return super().greet()
    
class A_1(A):
    def greet(self):
        print("Hello Good Morning By A_1")
        return super().greet()

    
class B:
    def greet(self):
        print( "Hello Good AfterNoon By B")
        return "None"
class C(A_1, B):
    def greet(self):
        return super().greet()
    
# super(C,self).greet() this is the actual syntax for super but we use directly it
    

obj = C()
print(C.__mro__) #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# (<class '__main__.C'>, <class '__main__.A_1'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(obj.greet())

# !Diamon Problem
class Delta:
    pass

class A(Delta):
    pass

class B(A):
    pass

class A_1(Delta):
    pass

class C(A_1):
    pass

class D(B, C):
    pass

obj = D()
print(D.mro())
# it follows the depth first search untill it reach at the last point it doesn't go back 
# if the the parent of parent is same for both classes then it attach it at the end of both class searched.

