# Day 28 - Object-Oriented Programming (OOP) Basics

# --------------------
# Class and Object
# --------------------
class Car:
    # Constructor (init) initializes object properties
    def init(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Method
    def start_engine(self):
        return f"{self.brand} {self.model} ({self.year}) engine started!"
    
    def car_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}"


# --------------------
# Creating Objects
# --------------------
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)

print(car1.car_info())
print(car1.start_engine())

print(car2.car_info())
print(car2.start_engine())


# --------------------
# Class with Default Values
# --------------------
class Dog:
    def init(self, name, breed="Mixed"):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"


dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max")  # breed defaults to "Mixed"

print(dog1.bark(), "-", dog1.breed)
print(dog2.bark(), "-", dog2.breed)


# --------------------
# Encapsulation Example
# --------------------
class BankAccount:
    def init(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private variable (name mangling)

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New Balance: {self.__balance}"
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New Balance: {self.__balance}"
        else:
            return "Insufficient Balance"
    
    def get_balance(self):
        return self.__balance


acc = BankAccount("Alice", 1000)
print(acc.deposit(500))
print(acc.withdraw(300))
print("Balance:", acc.get_balance())

# Trying to access private variable directly will fail
# print(acc.__balance)  # AttributeError













