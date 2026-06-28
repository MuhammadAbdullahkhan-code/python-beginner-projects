"""
Mini Project: Number Guessing Game
------------------------------------
The computer picks a random number, and the player tries to guess it
within a limited number of attempts, getting hints along the way.
"""

import random


def play_game(min_num=1, max_num=100, max_attempts=7):
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        guess_str = input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: ")

        if not guess_str.isdigit():
            print("Please enter a valid number.\n")
            continue

        guess = int(guess_str)
        attempts += 1

        if guess == secret_number:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s).")
            return True
        elif guess < secret_number:
            print("Too low! Try a higher number.\n")
        else:
            print("Too high! Try a lower number.\n")

    print(f"\nGame over! The number was {secret_number}.")
    return False


def play_game_auto_demo(min_num=1, max_num=100, max_attempts=7):
    """
    Non-interactive demo version that simulates guesses automatically,
    using a simple binary-search strategy. Useful for testing without
    needing to type input manually.
    """
    secret_number = random.randint(min_num, max_num)
    low, high = min_num, max_num
    attempts = 0

    print("=== Number Guessing Game (Auto Demo) ===")
    print(f"Secret number is between {min_num} and {max_num} (hidden).")

    while attempts < max_attempts:
        guess = (low + high) // 2
        attempts += 1
        print(f"Attempt {attempts}: guessing {guess}")

        if guess == secret_number:
            print(f"Correct! The number was {secret_number}. Took {attempts} attempt(s).")
            return
        elif guess < secret_number:
            print("Too low!")
            low = guess + 1
        else:
            print("Too high!")
            high = guess - 1

    print(f"Ran out of attempts. The number was {secret_number}.")


if __name__ == "__main__":
    play_game_auto_demo()
    print()
    # Uncomment to play interactively:
    # play_game()
