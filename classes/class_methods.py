# Instance methods and self parameter

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def calculate_area(self):
        """Calculates area using instance variable radius."""
        return self.pi * (self.radius ** 2)

    def calculate_circumference(self):
        """Calculates circumference."""
        return 2 * self.pi * self.radius

    def resize(self, new_radius):
        """Modifies the object state."""
        self.radius = new_radius
        print(f"Radius changed to {self.radius}")

if __name__ == "__main__":
    c = Circle(5)
    print(f"Area: {c.calculate_area():.2f}")
    
    c.resize(10)
    print(f"New Area: {c.calculate_area():.2f}")