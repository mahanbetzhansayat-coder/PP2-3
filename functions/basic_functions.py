# Demonstrating basic function definition and calling

def greet_user():
    """Simple function that prints a greeting."""
    print("Hello! Welcome to Python functions practice.")

def describe_weather(weather_type):
    """Function accepting one argument."""
    print(f"The weather is {weather_type} today.")

def calculate_area(width, height):
    """Calculates area and prints it."""
    area = width * height
    print(f"Area of {width}x{height} is: {area}")

# Calling the functions
if __name__ == "__main__":
    greet_user()
    describe_weather("sunny")
    describe_weather("rainy")
    calculate_area(5, 10)