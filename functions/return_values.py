# Demonstrating return statements

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def get_user_stats(name, age):
    """Returns a formatted string."""
    return f"User {name} is {age} years old."

def get_min_max(numbers):
    """Returns multiple values (tuple)."""
    return min(numbers), max(numbers)

if __name__ == "__main__":
    result_sum = add_numbers(10, 50)
    print(f"Sum: {result_sum}")
    
    # Returning multiple values
    scores = [10, 5, 99, 23]
    lowest, highest = get_min_max(scores)
    print(f"Lowest score: {lowest}, Highest score: {highest}")