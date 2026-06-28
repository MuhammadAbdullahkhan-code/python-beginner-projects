"""
Mini Project: Calculator
-------------------------
A simple command-line calculator supporting basic arithmetic operations.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter calculation (e.g. 5 + 3) or 'exit': ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid format. Use: number operator number (e.g. 5 + 3)\n")
            continue

        num1_str, operator, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Both values must be numbers.\n")
            continue

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print(f"Unknown operator '{operator}'. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")


# --- Quick non-interactive demo (so the file shows behavior when run) ---
def demo():
    print("--- Demo mode (no input required) ---")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("9 / 0 =", divide(9, 0))
    print("9 / 3 =", divide(9, 3))


if __name__ == "__main__":
    demo()
    print()
    # Uncomment the line below to run the interactive version:
    # calculator()
