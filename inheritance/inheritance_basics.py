# Basic Inheritance: Parent and Child classes

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Child Class
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

if __name__ == "__main__":
    dog = Dog("Buddy")
    dog.eat()   # Inherited method
    dog.bark()  # Child method
    
    cat = Cat("Whiskers")
    cat.sleep() # Inherited method
    cat.meow()  # Child method