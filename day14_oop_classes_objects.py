# Day 14 - Object-Oriented Programming (Classes & Objects)

# Example 1: Creating a simple class
class Person:
    def init(self, name, age):   # constructor method
        self.name = name
        self.age = age

    def greet(self):   # instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.greet()
p2.greet()

# Example 2: Adding methods
class Circle:
    def init(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Circle area:", c.area())
print("Circle circumference:", c.circumference())

# Example 3: Class variables (shared across all objects)
class Student:
    school_name = "ABC School"   # class variable

    def init(self, name):
        self.name = name         # instance variable

s1 = Student("Emma")
s2 = Student("John")

print(s1.name, "-", s1.school_name)
print(s2.name, "-", s2.school_name)

# Example 4: Updating class variable
Student.school_name = "XYZ School"
print(s1.name, "-", s1.school_name)
print(s2.name, "-", s2.school_name)

# Example 5: str method (string representation)
class Book:
    def init(self, title, author):
        self.title = title
        self.author = author

    def str(self):
        return f"{self.title} by {self.author}"

b1 = Book("1984", "George Orwell")
print(b1)














