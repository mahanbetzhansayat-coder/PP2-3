# Demonstrating *args and **kwargs

def sum_all(*args):
    """
    *args allows passing an arbitrary number of positional arguments.
    Inside the function, args is a tuple.
    """
    total = sum(args)
    print(f"Sum of {args} is: {total}")
    return total

def print_profile(**kwargs):
    """
    **kwargs allows passing an arbitrary number of keyword arguments.
    Inside the function, kwargs is a dictionary.
    """
    print("\nUser Profile:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

if __name__ == "__main__":
    # Using *args
    sum_all(1, 2, 3)
    sum_all(10, 20, 30, 40, 50)
    
    # Using **kwargs
    print_profile(name="Alice", age=25, city="New York", role="Developer")
    print_profile(product="Laptop", price=1000, in_stock=True)