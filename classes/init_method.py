# The __init__ constructor method

class Person:
    def __init__(self, name, age):
        """
        The constructor initializes the object's state.
        :param name: Name of the person
        :param age: Age of the person
        """
        self.name = name
        self.age = age
        print(f"Person {self.name} has been created.")

class Laptop:
    def __init__(self, brand, model, ram=8):
        self.brand = brand
        self.model = model
        self.ram = ram

if __name__ == "__main__":
    p1 = Person("John", 30)
    print(f"Name: {p1.name}, Age: {p1.age}")

    l1 = Laptop("Apple", "MacBook Air")
    l2 = Laptop("Dell", "XPS", ram=16)
    print(f"{l1.brand} {l1.model} has {l1.ram}GB RAM")
    print(f"{l2.brand} {l2.model} has {l2.ram}GB RAM")