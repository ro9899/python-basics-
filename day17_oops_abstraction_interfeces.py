# Day 17 - OOP: Abstraction & Interfaces in Python

from abc import ABC, abstractmethod

# --------------------
# Abstraction
# --------------------
# Abstract class: cannot be instantiated directly
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete classes must implement abstract methods
class Rectangle(Shape):
    def init(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# --------------------
# Interfaces
# --------------------
# In Python, interface = abstract class with only abstract methods

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyable):
    def fly(self):
        print("Bird is flying.")

class Airplane(Flyable):
    def fly(self):
        print("Airplane is flying.")

things = [Bird(), Airplane()]
for obj in things:
    obj.fly()

# --------------------
# Example: Payment System Interface
# --------------------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

payment_methods = [CreditCardPayment(), PayPalPayment()]
for method in payment_methods:
    method.pay(100)










