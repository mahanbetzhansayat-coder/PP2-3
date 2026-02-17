# Basic class definition and creating objects

class Dog:
    """A simple empty class representing a dog."""
    pass

class Car:
    """A simple class with a fixed attribute."""
    category = "Vehicle"

if __name__ == "__main__":
    # Creating objects (instances)
    dog1 = Dog()
    dog2 = Dog()
    
    # Manually setting attributes (not recommended practice, but possible)
    dog1.name = "Buddy"
    dog2.name = "Rex"
    
    print(f"Dog 1: {dog1.name}")
    print(f"Dog 2: {dog2.name}")
    
    my_car = Car()
    print(f"My car is a {my_car.category}")