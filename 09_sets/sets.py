"""
09 - Sets
---------
Sets are unordered collections of UNIQUE items.
"""

# --- Creating sets ---
fruits = {"apple", "banana", "mango"}
numbers = {1, 2, 3, 3, 2, 1}   # duplicates are automatically removed
print(fruits)
print(numbers)   # {1, 2, 3}

empty_set = set()   # NOTE: {} creates an empty dict, not a set!

# --- Adding and removing elements ---
fruits.add("orange")
print(fruits)

fruits.remove("banana")    # raises KeyError if not found
fruits.discard("kiwi")     # does nothing if not found (safe)
print(fruits)

popped_item = fruits.pop()  # removes a random item (sets are unordered)
print("Popped:", popped_item, "| Remaining:", fruits)

# --- Set operations ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)               # or a.union(b)
print("Intersection:", a & b)        # or a.intersection(b)
print("Difference (a - b):", a - b)  # or a.difference(b)
print("Symmetric difference:", a ^ b)  # items in a or b but not both

# --- Checking membership ---
print(3 in a)       # True
print(10 in a)      # False

# --- Subset / superset checks ---
small = {1, 2}
print(small.issubset(a))     # True
print(a.issuperset(small))   # True

# --- Converting between list and set ---
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
unique_items = set(list_with_duplicates)
print("Unique items:", unique_items)
back_to_list = list(unique_items)
print("Back to list:", back_to_list)

# --- Set comprehension ---
squares_set = {x ** 2 for x in range(1, 6)}
print(squares_set)

# --- Frozenset (immutable set) ---
frozen = frozenset([1, 2, 3])
print(frozen)
# frozen.add(4)   # AttributeError -- frozensets can't be modified

# --- Looping through a set ---
for fruit in fruits:
    print("Fruit:", fruit)

# --- Practical use case: removing duplicates from a list ---
emails = ["a@test.com", "b@test.com", "a@test.com", "c@test.com"]
unique_emails = list(set(emails))
print("Unique emails:", unique_emails)
