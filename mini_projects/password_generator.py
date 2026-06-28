"""
Mini Project: Password Generator
----------------------------------
Generates random, secure passwords based on user-specified criteria.
"""

import random
import string


def generate_password(length=12, use_upper=True, use_lower=True,
                       use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 for decent security.")

    char_pool = ""
    guaranteed_chars = []

    if use_lower:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_upper:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        char_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    if not char_pool:
        raise ValueError("At least one character type must be enabled.")

    # Fill the rest of the password length with random characters from the pool
    remaining_length = length - len(guaranteed_chars)
    random_chars = [random.choice(char_pool) for _ in range(remaining_length)]

    password_chars = guaranteed_chars + random_chars
    random.shuffle(password_chars)  # avoid predictable ordering

    return "".join(password_chars)


def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    levels = {0: "Very Weak", 1: "Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
    return levels[score]


def run_generator():
    print("=== Password Generator ===")
    try:
        length = int(input("Password length (default 12): ") or 12)
    except ValueError:
        length = 12

    password = generate_password(length=length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")


if __name__ == "__main__":
    print("--- Demo: generating a few sample passwords ---\n")
    for length in (8, 12, 16, 20):
        pwd = generate_password(length=length)
        print(f"Length {length:>2}: {pwd}  -> {password_strength(pwd)}")

    print()
    # Uncomment to run interactively:
    # run_generator()
