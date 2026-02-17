# Using lambda with map() to transform lists

numbers = [1, 2, 3, 4, 5]

# Example 1: Square every number
squared = list(map(lambda x: x ** 2, numbers))

# Example 2: Convert Celsius to Fahrenheit
celsius = [0, 20, 30, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# Example 3: Capitalize names
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda n: n.capitalize(), names))

if __name__ == "__main__":
    print(f"Original: {numbers}")
    print(f"Squared: {squared}")
    print(f"Temps (F): {fahrenheit}")
    print(f"Names: {capitalized}")