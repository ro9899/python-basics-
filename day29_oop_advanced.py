# Day 29 - OOP Advanced (Inheritance, Polymorphism, Abstraction)

from abc import ABC, abstractmethod   # for abstraction

# --------------------
# Inheritance Example
# --------------------
class Vehicle:
    def init(self, brand):
        self.brand = brand
    
    def move(self):
        return f"{self.brand} vehicle is moving"


class Car(Vehicle):   # Inheriting from Vehicle
    def init(self, brand, model):
        super().init(brand)   # Call parent constructor
        self.model = model
    
    def move(self):   # Method overriding (polymorphism)
        return f"{self.brand} {self.model} is driving on the road"


class Boat(Vehicle):
    def move(self):
        return f"{self.brand} boat is sailing in the water"


car = Car("Tesla", "Model X")
boat = Boat("Yamaha")

print(car.move())
print(boat.move())


# --------------------
# Polymorphism Example
# --------------------
def show_movement(vehicle_obj):
    print(vehicle_obj.move())

show_movement(car)   # Tesla Model X is driving on the road
show_movement(boat)  # Yamaha boat is sailing in the water


# --------------------
# Abstraction Example
# --------------------
class Animal(ABC):   # Abstract Base Class
    @abstractmethod
    def sound(self):
        pass  # abstract method must be implemented by child classes


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()
print("Dog sound:", dog.sound())
print("Cat sound:", cat.sound())


# --------------------
# Multiple Inheritance
# --------------------
class Flyer:
    def fly(self):
        return "Flying in the sky"


class Swimmer:
    def swim(self):
        return "Swimming in the water"


class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack Quack!"


duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())









