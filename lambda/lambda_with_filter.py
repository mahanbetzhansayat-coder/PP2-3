# Using lambda with filter() to select items

numbers = [1, -5, 10, -2, 3, 8, -9]

# Example 1: Keep only positive numbers
positives = list(filter(lambda x: x > 0, numbers))

# Example 2: Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Example 3: Filter words longer than 3 letters
words = ["hi", "hello", "yo", "python", "is", "cool"]
long_words = list(filter(lambda w: len(w) > 3, words))

if __name__ == "__main__":
    print(f"Original numbers: {numbers}")
    print(f"Positive numbers: {positives}")
    print(f"Even numbers: {evens}")
    print(f"Long words: {long_words}")