# Basic lambda syntax: lambda arguments: expression

# Regular function
def square_func(x):
    return x ** 2

# Equivalent Lambda function
square_lambda = lambda x: x ** 2

# Lambda with multiple arguments
multiply = lambda a, b: a * b

if __name__ == "__main__":
    print(f"Square of 5 (func): {square_func(5)}")
    print(f"Square of 5 (lambda): {square_lambda(5)}")
    
    print(f"10 * 20 = {multiply(10, 20)}")
    
    # Immediately invoked lambda
    print((lambda x: x + 10)(5))  # Prints 15