"""
03 - Conditions (if / elif / else)
-----------------------------------
Conditional statements let your program make decisions.
"""

age = 20

# --- Basic if/else ---
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# --- if / elif / else chain ---
marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# --- Nested conditions ---
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")

# --- Logical operators: and / or / not ---
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("Great day for a walk.")

if temperature > 35 or is_raining:
    print("Maybe stay indoors.")

# --- Ternary (conditional expression) ---
status = "adult" if age >= 18 else "minor"
print("Status:", status)

# --- Checking membership in conditions ---
fruits = ["apple", "banana", "mango"]
fruit = "banana"

if fruit in fruits:
    print(f"{fruit} is in the list.")
else:
    print(f"{fruit} is not in the list.")

# --- Chained comparisons ---
num = 15
if 10 < num < 20:
    print("num is between 10 and 20")

# --- match-case (Python 3.10+) ---
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Some other day")
