"""
06 - Lists
----------
Lists are ordered, mutable collections of items.
"""

# --- Creating lists ---
fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

print(fruits)
print(numbers)
print(mixed)

# --- Accessing elements ---
print(fruits[0])      # apple
print(fruits[-1])     # mango (last item)

# --- Slicing ---
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[::-1])  # reversed list

# --- Modifying lists ---
fruits.append("orange")
fruits.insert(1, "grape")
print(fruits)

fruits.remove("banana")
popped = fruits.pop()       # removes and returns last item
print(fruits, "| popped:", popped)

fruits[0] = "kiwi"           # direct index assignment
print(fruits)

# --- Useful list methods ---
numbers.sort()
print("Sorted:", numbers)

numbers.sort(reverse=True)
print("Reverse sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

print("Length:", len(numbers))
print("Count of 3:", numbers.count(3))
print("Index of 4:", numbers.index(4))

# --- Combining lists ---
combined = fruits + numbers
print("Combined:", combined)

# --- Copying lists (important: avoids reference issues) ---
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print("Original:", original, "| Copy:", copy_list)

# --- List comprehensions ---
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)

# --- Nested lists (2D lists) ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Matrix row 1:", matrix[1])
print("Matrix element [2][0]:", matrix[2][0])

# --- Iterating over a list ---
for fruit in fruits:
    print("Fruit:", fruit)

# --- Checking membership ---
print("apple" in ["apple", "pear"])  # True/False example
