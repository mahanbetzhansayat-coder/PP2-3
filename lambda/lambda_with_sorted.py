# Using lambda as a key for sorted()

# Example 1: Sort list of tuples by the second element (Age)
students = [
    ("Alice", 25),
    ("Bob", 20),
    ("Charlie", 30),
    ("David", 22)
]

# Sort by age (index 1)
sorted_by_age = sorted(students, key=lambda x: x[1])

# Example 2: Sort strings by length
fruits = ["apple", "banana", "kiwi", "cherry", "blueberry"]
sorted_by_len = sorted(fruits, key=lambda s: len(s))

# Example 3: Sort by last letter
sorted_by_last_char = sorted(fruits, key=lambda s: s[-1])

if __name__ == "__main__":
    print("Sorted by age:", sorted_by_age)
    print("Sorted by length:", sorted_by_len)
    print("Sorted by last letter:", sorted_by_last_char)