"""
01 - Variables
--------------
Variables are names that point to values stored in memory.
Python is dynamically typed, so you don't need to declare a type.
"""

name = "Ali"
age = 25
height = 5.9
is_student = True

print(name, age, height, is_student)

# --- Multiple assignment ---
x, y, z = 1, 2, 3
print(x, y, z)

# --- Same value to multiple variables ---
a = b = c = 0
print(a, b, c)

# --- Checking type ---
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student))  # <class 'bool'>

# --- Type casting ---
age_str = str(age)
pi_int = int(3.9)        # truncates to 3
num_from_str = float("12.5")

print(age_str, type(age_str))
print(pi_int)
print(num_from_str)

# --- Constants (by convention, uppercase names) ---
PI = 3.14159
MAX_USERS = 100

# --- Dynamic typing: a variable can change type ---
value = 10
print(value, type(value))
value = "now a string"
print(value, type(value))

# --- Variable naming rules ---
# valid: name, _name, name2, my_name
# invalid: 2name, my-name, class (reserved keyword)

first_name = "Muhammad"
_private_var = "hidden"
user2 = "second user"

print(first_name, _private_var, user2)
