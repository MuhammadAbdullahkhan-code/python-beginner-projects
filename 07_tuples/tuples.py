"""
07 - Tuples
-----------
Tuples are ordered, IMMUTABLE collections of items.
"""

# --- Creating tuples ---
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (5,)        # note the comma -- without it, it's just an int
empty_tuple = ()

print(coordinates)
print(colors)
print(single_item, type(single_item))

# --- Tuples can hold mixed types ---
person = ("Ali", 25, "Karachi")
print(person)

# --- Accessing elements ---
print(colors[0])     # red
print(colors[-1])    # blue

# --- Slicing ---
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])  # (2, 3, 4)

# --- Tuples are immutable: this would raise an error ---
# colors[0] = "yellow"   # TypeError: 'tuple' object does not support item assignment

# --- But you CAN reassign the whole variable ---
colors = ("yellow", "green", "blue")
print(colors)

# --- Tuple unpacking ---
name, age, city = person
print(name, age, city)

# --- Unpacking with * (collects remaining items) ---
first, *middle, last = (1, 2, 3, 4, 5)
print("first:", first, "middle:", middle, "last:", last)

# --- Nested tuples ---
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])      # (3, 4)
print(nested[1][0])   # 3

# --- Tuple methods ---
sample = (1, 2, 2, 3, 2, 4)
print("Count of 2:", sample.count(2))
print("Index of 3:", sample.index(3))

# --- Why use tuples over lists? ---
# 1. Immutability -> safer for data that shouldn't change (e.g. coordinates)
# 2. Slightly faster than lists
# 3. Can be used as dictionary keys (lists cannot, since they're mutable)

location_data = {
    (24.8607, 67.0011): "Karachi",
    (31.5497, 74.3436): "Lahore",
}
print(location_data[(24.8607, 67.0011)])

# --- Converting between list and tuple ---
list_version = list(numbers)
tuple_version = tuple(list_version)
print(list_version, tuple_version)

# --- Looping through a tuple ---
for color in colors:
    print("Color:", color)
