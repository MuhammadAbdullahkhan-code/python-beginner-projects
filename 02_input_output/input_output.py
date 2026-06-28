"""
02 - Input and Output
---------------------
input() reads a line of text from the user (always returns a string).
print() writes output to the console.
"""

# --- Basic output ---
print("Hello, World!")
print("Multiple", "values", "separated", "by", "spaces")
print("Custom separator", "here", sep=" | ")
print("No newline at the end", end=" ")
print("-- continues on the same line")

# --- Basic input ---
# name = input("Enter your name: ")
# print("Hello,", name)

# --- Input always returns a string, so cast when needed ---
# age_str = input("Enter your age: ")
# age = int(age_str)
# print("Next year you'll be", age + 1)

# --- Formatted output ---
name = "Sara"
age = 22
print(f"{name} is {age} years old.")               # f-string
print("{} is {} years old.".format(name, age))      # .format()
print("%s is %d years old." % (name, age))          # %-formatting (older style)

# --- Formatting numbers ---
price = 1234.5678
print(f"Price: {price:.2f}")        # 2 decimal places
print(f"Price: {price:,.2f}")       # with thousands separator

# --- Multi-line input simulation (commented, since this runs non-interactively) ---
# user_data = input("Enter name,age separated by comma: ")
# u_name, u_age = user_data.split(",")
# print(f"Name: {u_name.strip()}, Age: {u_age.strip()}")

# --- Reading multiple values in one line ---
# x, y = input("Enter two numbers separated by space: ").split()
# x, y = int(x), int(y)
# print("Sum:", x + y)

if __name__ == "__main__":
    print("\n--- Demo without live input ---")
    simulated_name = "Bilal"
    simulated_age = "30"  # pretend this came from input()
    age_value = int(simulated_age)
    print(f"{simulated_name} will be {age_value + 1} next year.")
