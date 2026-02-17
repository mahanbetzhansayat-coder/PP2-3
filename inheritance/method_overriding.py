# Method Overriding: Changing parent behavior in child

class Shape:
    def area(self):
        print("Area not defined for generic shape")
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # Overriding the area method
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    # Overriding the area method
    def area(self):
        return 3.14 * (self.radius ** 2)

if __name__ == "__main__":
    generic = Shape()
    generic.area()
    
    rect = Rectangle(10, 5)
    print(f"Rectangle Area: {rect.area()}")
    
    circ = Circle(7)
    print(f"Circle Area: {circ.area()}")