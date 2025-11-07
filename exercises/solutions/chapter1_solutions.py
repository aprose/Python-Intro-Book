"""
Solutions to Python Basics Exercises - Chapter 1
"""

# Exercise 1: Variables and Arithmetic
print("=" * 50)
print("Exercise 1: Rectangle Area and Perimeter")
print("=" * 50)

# Define variables
length = 10
width = 5

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Print results
print(f"Rectangle dimensions: {length} x {width}")
print(f"Area: {area} square units")
print(f"Perimeter: {perimeter} units")
print()


# Exercise 2: Control Flow
print("=" * 50)
print("Exercise 2: Number Classification")
print("=" * 50)

def classify_number(num):
    """Classify a number as positive/negative/zero and even/odd."""
    # Check if positive, negative, or zero
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")
    
    # Check if even or odd (only for non-zero)
    if num != 0:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

# Test the function
test_numbers = [5, -3, 0, 8, -12]
for num in test_numbers:
    classify_number(num)
    print()


# Exercise 3: Loops
print("=" * 50)
print("Exercise 3: Loops and Iterations")
print("=" * 50)

# Part 1: Print even numbers from 1 to 20
print("Even numbers from 1 to 20:")
even_numbers = []
for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
print()

# Part 2: Sum of numbers from 1 to 100
total_sum = sum(range(1, 101))
print(f"Sum of numbers from 1 to 100: {total_sum}")
print()

# Part 3: Multiplication table
def print_multiplication_table(num, up_to=10):
    """Print multiplication table for a given number."""
    print(f"Multiplication table for {num}:")
    for i in range(1, up_to + 1):
        result = num * i
        print(f"{num} x {i} = {result}")

print_multiplication_table(7)
print()


# Exercise 4: Functions
print("=" * 50)
print("Exercise 4: Useful Functions")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def max_of_three(a, b, c):
    """Find the maximum of three numbers."""
    return max(a, b, c)

# Test the functions
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")
print(f"Factorial of 5: {factorial(5)}")
print(f"Maximum of (10, 25, 18): {max_of_three(10, 25, 18)}")
