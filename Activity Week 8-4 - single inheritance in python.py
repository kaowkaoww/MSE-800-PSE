#Activity W8-4: single inheritance in python
"""
Write a Python program using single inheritance.
Create two classes: Animal (parent class) and Dog (child class).
Add a simple method in each class to demonstrate how single inheritance works.
After writing the code, briefly explain how it works.
Finally, share your code and explanation here.
"""
 
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Creating instances and demonstrating inheritance
my_dog = Dog("Buddy", "Golden Retriever")

# Using methods from parent class (Animal)
my_dog.eat()      # Inherited method
my_dog.sleep()    # Inherited method

# Using methods from child class (Dog)
my_dog.bark()     # Dog-specific method
my_dog.fetch()    # Dog-specific method

# Accessing attributes
print(f"\nMy dog's name is {my_dog.name} and breed is {my_dog.breed}.")

# Second child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def meow(self):
        print(f"{self.name} says: Meow!")
    
    def scratch(self):
        print(f"{self.name} is scratching the furniture.")

# Demonstrating hierarchical inheritance
print("=== Dog Instance ===")
my_dog = Dog("Buddy", "Golden Puddle")
my_dog.eat()      # Inherited from Animal
my_dog.sleep()    # Inherited from Animal
my_dog.bark()     # Dog-specific method
my_dog.fetch()    # Dog-specific method

print("\n=== Cat Instance ===")
my_cat = Cat("Lala", "White")
my_cat.eat()      # Inherited from Animal
my_cat.sleep()    # Inherited from Animal
my_cat.meow()     # Cat-specific method
my_cat.scratch()  # Cat-specific method

print(f"\nDog info: {my_dog.name} is a {my_dog.breed}")
print(f"Cat info: {my_cat.name} is {my_cat.color}")