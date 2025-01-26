# # Solving the python programs in OOps concepts .....
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# # creating the object of the class
# obj = Person("Jeet", 24); obj.introduce()

# # Solving the second problem !!
# pi = 3.14159

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#    # Creating the area()
#     def area(self):
#         pi = 3.14159
#         cal = pi * (self.radius ** self.radius)
#         print(f"The area of the circle is {cal}")
    
#     # Creating the circumference()
#     def circumference(self):
#         pi = 3.14159
#         cal = 2 * pi * self.radius
#         print(f"The circumference of the circle is {cal}")

# # Creating the object for the class Circle
# obj = Circle(2); obj.area(); obj.circumference()

# # Solving the third problem
# class Employee:
#     company_name = "TechCorp"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def employee_details(self):
#         print(f"{self.name} works in '{self.company_name}' with the salary {self.salary}")

# # Creating the object
# obj = Employee("Hrithik", 120000); obj.employee_details()

# # Solving the 4th question
# # Here comes the concept of Inheritance
# class Animal:
#     def speak(self):
#         print(f"Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print(f"Dog Barks")

# obj = Dog(); obj.speak()

# # Solving the 5th question Polymorphism

# # Write two classes, Rectangle and Circle, each with a method area() that calculates the area of the shape.
# # Create a function print_area(shape) that takes a shape object and calls its area() method.
# # Demonstrate polymorphism by passing objects of Rectangle and Circle to the print_area function.

# import math

# class Reactangle: # Creating the Rectangle class
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# class Circle: # Creating the Circle class
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)


# def print_shape(shape):
#     print(f"The area of the shape is: {shape.area()}")

# rect = Reactangle(10, 5) # Creating the object for the rectangle class !!

# circ = Circle(8) # Creating the object for the Circle class !!

# print_shape(rect); print_shape(circ)

# Advanced Questions
# Method Overriding:
# Create a base class Vehicle with a method fuel_type() that prints "Vehicle uses fuel."
# Create a derived class ElectricCar that overrides fuel_type() to print "Electric car uses electricity."
# Demonstrate the overriding behavior.

# Static and Class Methods:
# Create a class MathOperations with:
# A static method add(a, b) to add two numbers.
# A class method info() that prints a message about the class.
# Call both methods and demonstrate their usage.

# Operator Overloading:
# Write a class Point with attributes x and y.
# Overload the + operator to add two Point objects by summing their x and y values.

# Multiple Inheritance:
# Create two classes Teacher and Student with respective methods teach() and study().
# Create a class TeachingAssistant that inherits from both and can call both methods.

# Challenge Questions
# Property Decorators:
# Write a class Temperature with:
# A private attribute _celsius.
# A property fahrenheit that converts the Celsius value to Fahrenheit (F = C * 9/5 + 32).
# A setter for fahrenheit that updates the Celsius value when a Fahrenheit value is set.

# Abstract Classes:
# Create an abstract class Shape with an abstract method area().
# Implement concrete classes Square and Triangle that inherit from Shape and provide their implementations for the area() method.


"""Finish tommorow for sure !!"""
# Encapsulation:
# Create a class BankAccount with:
# Private attributes _account_number and _balance.
# Methods deposit(amount) and withdraw(amount) to modify the balance.
# A method get_balance() to view the current balance.
# Demonstrate how to interact with the BankAccount object while maintaining encapsulation.

class BankAccount:
    def __init__(self, __account_number, __balance):
        self.__account_number = __account_number
        self.__balance = __balance

    def deposite_amount(self, amount):
        if amount <= 0:
            print("Amount must be positive to deposite !")
            return
        self.amount = amount
        self.__balance += self.amount
        print(f"Amount {self.amount} successfully deposited !")

    def withdraw_amount(self, amount):
        if amount <= 0:
            print("Amount must be positive for withdrawing !")
            return
        if amount > self.__balance:
            print(f"Insufficient balance in the account: {self.__account_number}")
            return
        self.amount = amount
        self.__balance -= self.amount
        print(f"Amount {self.amount} successfully withdrawed !")
        

    def get_balance(self):
        print(f"In the account number: {self.__account_number}, balance remained: {self.__balance}")

# Creating the object for the above class !!
obj = BankAccount(12400, 12000)
obj.deposite_amount(500)
obj.get_balance()
obj.withdraw_amount(4000)
obj.get_balance()

# Method Overriding:
# Create a base class Vehicle with a method fuel_type() that prints "Vehicle uses fuel."
# Create a derived class ElectricCar that overrides fuel_type() to print "Electric car uses electricity."
# Demonstrate the overriding behavior.

class Vehical:
    def fuel_type(self):
        print("Vehical use fuel !")
class ElectricCar:
    def fuel_type(self):
        print("Electric Car uses electricity")

obj = Vehical(); obj.fuel_type()
obj1 = ElectricCar(); obj.fuel_type()

def show_fuel_type(verical_type):
    verical_type.fuel_type()