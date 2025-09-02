# Day 15 - OOP: Inheritance in Python

# Example 1: Simple inheritance
class Animal:
    def init(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Cat inherits from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

d = Dog("Buddy")
c = Cat("Whiskers")

d.speak()
c.speak()

# Example 2: Using super() to call parent constructor
class Vehicle:
    def init(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} vehicle is moving.")

class Car(Vehicle):
    def init(self, brand, model):
        super().init(brand)   # call parent constructor
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

car1 = Car("Tesla", "Model 3")
car1.drive()

# Example 3: Multilevel inheritance
class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(B):
    def method_c(self):
        print("Method C")

obj = C()
obj.method_a()
obj.method_b()
obj.method_c()

# Example 4: Multiple inheritance
class Father:
    def skill(self):
        print("Father: Gardening")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill(self):
        print("Child: Drawing")
        super().skill()   # follows Method Resolution Order (MRO)

ch = Child()
ch.skill()

# Example 5: Checking isinstance and issubclass
print("Is car1 an instance of Car?", isinstance(car1, Car))
print("Is car1 an instance of Vehicle?", isinstance(car1, Vehicle))
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))












