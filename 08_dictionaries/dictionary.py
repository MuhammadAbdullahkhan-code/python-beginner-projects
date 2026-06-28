"""
08 - Dictionaries
-----------------
Dictionaries store data as key-value pairs. Keys must be unique and hashable.
"""

# --- Creating dictionaries ---
student = {
    "name": "Areeba",
    "age": 21,
    "courses": ["Math", "CS"]
}
print(student)

empty_dict = {}
using_constructor = dict(name="Hassan", age=30)
print(using_constructor)

# --- Accessing values ---
print(student["name"])
print(student.get("age"))
print(student.get("grade", "N/A"))   # default if key doesn't exist

# --- Adding / updating values ---
student["grade"] = "A"               # add new key
student["age"] = 22                  # update existing key
print(student)

# --- Removing values ---
del student["grade"]
print(student)

removed_age = student.pop("age")
print("Removed age:", removed_age)
print(student)

# --- Checking keys ---
print("name" in student)        # True
print("age" in student)         # False (we removed it)

# --- Looping through dictionaries ---
student["age"] = 22  # add it back for demo
for key in student:
    print("Key:", key)

for key, value in student.items():
    print(f"{key} -> {value}")

for value in student.values():
    print("Value:", value)

# --- Nested dictionaries ---
users = {
    "user1": {"name": "Bilal", "age": 25},
    "user2": {"name": "Sara", "age": 28},
}
print(users["user1"]["name"])

# --- Dictionary comprehension ---
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

# --- Merging dictionaries ---
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
merged = {**dict_a, **dict_b}   # dict_b overwrites overlapping keys
print(merged)

# Python 3.9+ also supports the | operator
merged_v2 = dict_a | dict_b
print(merged_v2)

# --- Useful methods ---
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

student.update({"city": "Lahore", "age": 23})
print(student)

student.clear()
print("After clear:", student)
