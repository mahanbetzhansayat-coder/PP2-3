# Demonstrating positional and keyword arguments

def make_coffee(coffee_type, size="Medium", sugar=True):
    """
    Function with positional and default arguments.
    :param coffee_type: Required argument
    :param size: Optional, default is Medium
    :param sugar: Optional, default is True
    """
    sugar_txt = "with sugar" if sugar else "no sugar"
    print(f"Preparing a {size} {coffee_type}, {sugar_txt}.")

# Calling with different argument styles
if __name__ == "__main__":
    # Positional arguments
    make_coffee("Latte", "Large", True)
    
    # Using default values
    make_coffee("Cappuccino") 
    
    # Keyword arguments (order doesn't matter)
    make_coffee(sugar=False, coffee_type="Espresso", size="Small")