"""
05 - Functions
--------------
Functions let you package reusable blocks of logic.
"""

# --- Basic function ---
def greet():
    print("Hello!")

greet()

# --- Function with parameters ---
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Ahmed")

# --- Function with return value ---
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# --- Default parameter values ---
def greet_with_default(name="Guest"):
    print(f"Welcome, {name}!")

greet_with_default()
greet_with_default("Hina")

# --- Keyword arguments ---
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(age=30, city="Karachi", name="Zain")

# --- Variable number of arguments (*args) ---
def total_sum(*numbers):
    return sum(numbers)

print("Total:", total_sum(1, 2, 3, 4, 5))

# --- Variable keyword arguments (**kwargs) ---
def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Omar", age=28, profession="Engineer")

# --- Combining *args and **kwargs ---
def full_demo(a, b, *args, **kwargs):
    print("a:", a, "b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

full_demo(1, 2, 3, 4, x=10, y=20)

# --- Lambda functions (anonymous, single-expression) ---
square = lambda x: x * x
print("Square of 6:", square(6))

add_lambda = lambda a, b: a + b
print("Lambda sum:", add_lambda(4, 7))

# --- Functions as arguments (higher-order functions) ---
def apply_operation(x, y, operation):
    return operation(x, y)

print("Using lambda as argument:", apply_operation(10, 5, lambda a, b: a - b))

# --- Recursion ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# --- Docstrings & type hints ---
def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    return a / b

print("Divide:", divide(10, 2))
